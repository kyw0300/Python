from random import random
def getHoljjak():
    rnd = random()
    
    if rnd>0.5:
        return "홀"
    else:
        return "짝"
    
com = getHoljjak()
print("computer ==>",com)