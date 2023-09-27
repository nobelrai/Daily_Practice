class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def sub(self):
        return self.num1 - self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):
        return self.num1 / self.num2

    def mod(self):
        return self.num1 % self.num2


class Area(Calculator):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def area_of_rectangle(self):
        return self.num1 * self.num2


a1 = Area(23, 45)
print(a1.area_of_rectangle())
