from day03.my_oop01 import Animal

class Human(Animal):
    def __init__(self):
        super().__init__()
        self.tools = []
        self.tools.append("반지")
        
    def farming(self, tool):
        self.tools.append(tool)
        
    def __str__(self):
        ret = str(self.tools)
        
        return ret
        
h1 = Human()
h1.farming("손도끼")
print(h1.tools)
h1.farming("항아리")
print(h1.__str__())
h1.birthHappy()
print(h1.age)
print(h1)