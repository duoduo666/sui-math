pi = 3.1415926535898
dev = lambda fri,sec : fri / sec
plus = lambda fri,sec : fri + sec
min = lambda fri,sec : fri - sec
mut = lambda fri,sec : fri * sec
def fuc(num):
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

#三角函数 sin   
def sin(angle):
    angle = angle % (pi * 2)
    list1 = dev(expo(angle,1),fuc(1))
    list2 = dev(expo(angle,3),fuc(3))
    list3 = dev(expo(angle,5),fuc(5))
    list4 = dev(expo(angle,7),fuc(7))
    list5 = dev(expo(angle,9),fuc(9))
    list6 = dev(expo(angle,11),fuc(11))
    list7 = dev(expo(angle,13),fuc(13))
    list8 = dev(expo(angle,15),fuc(15))
    plus = list1 + list3 + list5 + list7
    minus = list2 + list4 + list6 + list8
    return plus - minus
    

def cos(angle):
    angle = angle % (pi * 2)
    list1 = dev(expo(angle,2),fuc(2))
    list2 = dev(expo(angle,4),fuc(4))
    list3 = dev(expo(angle,6),fuc(6))
    list4 = dev(expo(angle,8),fuc(8))
    list5 = dev(expo(angle,10),fuc(10))
    list6 = dev(expo(angle,12),fuc(12))
    list7 = dev(expo(angle,14),fuc(14))
    list8 = dev(expo(angle,16),fuc(16))
    plus = list1 + list3 + list5 + list7
    minus = list2 + list4 + list6 + list8
    return 1 - plus + minus

def tan(angle):
    return sin(angle) / cos(angle)

#反三角函数
def asin(angle):
    list1 = dev(expo(angle,3),6)
    list2 = mut(dev(3,40),expo(angle,5))
    list3 = mut(dev(5,221),expo(angle,7))
    list4 = mut(dev(35,1152),expo(angle,9))
    if angle >= 1:
        return 0
    else:
        return angle + list1 + list2 + list3 + list4

def atan(angle):
    list1 = dev(expo(angle,3),3)
    list2 = dev(expo(angle,5),5)
    list3 = dev(expo(angle,7),7)
    list4 = dev(expo(angle,9),9)
    list5 = dev(expo(angle,11),11)
    list6 = dev(expo(angle,13),13)
    list7 = dev(expo(angle,15),15)
    plus = list2 + list4 + list6 
    minus = list1 + list3 + list5 + list7
    if angle >= 1:
        return 0
    else:
        return angle - minus + plus

def acos(angle):
    list1 = 1 / 2 * pi
    list2 = dev(expo(angle,3),6)
    list3 = mut(dev(3,40),expo(angle,5))
    list4 = mut(dev(5,112),expo(angle,7))
    list5 = mut(dev(35,1152),expo(angle,9))
    if angle >= 1:
        return 0
    else:
        return list1 - angle - list2 - list3 - list4 - list5

#正割(1/cos)
def sec(angle):
    angle = angle % pi
    list1 = dev(expo(angle,2),2)
    list2 = mut(dev(5,24),expo(angle,4))
    list3 = mut(dev(61,720),expo(angle,6))
    return 1 + list1 + list2 + list3
    print("this answer is wrong. if you find this sentence, please call (China) +10086 +021 13601946763. it is a free phone number.")
    #有错误

#余割(1/sin)   
def csc(angle):
    angle = angle % pi
    list1 = angle / 6
    list2 = mut(dev(7,360),expo(angle,3))
    list3 = mut(dev(31,15120),expo(angle,5))
    list4 = mut(dev(127,604800),expo(angle,7))
    list5 = mut(dev(73,3421440),expo(angle,9))
    list6 = mut(dev(1414477,65383718400),expo(angle,11))
    return (1 / angle) + list1 + list2 + list3 + list4 + list5 + list6

#就是那个tan的倒数
def cot(angle):
    return cos(angle) / sin(angle)

#双面函数
#sinh
def sinh(angle):
    list1 = dev(expo(angle,3),fuc(3))
    list2 = dev(expo(angle,5),fuc(5))
    list3 = dev(expo(angle,7),fuc(7))
    list4 = dev(expo(angle,9),fuc(9))
    list5 = dev(expo(angle,11),fuc(11))
    list6 = dev(expo(angle,13),fuc(13))
    list7 = dev(expo(angle,15),fuc(15))
    list8 = dev(expo(angle,17),fuc(17))
    list9 = dev(expo(angle,19),fuc(19))
    list10 = dev(expo(angle,21),fuc(21))
    return angle + list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9 + list10

#cosh
def cosh(angle):
    list1 = dev(expo(angle,2),fuc(2))
    list2 = dev(expo(angle,4),fuc(4))
    list3 = dev(expo(angle,6),fuc(6))
    list4 = dev(expo(angle,8),fuc(8))
    list5 = dev(expo(angle,10),fuc(10))
    list6 = dev(expo(angle,12),fuc(12))
    list7 = dev(expo(angle,14),fuc(14))
    list8 = dev(expo(angle,16),fuc(16))
    list9 = dev(expo(angle,18),fuc(18))
    return 1 + list1 + list2 + list3 + list4 + list5 + list6 + list7 + list8 + list9

#tanh
def tanh(angle):
    list1 = dev(expo(angle,3),3)
    list2 = mut(dev(2,15),expo(angle,5))
    list3 = mut(dev(17,315),expo(angle,7))
    list4 = mut(dev(62,2835),expo(angle,9))
    list5 = mut(dev(1382,155925),expo(angle,11))
    return angle - list1 + list2 - list3 + list4 - list5
