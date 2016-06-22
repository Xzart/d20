import random

## Dice functions
def dice4(x):
    return random.randint(1,x)
def dice6(x):
    return random.randint(1,x)
def dice8(x):
    return random.randint(1,x)
def dice10(x):
    return random.randint(0,x)
def dice12(x):
    return random.randint(1,x)
def dice20(x):
    return random.randint(1,x)

##List values
k4 = dice4(4)
k6 = dice6(6)
k8 = dice8(8)
k10 = dice10(9)
k12 = dice12(12)
k20 = dice20(20)

print('Test - Dice functions. No Magic Methods')
print('Dice k4 - Result:', k4)
print('Dice k6 - Result:', k6)
print('Dice k8 - Result:', k8)
print('Dice k10 - Result:', k10)
print('Dice k12 - Result:', k12)
print('Dice k20 - Result:', k20)
print('Sum of all dice:',k4 + k6 + k8 + k10 + k12 + k20,'\n')

print('Test - Dice operations.')
print('2k4 + 3k6 :', 2*k4 + 3*k6)
print('k4 + 2k6 :', k4 + 2*k6)
