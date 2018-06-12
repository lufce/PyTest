'''
Created on 2018/06/12

@author: Shohei
'''

is_cont=True

while is_cont:
    print('press any key')
    c = input()
    
    if c == 'end':
        is_cont=False
    else:
        print('You pressed '+c)