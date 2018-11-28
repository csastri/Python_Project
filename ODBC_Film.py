import pyodbc
import datetime

dbconn = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=DELLPC3\DB1;'
    r'DATABASE=Movies;'
    r'Trusted_Connection=yes;'
    )
#vFilmYear = 2004
print('Enter the Film release year?')

vFilmYear = input()
vFilmYear = int(vFilmYear)

vRptYear = str(vFilmYear)
vCount = 0

fileName = 'Films_Released_In_'
outName = 'C:\\PYCODE\\Data\\' + fileName + vRptYear + '.csv'
print(outName)
outFile = open(outName, 'w')

outFile.write('Title,Release Date,Run Time Minutes\n')

dbcursor = dbconn.cursor()

SQL = 'SELECT Title, RunTimeMinutes' \
    ', CONVERT(VARCHAR(10), ReleaseDate, 101) AS [Release_Date]' \
    ' FROM dbo.Film'\
    ' WHERE DATEPART("yyyy", ReleaseDate) = ' + vRptYear +\
    ' ORDER BY ReleaseDate'

for row in dbcursor.execute(SQL):
    outFile.write(chr(34) + row.Title + chr(34) \
            + ',' +  chr(34) + row.Release_Date + chr(34) \
            + ',' + chr(34) + str(row.RunTimeMinutes) + chr(34) + '\n')
    vCount = vCount + 1
    
dbcursor.close
dbconn.close

if vCount == 0:
    outFile.write('No films were released in the year ' + vRptYear + '.')
else:
    outFile.write(str(vCount) + ' films were released in ' + vRptYear + '.')

outFile.close()
