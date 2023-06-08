class Animal:
    #age = 1
    def __init__(self):
        self.age = 1
    #def __init__(self, age):
    #    self.age = age
    
    def getAge(self):
        return self.age
    
    def birthHappy(self):
        self.age += 1

if __name__=='__main__':
    a1 = Animal()
    print("11",a1.age)
    a1.birthHappy()
    print("11",a1.getAge())
