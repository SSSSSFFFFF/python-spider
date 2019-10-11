# -*- coding: utf-8 -*-
'''
爬知乎
'''
import requests

def Spider():
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    url = "https://www.zhihu.com/"
    myPage = requests.get(url,headers=headers).text
    print(myPage)

if __name__ == '__main__':
    print ("start")
    Spider()
    print ("end")