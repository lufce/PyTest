'''
Created on 2018/07/05

@author: shohei_desk
'''

import requests as webs

res = webs.get("https://www.cell.com/cell/fulltext/S0092-8674(18)30713-X")
res.encoding = res.apparent_encoding
f1 = open("cell_article2.html", "w", encoding = "UTF-8")
f1.write(res.text)
f1.close()
