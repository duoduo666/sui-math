def fac(num):
    if num == 1:
        return num
    else:
        y=1
        for i in range(1,num+1):
            y *= i
        return y
def expo(num,time):
    if time == 1:
        return num
    else:
        y =num
        for i in range(1,time):
            num *= y
        return num
#常数e
def e(num=1):
    x = 0
    y = 2
    for i in range(15):
        x += (expo(num,y) / fac(y))
        y += 1
    return 1 + num + x

#常数pi
def pi(num=1,w='m'):
    if w == 'm':
        return 3.1415926535898 * num
    if w == 'd':
        return 3.1415926535898 / num
    if w != 'm' and w != 'd':
        return "please put 'm' or 'd' in target two of pi. 'm' means mutiple and 'd' means device."
    if num <= 0:
        return "It can not be 0"
    
#真正的计算pi 用这个的脑子有点问题 有好的不用，用这个这么慢的
def bpi(darts):
    from random import random      
    from time import perf_counter            
    start=perf_counter()           
    hits = 0
    for i in range(1,darts+1):     
        x,y=random(),random()      
        dist=pow(x**2+y**2,0.5)    
        if dist <=1.0:             
            hits = hits + 1
    pi=4*(hits/darts)              
    a = "圆周率值是" + format(pi) + "      " + "运行时间:" + format(perf_counter()-start)
    b = "the number of darts is too small, it cause pi unbelieveble." + "     " + a
    if pi > 3.14:
        if pi - 3.14 > 0.1:
            return b
        else:
            return a
    if pi <= 3.14:
        if 3.14 - pi > 0.1:
            return b
        else:
            return a
    return a
