# coding = uft-8
import random

"""
 bug 1 同一strname 的对象会重复生成，利于节省内存
 
 question 1 创建类时，什么变量声明为对象属性？
"""


class Person(object):
    """
    最小的类,
    """

    def __init__(self, name):
        self.name = name
        self.money = 0

    def __str__(self):
        return f"{self.name}: {self.money}"


class ALL(object):
    """

    """
    def __init__(self, name_list=None):
        self.persons = self.get_persons(name_list)
        self.num = len(self.persons)
        self.persons_info = []
        # 保存所有组的列表
        self.groups = []
        # 用于资金流动统计
        # 盈利组
        self.profit = []
        # 亏损组
        self.loss = []

    def __str__(self):
        return str([{i.name: i.money} for i in self.persons])

    # 创建person对象
    def get_persons(self, name_list):
        """
        用于初始化总人数
        :param name_list: 用户传入的list[str]
        :return: list[person]
        """
        if name_list is None:
            name_list = ['温柔', '老仇', '李永', '马区', '小葵', '阿发', '夏法', '陈亮']
            persons = []
            for i in range(len(name_list)):
                persons.append(Person(name_list[i]))
            return persons
        elif isinstance(name_list[0], str):
            persons = []
            for i in range(len(name_list)):
                persons.append(Person(name_list[i]))
            return persons
        elif isinstance(name_list[0], Person):
            return name_list

    # 分组
    def divide_gruop(self, n=2):
        """

        :param n: ALL分的gruop 数
        :return: 含有组的组列表
        """
        if self.num % n != 0:
            raise ValueError(f'总人数{self.num}不能分成{n}组')
        # 支持多轮分组
        self.groups = []

        # 保存gruop 对象
        random_index = [x for x in range(self.num)]
        for i in range(n):
            temp = []
            for _ in range(self.num // n):
                index = random.choice(random_index)
                temp.append(self.persons[index])
                random_index.remove(index)
            # groupname = 'group' + str(i)
            self.groups.append(Group(temp))
        return self.groups

    # 获取info信息，并更新
    def get_persons_info(self):
        persons_info = []
        self.profit = []
        self.loss = []
        for i in self.persons:
            if i.money > 0:
                self.profit.append(i)
            elif i.money < 0:
                self.loss.append(i)
            persons_info.append({i.name: i.money})
        return persons_info

    # pk结束进行结算，先按两队结算
    def settlement(self, winner=True):
        """

        :param winner: 确定哪组胜利
        :return:
        """
        if self.groups is []:
            raise ValueError('还未分组，不能结算')
        if winner:
            self.groups[0].change_money(True, 100)
            self.groups[1].change_money(False, 100)
            self.persons_info = self.get_persons_info()

        else:
            self.groups[0].change_money(True, 100)
            self.groups[1].change_money(False, 100)
            self.persons_info = self.get_persons_info()

    # 输出资金流动
    def flow_money(self):
        """
        垃圾逻辑，等有一天重写
        :return:
        """
        flow_info = ''
        # 要对对象属性进行操作，防止改变对象属性，先赋值出来
        # 选择二位列表，不需要查询
        profit_list = [[x.name, x.money] for x in self.profit]
        loss_list = [[x.name, x.money] for x in self.loss]

        while len(profit_list) > 0:
            temp = ''
            while profit_list[0][1] != 0:
                while loss_list[0][1] != 0:
                    # 配对时，某人赢得钱和另一人输的钱一样多：
                    if profit_list[0][1] + loss_list[0][1] == 0:
                        temp += f"{loss_list[0][0]} give {profit_list[0][0]} {profit_list[0][1]}\n"
                        profit_list[0][1] = 0
                        loss_list[0][1] = 0
                    # 配对时，某人赢得钱比另一个人输的钱多，继续匹配
                    elif profit_list[0][1] + loss_list[0][1] > 0:
                        temp += f"{loss_list[0][0]} give {profit_list[0][0]} {abs(loss_list[0][1])}\n"
                        profit_list[0][1] = profit_list[0][1] + loss_list[0][1]
                        loss_list[0][1] = 0
                    # 配对时，某人赢得钱比另一个人输的钱少，继续匹配
                    elif profit_list[0][1] + loss_list[0][1] < 0:
                        temp += f"{loss_list[0][0]} give {profit_list[0][0]} {profit_list[0][1]}\n"
                        loss_list[0][1] = profit_list[0][1] + loss_list[0][1]
                        profit_list[0][1] = 0
                    if loss_list[0][1] == 0:
                        del loss_list[0]
                        break
                    # profit_list[0][1] 为0，loss_list[0][1]不为0时及时跳出
                    if profit_list[0][1] == 0:
                        break
                if profit_list[0][1] == 0:
                    del profit_list[0]
                    break
            flow_info += temp

        return flow_info


class Group(ALL):
    def change_money(self, result, value=100):
        # 每次资金变化时，实施更新盈利和亏损组
        self.profit = []
        self.loss = []
        if result:
            for i in self.persons:
                # print(i, id(i))
                i.money += value
                # print(i, id(i))
        else:
            for i in self.persons:
                i.money -= value


def main():
    pass


if __name__ == '__main__':
    test = ALL()
    # # test1 测试ALL初始化
    # print("test1", test)
    # # test2 测试分组
    # # for i in range(10):
    # #     gruops = test.divide_gruop()
    # #     print("test2", i, gruops)
    # #     for j in gruops:
    # #         print('*******test2', j)
    # test2.1 单次分组 检验对象是否是同一对象，还是新建的对象
    # for x in test.persons:
    #     print(x,id(x))
    # # 分组前的对象
    # print("分组前的对象*****************")
    # gruops = test.divide_gruop()
    # for j in gruops:
    #     # print(id(j))
    #     for i in j.persons:
    #         print(i, id(i))
    #         # print(type(i))
    #     # print('*******test2.1', j)
    # for x in test.persons:
    #     print(x,id(x))
    # # test3 测试结算
    # gruops = test.divide_gruop()
    # test.settlement()
    # gruops = test.divide_gruop()
    # test.settlement()
    # print(type(test.persons))
    # for j in gruops:
    #     print(j)
    #     for i in j.persons:
    #         print(i)
    # for i in test.persons:
    #     print(i)
    # print(test.persons_info)
    # print(test.profit)
    # for i in test.profit:
    #     print(i)
    # print(test.loss)
    # print(test.flow_money())
    # test4 测试盈利组和亏损组

    # test5 多轮分组比赛后，测试资金流动
    random_num = random.randint(1, 11)
    print(random_num)
    for i in range(random_num):
        test.divide_gruop(2)
        test.settlement()
    print(test.persons_info)
    print("profit", [[i.name, i.money] for i in test.profit])
    print("loss", [[i.name, i.money] for i in test.loss])
    print(test.flow_money())
