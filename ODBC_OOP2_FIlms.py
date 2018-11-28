import pyodbc

class Db:
    DRIVER   =  r'DRIVER={ODBC Driver 13 for SQL Server};'
    SERVER   =  r'SERVER=SERVER=DELLPC3\DB1;'
    DATABASE =  r'DATABASE=Movies;'
    TRUSTED = r'Trusted_Connection=yes;'
    #USERNAME =  r'UID=sa;' 
    #PASSWORD =  r'PWD=1'    

    def __init__(self):
        #self.cnxn = pyodbc.connect(self.DRIVER + self.SERVER + self.DATABASE + self.USERNAME + self.PASSWORD)
        self.cnxn = pyodbc.connect(self.DRIVER + self.SERVER + self.DATABASE + self.TRUSTED)
        self.cursor = self.cnxn.cursor()                

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("__exit__")
        self.cursor.close()
        self.cnxn.close()   


with Db() as d:
    print(d)