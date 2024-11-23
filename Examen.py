import requests
from bs4 import BeautifulSoup

class SiteManager:
    def __init__(self):
        self.sites = []

    def add_site(self, url):
        if url not in self.sites:
            self.sites.append(url)
            return f"Сайт {url} доданий. Дякую за використання!"
        return "Сайт вже існує у списку."

    def get_sites(self):
        return self.sites

    @staticmethod
    def display_message(message):
        print(message)


class SiteParser:
    def fetch_content(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Помилка завантаження сайту {url}: {e}")
            return None

    def count_matches(self, url, request):
        html_content = self.fetch_content(url)
        if not html_content:
            return 0
        soup = BeautifulSoup(html_content, "html.parser")
        text = soup.get_text().lower()
        return text.count(request.lower())


class UserInterface:
    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def display_message(message):
        print(message)

    def show_menu(self):
        print("Меню:")
        print("1. Додати сайт")
        print("2. Показати сайти")
        print("3. Шукати інформацію")
        print("4. Вихід")
        return input("Виберіть пункт меню: ")


class SearchApp:
    def __init__(self):
        self.site_manager = SiteManager()
        self.site_parser = SiteParser()
        self.user_interface = UserInterface()

    def sort_results(self, results):
        return sorted(results, key=self.sort_key, reverse=True)

    def sort_key(self, result):
        return result[1]
    def run(self):
        while True:
            choice = self.user_interface.show_menu()
            if choice == "1":
                url = self.user_interface.get_input("Введіть URL-адресу сайту: ")
                message = self.site_manager.add_site(url)
                self.user_interface.display_message(message)
            elif choice == "2":
                sites = self.site_manager.get_sites()
                if sites:
                    self.user_interface.display_message("Додані сайти:")
                    for site in sites:
                        self.user_interface.display_message(site)
                else:
                    self.user_interface.display_message("Список сайтів порожній.")
            elif choice == "3":
                answer = self.user_interface.get_input("Введіть текст для пошуку: ")
                sites = self.site_manager.get_sites()
                if not sites:
                    self.user_interface.display_message("Список сайтів порожній..")
                else:
                    results = []
                    for site in sites:
                        coincidence = self.site_parser.count_matches(site, answer)
                        results.append((site, coincidence))

                    results = self.sort_results(results)
                    self.user_interface.display_message("Результати пошуку:")
                    for site, count in results:
                        self.user_interface.display_message(f"{site}: {count} збігів")
            elif choice == "4":
                self.user_interface.display_message("Вихід із програми.")
                break
            else:
                self.user_interface.display_message("Некоректний вибір, спробуйте знову.")
                continue



if __name__ == "__main__":
    app = SearchApp()
    app.run()