'''
Created on 2018/06/12

@author: Shohei
'''

def genet():
    yield 'あ'
    yield 'い'
    yield 'う'

obj = genet();

text = obj.__next__()
print(text)
text = obj.__next__()
print(text)
text = obj.__next__()
print(text)
text = obj.__next__()
print(text)