import os
import random

vMyNum = random.randint(1,100)
fileName = 'Guests'
txtFile = 'C:\\PYCODE\\Data\\' + fileName + '.txt'
inFile=open(txtFile, 'r')
for line in iter(inFile):
   prtLine = line.rstrip()
   print(prtLine)
inFile.close()

outName = 'C:\\PYCODE\\Data\\' + fileName + '_' + str(vMyNum) + '.txt'
print(outName)
outFile = open(outName, 'w')
outFile.write('Hello, the random number was ' + str(vMyNum) + '.')
outFile.close()
