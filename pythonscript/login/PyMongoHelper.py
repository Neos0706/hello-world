import pymongo


class PyMongoHelper(object):
    def __init__(self, host='localhost', port=27017):
        self.host = host
        self.port = port
        try:
            self.client = pymongo.MongoClient(host=self.host, port=self.port)
            self.db = self.client.python3
            self.collection = self.db.user
        except Exception as e:
            print(f'{__name__} Mongo connect error: {e}')
        else:
            print(f'{__name__} Mongo connect success' )

    def insert_one(self, one_json:dict) ->None:
        try:
            result = self.collection.insert_one(one_json)
        except Exception as e:
            print(e)
            
    def insert_many(self, json_list: list):
        try:
            result = self.collection.insert_one(json_list)
            print(result)
        except Exception as e:
            print(e)

    def find_one(self, one_json=None):
        try:
            result_cursor = self.collection.find(one_json)
            # 把cusror转化为list 存起来，不然用完就没了
            result_list = list(result_cursor)
            # print(type(result_list[0]))
            # print(dir(result))
        except Exception as e:
            print(e)
        return result_list[0] if len(result_list) > 0 else None

    def find_all(self, one_json=None):
        try:
            result_cursor = self.collection.find()
            result_list = list(result_cursor)
        except Exception as e:
            print(e)
        # print(result[0])
        return result_list if len(result_list) > 0 else None


            
        
    
            




if __name__ == '__main__':
    test = PyMongoHelper()
    # test.insert_one({"name":"guoqi","sex":"male","age":26})
    query_json = {'account': 'root'}
    # print(type(query_json))
    print(test.find_one(query_json))

        