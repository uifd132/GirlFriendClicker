import random

def textGen():
    with open(r"Texts.txt") as f:
        lines = f.readlines()
        random_int = random.randint(0,len(lines)-1)
        return lines[random_int]

