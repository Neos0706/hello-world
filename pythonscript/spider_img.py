import os
import re
import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup


url = "https://www.qqtn.com/tx/nanshengtx_1.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
base_url = "https://www.qqtn.com"
file = "/Users/admin/facedata/img_download_qqan"


def get_imgs(url):
    response = requests.get(url, headers=headers)
    response.encoding = "gb2312"
    html = response.text
    # print(html)
    imgs_urls = re.findall(f'<a href="(.*?)" target="_blank" title=".*?"', html)
    for imgs_url in imgs_urls:
        full_url = base_url + imgs_url
        print(full_url)
        imgs_response = requests.get(full_url, headers=headers)
        imgs_response.encoding = "gb2312"
        imgs_response_html = imgs_response.text
        node_html = imgs_response_html
        # print(node_html)
        img_urls = re.findall(f'<img src="(.*?)"/></p', node_html)
        time.sleep(0.5)
        for img_url in img_urls:
            img_name = img_url.split('/')[-1]
            img_response = requests.get(img_url, headers=headers)
            with open(file+'/'+img_name, 'wb') as f:
                f.write(img_response.content)
            print(img_url)
            time.sleep(0.5)
    next_page = re.findall(f'更多.*<a href="(.*?)" class="tsp_next"><i>下一页', html)
    time.sleep(1.5)
    if next_page:
        print(next_page)
        get_imgs(base_url+next_page[0])
    else:
        print("爬取完毕")






    # driver = webdriver.Chrome()
    # driver.get(url)
    # driver.implicitly_wait(10)
    # ul = driver.find_elements_by_xpath('''//body/div[@class="g-gxlist-box g-box-1200 m-margin15 clearfix"]/div[1]/ul/li''')
    # for li in ul:
    #     li.click()
    #     # img = driver.find_elements_by_class_name("m_qmview")
    #     img = driver.find_elements_by_xpath('//*[@id="content"]/p[1]/a/li/img')
    #     # img = driver.find_element_by_xpath('//*[@id="content"]/p[1]/a/li/img')
    #     print(img)
        # print(li)
    # content = driver.page_source
    # soup = BeautifulSoup(content, "html.parser")
    # for li in soup.find_all("li", )


if __name__ == '__main__':
    url = "https://www.qqtn.com/tx/nanshengtx_1.html"
    get_imgs(url)