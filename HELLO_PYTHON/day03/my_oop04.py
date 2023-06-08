class LeeJY:
    def __init__(self):
        self.cnt_company = 20
        
    def seat(self):
        self.cnt_company += 1
        
class Bin:
    def __init__(self):
        self.amount_oil = 10000
        
    def dig(self):
        self.amount_oil *= 2
        
class KimJeungUn:
    def __init__(self):
        self.cnt_nuclear = 30
    
    def aoji(self):
        self.cnt_nuclear += 2
        
class KimJiWan(LeeJY,Bin,KimJeungUn):
    def __init__(self):
        LeeJY.__init__(self)
        Bin.__init__(self)
        KimJeungUn.__init__(self)
        
        self.money = 10000
        
    def save(self):
        self.money += 1000 
        
kjw = KimJiWan()

print(kjw.cnt_company)
print(kjw.amount_oil)
print(kjw.cnt_nuclear)
print(kjw.money)

kjw.seat()
kjw.dig()
kjw.aoji()
kjw.save()

kjw.seat()
kjw.dig()
kjw.aoji()
kjw.save()

print()
print(kjw.cnt_company)
print(kjw.amount_oil)
print(kjw.cnt_nuclear)
print(kjw.money)