import random

class Dice:
    def kostka6(x,y):
        return random.randint(x,y)
    def kostka4(x,y):
        return random.randint(x,y)
    def kostka8(x,y):
        return random.randint(x,y)
    def kostka10(x,y):
        return random.randint(x,y)
    def kostka12(x,y):
        return random.randint(x,y)
    def kostka20(x,y):
        return random.randint(x,y)
    

kostka4 = Dice.kostka4(1,4)
kostka6 = Dice.kostka6(1,6)
kostka8 = Dice.kostka6(1,8)
kostka10 = Dice.kostka6(0,9)
kostka12 = Dice.kostka6(1,12)
kostka20 = Dice.kostka6(1,20)
print('Kostka k4 - Wynik:', kostka4)
print('Kostka k6 - Wynik:', kostka6)
print('Kostka k8 - Wynik:', kostka8)
print('Kostka k10 - Wynik:', kostka10)
print('Kostka k12 - Wynik:', kostka12)
print('Kostka k20 - Wynik:', kostka20)
