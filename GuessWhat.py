import random

#vMyNum = random.randint(1,9)
#vRestList = ['A1','B1','C1','D1','E1','F1','G1','H1','I1','J']
#print(vMyNum)
#print('Eat at ' + vRestList[vMyNum])
4
#vYourNum = 0

print('What is your number?')

vYourNum = input()
vYourNum = int(vYourNum)
vMyNum = random.randint(1,9)
if vMyNum == vYourNum:
    print('You got me the number was ' + str(vMyNum))
else:
    print('Gotcha My num was '  + str(vMyNum) + ' Your number was ' + str(vYourNum))
