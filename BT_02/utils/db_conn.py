import mysql.connector
from loguru import logger

class MySQLConn:
   def __init__(self) -> None:
      pass

   def create_conn(self):
      conn = mysql.connector.connect(host='localhost',
                                 user='root',
                                 passwd='root',
                                 database='qlst')
      logger.info('Connected to MySQL Database')
      return conn

# cur = myconn.cursor()
# cur.execute("show databases")
# for row in cur:
#    print(row)

# myconn.close()