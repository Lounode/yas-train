import random

def randomNumberGen(size):
    if size == 1:
        return int(random.choice(list(range(0,10))))
    if size == 2:
        return int(random.choice(list(range(1,10)))*10+random.choice(list(range(0,10))))
    if size == 3:
        return int(random.choice(list(range(1,10)))*100+random.choice(list(range(0,10)))*10+random.choice(list(range(0,10))))
    if size == 4:
        return int(random.choice(list(range(1,10)))*1000+random.choice(list(range(0,10)))*100+random.choice(list(range(0,10)))+random.choice(list(range(0,10)))*10)
def randomNumber():#return one number range 1 to 9999
    return str(randomNumberGen(int(random.choice(list(range(1,5))))))