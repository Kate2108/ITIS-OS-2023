import random
import time


def rand(min, max):
    return random.randint(min, max)


def rand_sign():
    match rand(1,4):
        case 1:
            return "+"
        case 2:
            return "-"
        case 3:
            return "*"
        case 4:
            return "/"



for i in range(0, rand(120, 180)):
    print(str(rand(1, 9)) + " " + rand_sign() + " " + str(rand(1, 9)), flush = True)
    time.sleep(1)