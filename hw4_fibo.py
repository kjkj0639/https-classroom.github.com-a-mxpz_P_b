# -*- coding: utf-8 -*-

#25
def fib(num):
    if num == 0 or num == 1:
        return num

    else:
        return fib(num - 1) + fib(num - 2)


num = int(input("你想看費氏數列第幾個數字？ "))
print('費氏數列第', num, '個數字是', fib(num))
