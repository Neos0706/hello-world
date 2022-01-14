import pymysql



class PyMySQLHelper(object):

    def __init__(self,host='localhost', port=3306, user='root',password='',database='python3',charset='utf8') -> None:
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, database=self.database, charset=self.charset)
            self.cursor = self.conn.cursor()
        except pymysql.Error as e:
            print(f'MySql Error: {e}')

    def cud(self, sql):
        try:
            print(sql)
            self.cursor.execute(sql)

        except pymysql.Error as e:
           print(f'MySql Error: {e}') 
        else:
            self.commit()
        
    # 执行retrievesql命令
    def query(self, sql):
        try:
            rows = self.cursor.execute(sql)
            return rows
        except pymysql.Error as e:
            print(f'MySql Error: {e}')

    def query_one(self,sql):
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            return result
        except pymysql.Error as e:
            print(f'MySql Error: {e}')


    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()
        print('mysql connect release by close')

    # 不知道 会不会用到
    # def __del__(self):
    #     print("mysql connect release by __del__")
    #     self.close()




if __name__ == '__main__':
    test = PyMySQLHelper()
    test.retrieve('1')