import redis


class PyRedisHelper(object):
    def __init__(self, host='localhost', port=6379, db=0, decode_responses=True):
        self.host = host
        self.port = port
        self.db = db
        self.decode_responses = decode_responses
        # 尝试在self.pool使用单例模式
        self.pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db, decode_responses=self.decode_responses)


    def get(self, name):
        self.r = redis.Redis(connection_pool=self.pool)
        result = self.r.get(name=name)
        return result

    def setnx(self, key, value):
        self.r = redis.Redis(connection_pool=self.pool)
        result = self.r.setnx(key, value)
        return result



if __name__ == '__main__':
    test1 = PyRedisHelper()
    print(id(test1.get('foo')))
    print(id(test1.get('foo')))

    # print(test1.get('fo'))
    # print(test1.setnx('foo','bar'))
    # print(test1.setnx('root','123456'))