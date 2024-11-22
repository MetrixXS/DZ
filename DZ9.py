

class Character:
    def __init__(self, name):
        self.name = name
        self.__health = 100
        self.__energy = 100
        self.__weapon = None

    def attack(self):
        if self.__energy >= 10:
            self.__energy -= 10
            print(f"{self.name} атакує з допомогою {self.__weapon}.")
        else:
            print(f"{self.name} У вас немаэ энергії для атакування!")

    def take_damage(self):
        self.__health -= 10
        if self.__health <= 0:
            print(f"Персонаж {self.name} загинув")
        else:
            print(f"{self.name} отримав 10 урона. Залишилося здоров'я: {self.__health}.")

    def equip_weapon(self, magic):
        self.__weapon = magic
        print(f"{self.name} тепер озброєний: {self.__weapon}.")

    def get_status(self):
        weapon_status = self.__weapon if self.__weapon else "Немає зброї"
        return f"Ім'я: {self.name}, Здоров'е: {self.__health}, Энергія: {self.__energy}, Зброя: {weapon_status}"


character1 = Character
print(character1)