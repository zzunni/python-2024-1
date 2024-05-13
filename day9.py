from random import randint

class Dice:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.size = 30
        self.value = 1

    def read_dice(self):
        return self.value

    def print_dice(self):
        print(f"주사위의 값 {self.value}")

    def roll_dice(self):
        self.value = randint(1, 6)

d = Dice(100, 100)
d.roll_dice()
d.print_dice()