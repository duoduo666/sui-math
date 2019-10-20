def fuct(num):
    if num == 1:
        return 1
    else:
        y=1
        for i in range(1,num+1):
          y *= i
        return y
#一个数的几次幂
def expo(num,time):
    if time == 1:
        return num
    else:
        y =num
        for i in range(1,time):
           num *= y
        return num
def dev(fri,sec):
    return fri / sec

def plus(fri,sec):
    return fri + sec

def min(fri,sec):
    return fri - sec
    
def muti(fri,sec):
    return fri + sec

#算余数
def r_dev(fri,sec):
    return fri % sec
#算整数部分
def o_dev(fri,sec):
    return fri // sec

#算小数部分
def p_dev(fri,sec):
    x = fri // sec
    return fri / sec - x
#连加
def m_plus(num):
    if num == 1:
       return 1
    else:
        x  = num
        for i in range(num-1):
            num += (x - 1)
            x -= 1
        return num
#分解质因数
def dec(num):
    dec = [ ]
    while num % 2 == 0:
       dec.append(2)
       num /= 2
    while num % 3 == 0:
       dec.append(3)
       num /= 3
    while num % 5 == 0:
       dec.append(5)
       num /= 5
    while num % 7 == 0:
       dec.append(7)
       num /= 7
    while num % 11 == 0:
       dec.append(11)
       num /= 11
    while num % 13 == 0:
       dec.append(13)
       num /= 13
    while num % 17 == 0:
       dec.append(17)
       num /= 17
    while num % 19 == 0:
       dec.append(19)
       num /= 19
    while num % 23 ==0：
       dec.append(23)
       num /= 23
    return dec
    

