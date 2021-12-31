import hashlib
import PyMySQLHelper



"""实现模拟登录"""

class Login(object):


    def main(self):
        account = input("please input your account")
        password = input("please input your password")
        if not self.check_accout(account):
            print("账号不存在")
        else:
            if self.check_password(account, password):
                print('登录成功')
            else:
                print('登录失败请检查密码')


    def check_password(self,account:str,password:str)-> bool:
        sql = f"select password from user where account = '{account}'"
        sqlpassword = PyMySQLHelper.PyMySQLHelper().query_one(sql)[0]
        if password == sqlpassword:
            return True
        else:
            return False


    def check_accout(self, account: str) -> bool:

        # 需要加上引号
        sql = f"select * from user where account = '{account}'"
        if PyMySQLHelper.PyMySQLHelper().query_one(sql):
            # print(PyMySQLHelper.PyMySQLHelper().query_one(sql))
            return True
        else:
            return False



if __name__ == '__main__':
    test = Login()
    # test.check_password('root', '123456')
    test.main()
