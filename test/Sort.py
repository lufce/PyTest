'''
Created on 2018/08/25

@author: Shohei
'''

import random, inspect, copy, math

def main():
    #ソートすべき数値配列の生成
    unsorted1 = list(range(50))
    random.shuffle(unsorted1)
    unsorted2 = list(range(50,100))
    #unsorted1.extend(unsorted2)
    
    print(unsorted1)
    print(bubble_sort(unsorted1))
    print(bubble_sort_improved(unsorted1))
    print(selection_sort(unsorted1))
    print(insertion_sort(unsorted1))
    print(insertion_sort2(unsorted1))
    print(shell_sort(unsorted1))

#ループ回数をプリントする
def loop_printer(func_name,loops):
    print("{0}: {1} loops".format(func_name, loops))

#バブルソート
#隣同士の要素の比較を最初から最後まで何度も行う
def bubble_sort(unsorted_array):

    counter = 0
    working_array = copy.deepcopy(unsorted_array)

    for i in reversed(range(len(working_array))):
        counter = counter + 1
        
        for j in range(i):
            counter = counter + 1
            
            if working_array[j] > working_array[j+1]:
                buf = working_array[j]
                working_array[j] = working_array[j+1]
                working_array[j+1] = buf
                
    loop_printer(inspect.currentframe().f_code.co_name, counter)
    
    return working_array

#改良版バブルソート
#swappedがfalseのままということはそれ以降の配列はすでにソートされていることを示す。
def bubble_sort_improved(unsorted_array):
    
    counter = 0
    working_array = copy.deepcopy(unsorted_array)

    for i in reversed(range(len(working_array))):
        counter = counter + 1
        
        swapped = False
        
        for j in range(i):
            counter = counter + 1
            
            if working_array[j] > working_array[j+1]:
                buf = working_array[j]
                working_array[j] = working_array[j+1]
                working_array[j+1] = buf
                swapped = True
                
        if swapped == False:
            break

    loop_printer(inspect.currentframe().f_code.co_name, counter)

    return working_array

#選択ソート
#最小値を探して、現在のポジションと交換
def selection_sort(unsorted_array):
    
    counter = 0
    working_array = copy.deepcopy(unsorted_array)
    
    for i in range(len(working_array)):
        counter = counter + 1
        
        #最小値の探索
        min_index = i
        
        for j in range(i+1,len(working_array)):
            counter = counter + 1
            
            if working_array[j] < working_array[min_index]:
                min_index = j

        #値の交換
        temp = working_array[i]
        working_array[i] = working_array[min_index]
        working_array[min_index] = temp

    loop_printer(inspect.currentframe().f_code.co_name, counter)

    return working_array

#挿入ソート
#insertion_valueより左側を比較していく。
def insertion_sort(unsorted_array):
    
    counter = 0
    working_array = copy.deepcopy(unsorted_array)
    
    for i in range(1, len(working_array)):
        counter = counter + 1
        
        insertion_value = working_array[i]
        insertion_index = 0
        
        for j in range(i-1, -1, -1):
            counter = counter + 1
            
            if working_array[j] > insertion_value:
                working_array[j+1] = working_array[j]
            else:
                insertion_index = j + 1
                break

        working_array[insertion_index] = insertion_value
        
    loop_printer(inspect.currentframe().f_code.co_name, counter)

    return working_array

#挿入ソート2
#insertion_valueより左側を比較していく。
def insertion_sort2(unsorted_array):
    
    counter = 0
    working_array = copy.deepcopy(unsorted_array)
    
    i = 1
    while i < len(working_array):
        counter = counter + 1
        
        insertion_value = working_array[i]
        j = i
        
        if working_array[j-1] > insertion_value:
        
            while True:
                counter = counter + 1
                    
                working_array[j] = working_array[j-1]
                j = j - 1
                    
                if j < 1 or working_array[j-1] <= insertion_value:
                    break
            
            working_array[j] = insertion_value
            
        i = i + 1
        
    loop_printer(inspect.currentframe().f_code.co_name, counter)

    return working_array

#シェルソート
#https://programming-place.net/ProgrammingPlacePlus/algorithm/sort/005.html
def shell_sort(unsorted_array):
    
    counter = 0
    working_array = copy.deepcopy(unsorted_array)
    
    #間隔を設定する
    h = 1
    while(h < len(working_array) // 9):
        h = 3 * h + 1
    
    #挿入ソートを行う
    while h > 0:
        counter = counter + 1
        
        for i in range(h, len(working_array)):
            counter = counter + 1
            
            insertion_value = working_array[i]
        
            if working_array[i-h] > insertion_value:
                j = i
                while True:
                    counter = counter + 1
                    
                    working_array[j] = working_array[j-h]
                    j = j - h
                    
                    if j < h or working_array[j-h] <= insertion_value:
                        break
                    
                working_array[j] = insertion_value
        
        h = h // 3
        
        
    loop_printer(inspect.currentframe().f_code.co_name, counter)

    return working_array


if __name__ == "__main__":
    main()