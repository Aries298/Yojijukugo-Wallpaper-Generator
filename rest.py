import random

def gennum():
    num = random.randint(1,150)
    return num if random.randint(0,1) else -num
