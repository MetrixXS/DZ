class InvalidAgeError(Exception):
    pass


class Person:
    def __init__(self, age):
        self.age = age

    def set_age(self):
        if self.age < 0 or self.age > 120:
            raise InvalidAgeError(f"WRONG")


try:
    person1 = Person(121)
    person1.set_age()
except InvalidAgeError:
    print("ERROR")