import hashlib
import hmac
import PyMongoHelper



"""实现模拟登录"""

class Login(object):

    def main(self):
        account = input("please input your account")
        password = input("please input your password")
        if not self.check_accout(account):
            print("账号不存在")
        else:
            if self.check_password(password):
                print('登录成功')
            else:
                print('登录失败请检查密码')


    def check_password(self,password:str)-> bool:
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        if hash_password == str(self.cursor['password']):
            return True
        else:
            return False


    def check_accout(self, account: str) -> bool:

        # 需要加上引号
        # sql = f"select * from user where account = '{account}'"
        query_json = {'account': account}
        # 保存查询结果，减少查询次数
        cursor = PyMongoHelper.PyMongoHelper().find_one(query_json)
        if cursor:
            self.cursor = cursor
            return True
        else:
            return False



if __name__ == '__main__':
    test = Login()
    # print(test.check_accout('root'))
    # print(test.check_password('123456'))
    test.main()
