class Character:
    def __init__ (self, name , health):
        self.name = name
        self.health = health

    def attack(self, character):
        print(character.name,",yours HP", character.health,"." )

class Hero(Character):
    def __init__(self,name,health,weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

class Enemy(Character):
    def __init__(self,name,health,damage):
        self.name = name
        self.health = health
        self.weapon = damage

character1 = Character("Itadori", 195)
hero1 = Hero("Gojo", 300, "Purple")
enemy1 = Enemy("Sukuna", 200,85)
character1.attack(character1)
character1.attack(hero1)
character1.attack(enemy1)