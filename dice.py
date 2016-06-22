import random

def kostka4(x):
    return random.randint(1,x)
def kostka6(x):
    return random.randint(1,x)
def kostka8(x):
    return random.randint(1,x)
def kostka10(x):
    return random.randint(0,x)
def kostka12(x):
    return random.randint(1,x)
def kostka20(x):
    return random.randint(1,x)

k4 = kostka4(4)
k6 = kostka6(6)
k8 = kostka8(8)
k10 = kostka10(9)
k12 = kostka12(12)
k20 = kostka20(20)

print('Kostka k4 - Wynik:', k4)
print('Kostka k6 - Wynik:', k6)
print('Kostka k8 - Wynik:', k8)
print('Kostka k10 - Wynik:', k10)
print('Kostka k12 - Wynik:', k12)
print('Kostka k20 - Wynik:', k20)

print('2k4 + 3k6 =', 2*k4 + 3*k6)
print('k4 + 2k6=', k4 + 2*k6)
