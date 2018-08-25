'''
Created on 2018/08/25

@author: Shohei
'''

import random, inspect, copy

def main():
    #ソートすべき数値配列の生成
    unsorted1 = list(range(50))
    unsorted2 = list(range(50,100))
    random.shuffle(unsorted1)
    unsorted1.extend(unsorted2)
    
    bubble_sort(unsorted2)
    bubble_sort_improved(unsorted2)

#ループ回数をプリントする
def loop_printer(func_name,loops):
    print("{0}: {1} loops".format(func_name, loops))

#バブルソート
def bubble_sort(unsorted_array):

    counter = 0
    working_array = copy.deepcopy(unsorted_array)

    for i in reversed(range(len(working_array)-1)):
        
        counter = counter + 1
        
        for j in range(i):
            if working_array[j] > working_array[j+1]:
                buf = working_array[j]
                working_array[j] = working_array[j+1]
                working_array[j+1] = buf
                
                counter = counter + 1
                
    loop_printer(inspect.currentframe().f_code.co_name, counter)
    
    return working_array

#改良版バブルソート
#swappedがfalseのままということはそれ以降の配列はすでにソートされていることを示す。
def bubble_sort_improved(unsorted_array):
    
    counter = 0
    working_array = copy.deepcopy(unsorted_array)

    for i in reversed(range(len(working_array)-1)):
        swapped = False
        counter = counter + 1
        
        for j in range(i):
            if working_array[j] > working_array[j+1]:
                buf = working_array[j]
                working_array[j] = working_array[j+1]
                working_array[j+1] = buf
                swapped = True
                
                counter = counter + 1
                
        if swapped == False:
            break

    loop_printer(inspect.currentframe().f_code.co_name, counter)

    return working_array

if __name__ == "__main__":
    main()