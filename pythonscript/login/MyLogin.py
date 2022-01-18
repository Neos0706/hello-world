import hashlib
import hmac
import PyMySQLHelper
import PyRedisHelper



"""实现模拟登录
1.0.0 算法：
    用户输入username 和password
        判断 username 是否在redis中 ？如何选择账号密码在redis中的存贮结构
            如果在，判断password
            如果不在，判断username是否在mysql中：
                在，验证密码
                    密码正确
                不在,返回账号不存在
                

1 为了节省内存，先创建redis链接对象，查询不到，再使用mysql
     
"""

class Login(object):


    def main(self):
        account = input("please input your account")
        password = input("please input your password")
        redis_ret = self.check_accout_redis(account)
        hash_password = hashlib.sha256(password.encode()).hexdigest()
        # 先从
        if not redis_ret:
            mysql_ret = self.check_accout_mysql(account)
            if not mysql_ret:
                print('账号不存在')
            else:
                if mysql_ret[2] == hash_password:
                    #从mysql 把数据添加到redis
                    self.redis.setnx(account, hash_password)
                    print('登录成功')
                else:
                    print('密码错误')
        else:
            if redis_ret == hash_password:
                print('登录成功')
            else:
                print('密码错误')


    # 不需要再次查询密码
    # def check_password_mysql(self,account:str,password:str)-> bool:
    #     sql = f"select password from user where account = '{account}'"
    #     sqlpassword = self.mysql.query_one(sql)[0]
    #     hash_password = hashlib.sha256(password.encode()).hexdigest()
    #     if hash_password == sqlpassword:
    #         return True
    #     else:
    #         return False


    def check_accout_mysql(self, account: str) -> bool:
        # 需要加上引号
        sql = f"select * from user where account = '{account}'"
        self.mysql = PyMySQLHelper.PyMySQLHelper()
        mysql_ret = self.mysql.query_one(sql)
        return mysql_ret

    def check_accout_redis(self, account: str) ->bool:
        self.redis = PyRedisHelper.PyRedisHelper()
        redis_ret = self.redis.get(account)
        return redis_ret



if __name__ == '__main__':
    test = Login()
    # account = 'roots'
    # # test.check_password('root', '123456')
    # # print(test.check_accout_redis(account))
    # print()
    test.main()
