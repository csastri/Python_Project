import pyodbc
import pandas as pd

### instance a python db connection object- same form as psycopg2/python-mysql drivers also
#conn = pymssql.connect(server="172.0.0.1", user="howens",password="some_fake_password", port=63642)  # You can lookup the port number inside SQL server. 

dbconn = pyodbc.connect(
    r'DRIVER={ODBC Driver 13 for SQL Server};'
    r'SERVER=DELLPC3\DB1;'
    r'DATABASE=Movies;'
    r'Trusted_Connection=yes;'
    )


vRptYear = input('Enter a Report Year : ')
#vRptYear = '2015'
sqlstmnt = 'SELECT Title, RunTimeMinutes' \
    ', CONVERT(VARCHAR(10), ReleaseDate, 101) AS [Release_Date]' \
    ' FROM dbo.Film'\
    ' WHERE DATEPART("yyyy", ReleaseDate) = ' + vRptYear +\
    ' ORDER BY ReleaseDate'
print(sqlstmnt)
## Excute Query here
df = pd.read_sql(sqlstmnt,dbconn)
ctr = len(df.index)
print(str(ctr))

if ctr == 0:
    print('No films were released in ' + str(vRptYear))
else:
    df.to_csv('C:\\PYCODE\\Data\\Movies_Panda_' + vRptYear + '.csv')
    csvdata = pd.read_csv('C:\\PYCODE\\Data\\Movies_Panda_' + str(vRptYear) + '.csv',\
                parse_dates=True, index_col = 'Title')     
    print(csvdata[['Release_Date','RunTimeMinutes']],end="")
    print()
    print('='*50)
    if ctr == 1:
        print(str(ctr) + ' film was released in ' + vRptYear + '.')
    else:
        print(str(ctr) + ' films were released in ' + vRptYear + '.')
print('End of Program')