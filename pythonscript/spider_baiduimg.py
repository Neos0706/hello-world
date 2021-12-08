import os
import re
import sys
import time
import json
import requests
import getpass
import threading
import ast

base_url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word="

"""
1 搜索图片
2 获取图片url
3 下载图片

如何对图片进行去重？
建立log
以json的格式存储url
下载前判断是否在log中，没有就下载，把url存在log中
目前遇到的问题

设想 ：给程序加上logging分级信息

"""


class BaiduSpider(object):

    def __init__(self, keyword, savepath=None, cur_target=100):
        # self.base_url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word="
        # self.base_url = "https://image.baidu.com/user/logininfo?src=pc&page=searchresult&time=1631518912636"
        self.base_url = "https://image.baidu.com/search/acjson?"
        self.keyword = keyword
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            # "Accept": "application / json, text / javascript, * / *; q = 0.01",
            # "Accept-Encoding": "gzip, deflate, br",
            # "Host": "image.baidu.com",
            # "Referer": "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=1",
        }
        self.cur_target = cur_target
        self.params = {
            'tn': 'resultjson_com',
            'logid': '10069732654425565224',
            'ipn': 'rj',
            'ct': '201326592',
            'is': ' ',
            'fp': 'result',
            'queryWord': f'{self.keyword}',
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': ' ',
            'st': '-1',
            'z': '',
            'ic': '0',
            'hd': '',
            'latest': '',
            'copyright': '',
            'word': f'{self.keyword}',
            's': ' ',
            'se': ' ',
            'tab': ' ',
            'width': ' ',
            'height': ' ',
            'face': ' 0',
            'istype': ' 2',
            'qc': ' ',
            'nc': ' 1',
            'fr': ' ',
            'expermode': ' ',
            'nojc': ' ',
            # 已经请求到的数量,以30为步长
            'pn': '30',
            # 每页的显示个数 最大值为60
            'rn': ' 30',
            'gsm': ' 1e',
            '1631520201265': ' ',
        }
        if savepath:
            self.savepath = savepath
        else:
            self.savepath = f'/Users/{getpass.getuser()}/Downloads/{self.keyword}'
        self.info_dict = self._mkdirandjson()
        print(type(self.info_dict["fromURLHost"]), self.info_dict["fromURLHost"])

        self.info_dict["fromURLHost"] = ast.literal_eval(str(self.info_dict["fromURLHost"]))

        # self.info_dict["fromURLHost"] = ast.literal_eval(self.info_dict["fromURLHost"])

        # print(type(self.info_dict), self.info_dict)
        # print(type(eval(self.info_dict["fromURLHost"])), self.info_dict["fromURLHost"])


        # 本次爬取所需要的页数

    def get_page(self, pages):
        params = {
            'tn': 'resultjson_com',
            'logid': '10069732654425565224',
            'ipn': 'rj',
            'ct': '201326592',
            'is': ' ',
            'fp': 'result',
            'queryWord': f'{self.keyword}',
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': ' ',
            'st': '-1',
            'z': '',
            'ic': '0',
            'hd': '',
            'latest': '',
            'copyright': '',
            'word': f'{self.keyword}',
            's': ' ',
            'se': ' ',
            'tab': ' ',
            'width': ' ',
            'height': ' ',
            'face': ' 0',
            'istype': ' 2',
            'qc': ' ',
            'nc': ' 1',
            'fr': ' ',
            'expermode': ' ',
            'nojc': ' ',
            # 已经请求到的数量,以30为步长
            'pn': f'{pages * 30}',
            # 每页的显示个数 最大值为60
            'rn': ' 30',
            'gsm': ' 1e',
            '1631520201265': ' ',
        }
        return params

    # 逻辑非常混乱
    # 创建
    def _mkdirandjson(self):
        if not os.path.exists(self.savepath):
            os.mkdir(self.savepath)
        if os.path.exists(os.path.join(self.savepath, "download_" + self.keyword + ".json")):
            with open(os.path.join(self.savepath, "download_" + self.keyword + ".json"), "r") as f:
                info_dict = json.load(f, strict=False)
            return info_dict

        else:
        # 新建json文件
            info_dict = {
                "keyword": self.keyword,
                "savepath": self.savepath,
                # 已下载的图片数量
                "downloaded": 0,
                # 图片重复未下载的数量，本爬虫可以去重
                "repeat_undwnloaded":0,
                #上次请求的page
                "last_page":0,
                "fromURLHost": {}

            }
        with open(os.path.join(self.savepath, "download_" + self.keyword + ".json"), "w") as f:
            f.write(json.dumps(info_dict, indent=4, ensure_ascii=False))
        return info_dict


    # 获取目标pages的页面
    def get_html(self, param=None):
        # response = requests.get(self.base_url+self.keyword, headers=self.headers)
        i = 1
        while i < 6:
            try:
                response = requests.get(self.base_url, headers=self.headers, params=param, timeout=2 + i * 3)
                # if response.raise_for_status() == 200:
                print(type(response))
                return response
            except requests.exceptions.RequestException as e:
                print(f"获取页面{self.base_url}时，第{i}次失败  \n 原因为{e}")
                i += 1
        return False

    def engine(self):
        download_count = 0
        undownload_count = 0
        for i in range(1000):
            if download_count >= self.cur_target:
                print(f"本次爬取{self.keyword}类行图片{download_count}张，已存放在{self.savepath}文件夹下,成功去重{undownload_count}张")
                self.info_dict['downloaded'] += download_count
                self.info_dict['repeat_undwnloaded'] += undownload_count
                self.info_dict['last_page'] += i
                self.info_dict['fromURLHost'] = str(self.info_dict['fromURLHost'])
                with open(os.path.join(self.savepath, "download_" + self.keyword + ".json"), "w") as f:
                    f.write(json.dumps(self.info_dict, indent=4, ensure_ascii=False))
                break
            else:

                cur_param = self.get_page(i)
                # 有一个含"\"的json解析错误
                try:
                    res = self.get_html(cur_param).json()
                except json.decoder.JSONDecodeError:
                    print(res)
                for j in range(len(res["data"]) - 1):
                    get_img_res =self.get_img(res, j)
                    if get_img_res:
                        download_count += 1
                    else:
                        undownload_count += 1

    def get_img(self, res, j):
        # for j in range(len(res["data"])-1):
        # 根据fromURLHost和shituToken来做判断是否是重复图片
        # 实测有效
        if res["data"][j]["fromURLHost"] not in self.info_dict["fromURLHost"]:
            # 设置为集合查询更快
            self.info_dict["fromURLHost"].setdefault(res["data"][j]["fromURLHost"], set())
        if res["data"][j]['shituToken'] not in self.info_dict["fromURLHost"][res["data"][j]["fromURLHost"]]:
            url = BaiduSpider.baidu_uncomplie(res["data"][j]["objURL"])
            self.download_imgs(url)
            self.info_dict["fromURLHost"][res["data"][j]["fromURLHost"]].add(res["data"][j]["shituToken"])
            print(self.info_dict)
            return True

        else:
            # url = BaiduSpider.baidu_uncomplie(res["data"][j]["objURL"])
            # self.download_imgs(url)
            print(f'{res["data"][j]["fromURLHost"]}的图片有重复嫌疑，未下载，shituToken:{res["data"][j]["shituToken"]}')
            return False

    def download_imgs(self, url):
        imgname = self.keyword + "_" + time.strftime("%Y%m%d%H%M%S", time.localtime()) + str(time.time())[-4:-1] + ".jpg"
        res = requests.get(url)
        imgpath = os.path.join(self.savepath, imgname)
        with open(imgpath, "wb") as f:
            f.write(res.content)
        print(f"正在下载图片{imgpath}")
        # time.sleep(1)

    # 解密baidu的objURL(原图)，thumbURL不是原图，我们只要原图
    @classmethod
    def baidu_uncomplie(cls, url):
        res = ''
        c = ['_z2C$q', '_z&e3B', 'AzdH3F']
        d = {'w': 'a', 'k': 'b', 'v': 'c', '1': 'd', 'j': 'e', 'u': 'f', '2': 'g', 'i': 'h', 't': 'i', '3': 'j',
             'h': 'k', 's': 'l', '4': 'm', 'g': 'n', '5': 'o', 'r': 'p', 'q': 'q', '6': 'r', 'f': 's', 'p': 't',
             '7': 'u', 'e': 'v', 'o': 'w', '8': '1', 'd': '2', 'n': '3', '9': '4', 'c': '5', 'm': '6', '0': '7',
             'b': '8', 'l': '9', 'a': '0', '_z2C$q': ':', '_z&e3B': '.', 'AzdH3F': '/'}
        if url is None or 'http' in url:
            return url
        else:
            j = url
            for m in c:
                j = j.replace(m, d[m])
            for char in j:
                if re.match(r'^[a-w\d]+$', char):
                    char = d[char]
                res = res + char
            return res


if __name__ == '__main__':
    test = BaiduSpider("两个黑人", cur_target=300)
    test.engine()
    # print(test.get_html(test.params).json())
    # test.download_imgs()
    # img = requests.get("https://img0.baidu.com/it/u=3299185958,3315182329&fm=26&fmt=auto")
    # print(img.content)
    # with open("/Users/admin/Downloads/111.jpg", "wb") as f1:
    #     f1.write(img.content)
    # url = 'ippr_z2C$qAzdH3FAzdH3F1y_z&e3B8mn_z&e3Bv54AzdH3Fw6ptvsjAzdH3FGbGOVSBIacnnRNEG_z&e3Bip4s'
    #
    # uncomplie_url=BaiduSpider.baidu_uncomplie(url)
    # print(uncomplie_url)
