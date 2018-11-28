
import pyodbc
import datetime

class sqlConnection():
   def __init__(self):
       #SQL Connection variables
      strDriver = r'DRIVER={ODBC Driver 13 for SQL Server};'
      strServer = r'SERVER=DELLPC3\DB1;'
      strDatabase = r'DATABASE=Movies;'
      strTrustedC = r'Trusted_Connection=yes;'
    
       #Establish connection to SQL server
      try:
         cnxn = pyodbc.connect(strDriver + strServer + strDatabase + strTrustedC)
         cursor = cnxn.cursor()         
         print ("Connection to SQL server success")
      except:
         print ("Connection to SQL server failed")


   def __enter__(self):
      return self



   def __exit__(self, extype, exvalue, traceback):  
      print ("Connection closed to SQL server")


with sqlConnection() as cnxn:
   # do stuff with conn
   # leaving the block closes the db-connection
   print("X")