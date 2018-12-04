'''
Created on 2018/12/04

@author: Shohei
'''

a1 = ["a ","b ","c "]
a2 = ["d ","e ","f "]
a3 = []
a3.append(a1)
a3.append(a2)
print(a1)
print(a2)
print(a3)
b1 = []
b2 = []
for n in a3:
    for m in n:
        b1.append(m.strip())
    
    b2.append(b1)
    b1 = []

print(a3)
print(b2)