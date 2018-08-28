'''
Created on 2018/08/25

@author: Shohei
'''

import random, inspect, copy, time

def main():
    #ソートすべき数値配列の生成
    unsorted1 = list(range(1000))
    random.shuffle(unsorted1)
    unsorted2 = list(range(50,100))
    unsorted3 = [3,3,2,2,1,1]
    #unsorted1.extend(unsorted2)
    
    tested_array = copy.deepcopy(unsorted1)

    print(tested_array)
    
#     print(bubble_sort(tested_array))
#     print(bubble_sort_improved(tested_array))
#     print(selection_sort(tested_array))
#     print(insertion_sort(tested_array))
#     print(insertion_sort2(tested_array))
#     print(shell_sort(tested_array))
#     print(merge_sort(tested_array))
    
    
    bubble_sort(tested_array)
    bubble_sort_improved(tested_array)
    selection_sort(tested_array)
    insertion_sort(tested_array)
    insertion_sort2(tested_array)
    shell_sort(tested_array)
    merge_sort(tested_array)
    
    print("end")

#ループ回数と所要時間をプリントする
def loop_printer(func_name, loops, runtime):
    print("{0}: {1} loops: {2} sec.".format(func_name, loops, runtime))

#バブルソート
#隣同士の要素の比較を最初から最後まで何度も行う
def bubble_sort(unsorted_array):
    t1 = time.time()
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
                
    t2 = time.time()
    loop_printer(inspect.currentframe().f_code.co_name, counter, t2 - t1)
    
    return working_array

#改良版バブルソート
#swappedがfalseのままということはそれ以降の配列はすでにソートされていることを示す。
def bubble_sort_improved(unsorted_array):
    t1 = time.time()
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

    t2 = time.time()
    loop_printer(inspect.currentframe().f_code.co_name, counter, t2 - t1)

    return working_array

#選択ソート
#最小値を探して、現在のポジションと交換
def selection_sort(unsorted_array):
    t1 = time.time()
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
    
    t2 = time.time()
    loop_printer(inspect.currentframe().f_code.co_name, counter, t2 - t1)

    return working_array

#挿入ソート
#insertion_valueより左側を比較していく。
def insertion_sort(unsorted_array):
    t1 = time.time()
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
    
    t2 = time.time()    
    loop_printer(inspect.currentframe().f_code.co_name, counter, t2 - t1)

    return working_array

#挿入ソート2
#insertion_valueより左側を比較していく。
def insertion_sort2(unsorted_array):
    t1 = time.time()
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
    
    t2 = time.time()    
    loop_printer(inspect.currentframe().f_code.co_name, counter, t2 - t1)

    return working_array

#シェルソート
#https://programming-place.net/ProgrammingPlacePlus/algorithm/sort/005.html
def shell_sort(unsorted_array):
    t1 = time.time()
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
        
    t2 = time.time()    
    loop_printer(inspect.currentframe().f_code.co_name, counter, t2 - t1)

    return working_array

#マージソート
#配列を2つに分割していって、その後2つのソートされた配列から先頭の要素を比較して小さい方から取り出して新しい配列を作り出す。
def merge_sort(unsorted_array):
    t1 = time.time()
    #カウンターを普通に使おうとすると、int型がイミュータブルである影響で再帰中に加算されたものが反映されない。そこでわざとミュータブルなリストにしている。
    counter = [0]
    working_array = copy.deepcopy(unsorted_array)
    
    split_process(working_array, counter)

    t2 = time.time()
    loop_printer(inspect.currentframe().f_code.co_name, counter[0], t2 - t1)

    return working_array

def split_process(main_array, counter):
    
    #分割操作
    if(len(main_array) > 1):
        counter[0] = counter[0] + 1
        
        m = len(main_array) // 2
        
        a1 = main_array[:m]
        a2 = main_array[m:]
        
        split_process(a1, counter)
        split_process(a2, counter)
        merge_process(a1, a2, main_array, counter)
        
def merge_process(array1, array2, merged_array, counter):
    i = 0
    j = 0
    
    while(i < len(array1) or j < len(array2)):
        #どちらかの配列の要素がまだ残っているとき
        counter[0] = counter[0] + 1
        
        if(j >= len(array2) or (i < len(array1) and array1[i] <= array2[j])):
            #array2の要素を使い切った場合、または
            #array1とarray2の両方の要素が残っていて、array1のほうが小さい場合は
            #array1の要素をmerged_arrayの最後尾に追加する。
            
            merged_array[i+j] = array1[i]
            i = i + 1
        
        else:
            merged_array[i+j] = array2[j]
            j = j + 1
        
#ヒープソート
#まずはヒープの実装

class MyHeap:
    '''
    ヒープソートのためにヒープ構造を実装してみる。 
    データはself.array[1]から入れていく。1スタートの構造。    
    根には最小値がくる
    '''
    
    
    def __init__(self, arr):
        self.capcity = len(arr)*2
        self.count = len(arr)
        self.array = [0] * self.capacity
        
    def parent(self, now):
        if(now < 1 or now > self.count):
            #now_pointがarrayのindexを超えている場合
            return None
        else:
            #根でも0が返される。
            return now // 2
    
    def right_child(self, now):
        right = now * 2
        if(now < 1 or now > self.count):
            #now_pointがarrayのindexを超えている場合
            return None
        if(right > self.count):
            #子がいないなら
            return None
        return right
    
    def left_child(self, now):
        left = now * 2 + 1
        if(now < 1 or now > self.count):
            #now_pointがarrayのindexを超えている場合
            return None
        if(left > self.count):
            #子がいないなら
            return None
        return left
    
    def sibling(self, now):
        if(now < 1 or now > self.count):
            #now_pointがarrayのindexを超えている場合
            return None
        if(now % 2 == 0):
            return now + 1
        else:
            #根でも0が返される
            return now - 1
    
    def getMinimum(self):
        if(self.count == 0):
            return None
        else:
            return self.array[1]

if __name__ == "__main__":
    main()