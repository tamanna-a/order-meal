import pymysql
import json

class Database:
    def __init__(self):
       self.host = 'localhost'
       self.user = 'root'
       self.password = "eamaitre_7_A"
       self.db_schema = 'homefood'

    def _get_connection(self):
        conn = pymysql.connect(host = self.host, user = self.user,
                              password = self.password,
                               db = self.db_schema,
                               cursorclass=pymysql.cursors.DictCursor)

        return conn

if __name__ == '__main__':
    db = Database()
    cursor = db._get_connection().cursor()
    sql = 'select * from user'

    res = cursor.execute(sql)

    # Fetch the rows
    res = cursor.fetchall()

    print("result = \n",
          json.dumps(res, indent=2, default=str))

