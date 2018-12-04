'''
Created on 2018/07/05

@author: shohei_desk
'''

import requests as webs
import codecs

res = webs.get("https://www.nature.com/ncb/")
res.encoding = res.apparent_encoding
f1 = open("ncb_top.html", "w", encoding = "UTF-8")
# f1 = open("emboj_newarticles.html", "w", encoding = "UTF-8")
f1.write(res.text)
f1.close()

print("end")


def test_file_read():
    #テスト用のHTMLファイルをダウンロードして読み込む
    page_path = "web_src/test_page.html"
    file = codecs.open(page_path,"r",'utf-8')
    page_text = file.read()