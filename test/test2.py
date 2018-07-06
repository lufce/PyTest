'''
Created on 2018/07/05

@author: shohei_desk
'''

import requests as webs

res = webs.get("http://emboj.embopress.org/content/early/2018/07/04/embj.201899264")
res.encoding = res.apparent_encoding
f1 = open("emboj_article.html", "w", encoding = "UTF-8")
# f1 = open("emboj_newarticles.html", "w", encoding = "UTF-8")
f1.write(res.text)
f1.close()
