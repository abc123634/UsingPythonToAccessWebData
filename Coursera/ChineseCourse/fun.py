import math
def fun(num):
    if num<0:
        print '-',
        num = -num
    if num/10:
        fun(num/10)
    print chr(num%10+48),

num = -1234
fun(num)