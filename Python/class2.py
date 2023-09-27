class Names:
    def __init__(self,a, b, c):
        self.name = a
        self.middle_name = b
        self.surname = c

    def info(self):
        return f"{self.name} {self.middle_name} {self.surname}"

    def x(self):
        return f"{self.name}"

    def y(self):
        return f"{self.middle_name}"

    def z(self):
        return f"{self.surname}"


class ABC:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"name = {self.name} age = {self.age}"


a1 = ABC("Nobel", 23)
print(a1.info())

n1 = Names("Nobel", "Sampang", "Rai")
print(n1.x())
