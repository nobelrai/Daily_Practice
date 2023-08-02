class Calculate:
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
    
class Volume(Calculate):
    def __init__(self,num1, num2, num3):
        super().__init__(num1, num2)
        self.num3 = num3
    
    def volume_of_rectangle(self):
        return self.num1 * self.num2 * self.num3
    
    def mul(self):
        return self.num1 * self.num2 * self.num3

    
c1 = Calculate(2,5)
Cu = Volume(2,3,5)
print(Cu.volume_of_rectangle())
print(Cu.mul())
print(c1.sub())