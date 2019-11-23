#阶乘（完美阶乘 10位数搓搓有余） 建议使用这个
def fac(num):
    if num == 1:
        return num
    else:
        y=1
        for i in range(1,num+1):
            y *= i
        return y
    

#阶乘(最高到10000 10000以上无法算出)
def fuc(num):
    if num ==1:
        return 1
    return num * fuc(num - 1)

#一个数的几次幂
def expo(num,time):
    if time == 1:
        return num
    else:
        y =num
        for i in range(1,time):
            num *= y
        return num
#余数
def rdev(fri,sec):
    return fri %sec
#算整数部分
def odev(fri,sec):
    return fri // sec
#算小数部分
def pdev(fri,sec):
    return fri / sec - fri // sec
#连加
def mplus(num):
    x  = num
    for i in range(num-1):
        num += (x - 1)
        x -= 1
    return num
    
#从角度换弧度
def charc(angle):
    return angle * pi / 180

#从弧度换角度
def chang(arc):
    return arc * 180 / pi

#绝对值
def abso(num):
    if num < 0:
        return num - num - num
    elif num >= 0:
        return num

#分解质因数
def dec(num):
    dec = []
    x = 3
    while num % 2 == 0:
        dec.append(2)
        num /= 2
    while num >= x:
        while num % x == 0:
            dec.append(x)
            num /= x
        x += 2
    return dec

#最小公倍数
def lcm(num1,num2):
    x = 2
    lc = []
    while num1 >= x and num2 >= x:
        while num1 % x == 0 and num2 % x == 0:
            lc.append(x)
            num1 /= x
            num2 /= x
        x += 1
    lc.append(num1)
    lc.append(num2)
    y = 1
    for i in lc:
        y *= i
    return y
    
#最大公因数
def mcf(num1,num2):
    mc = []
    x = 2
    while num1 >= x and num2 >= x:
        while num1 % x == 0 and num2 % x == 0:
            mc.append(x)
            num1 /= x
            num2 /= x
        x += 1
    y = 1
    for i in mc:
        y *= i
    return y

#对数
#ln
def ln(num):
    if num > 0 and num != 1 and num <= 100:
        a = (num - 1) / (num + 1)
        x = 0
        for i in range(3,1001,2):
            x += (expo(a,i) / i)
        return 2 * (x + a)
    elif num == 1:
        return 0
    elif num <= 0:
        return "are you kidding me? the number you type in LN is smaller than 1!"
    if num > 100:
        return "the number you type in Ln is very big. please try 'bln' instead. \n But it might be slowly"

def bln(num):
    if num > 100 and num < 10000:
        a = (num - 1) / (num + 1)
        x = 0
        for i in range(3,10001,2):
            x += (expo(a,i) / i)
        return 2 * (x + a)
    elif num != 1 and num <= 100:
        a = (num - 1) / (num + 1)
        x = 0
        for i in range(3,1001,2):
            x += (expo(a,i) / i)
        return 2 * (x + a)
    elif num == 1:
        return 0
    elif num < 0:
        return "are you kidding me? the number you type in LN is smaller than 1!"
    elif num >= 10000:
        a = (num - 1) / (num + 1)
        x = 0
        for i in range(3,50001,2):
            x += (expo(a,i) / i)
        return 2 * (x + a)

