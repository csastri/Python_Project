import random
import ctypes  # An included library with Python install.
def MsgBox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

vMyNum = random.randint(1,7)
vRestList = ['TGIF','Don Cucos','Macaroni Grill', 'Food Court', 'Urban Pizza', \
             'El Pollo Loco', 'Thai Palace', '', 'Sharkeys']
#print(vMyNum)
#print('You should eat at ' + vRestList[vMyNum])

MsgBox('YOU SHOULD EAT AT ... ', vRestList[vMyNum], 1)

#vYourNum = 0

#print('What is your number?')

#vYourNum = input()
#vYourNum = int(vYourNum)

#if vMyNum == vYourNum:
    #print('You got me the number was ' + str(vMyNum))
#else:
    #print('Gotcha My num was '  + str(vMyNum) + ' Your number was ' + str(vYourNum))
