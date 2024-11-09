class Rectangle:
    def __init__(self):
        self.height = 8
        self.weight = 3
        self.calculate_area = self.height * self.weight
        self.calculate_perimiter = 2 * (self.height + self.height)

    def calculator (self):
        print(f"Area = {self.calculate_area} Perimiter = {self.calculate_perimiter}")

rectangle1 = Rectangle()
rectangle1.calculator()