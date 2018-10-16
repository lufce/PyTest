'''
Created on 2018/08/28

@author: Shohei
'''

def main():
    number = 10
    
    print(r_kaijo(number))
    print(l_kaijo(number))
    

def r_kaijo(n):
    if(n==1):
        return 1
    else:
        return n*r_kaijo(n-1)
    
def l_kaijo(n):
    ans = 1
    i = 1
    while(i <= n):
        ans = ans * i
        i = i + 1
    
    return ans

if __name__ == "__main__":
    main()