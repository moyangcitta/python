#!usr/bin/env python3
#-*- coding:utf-8 -*-
#practice_2048
import random
location = []
for i in range(16):
    location.append(0)

def number_make():                                  #生成随机数字
    while 1:                                        #循环消除相同位置的数字
        number_location_f = random.random() * 16    #产生随机位置
        number_location_c = "{0:.0f}".format(number_location_f + 1)
        number_location = eval(number_location_c)
        if location[number_location] != 0:          #判断是否存在相同数字
            continue
        else:
            location[number_location] = 2
        for i in range(16):                         #画出数字所在位置
            if i in [3,7,11]:
                print("\n")
            else:
                print("{}\t".format(location[number_location]),end = "")
                break

def direction_control(a):


def main():
    while 1:
        number_make()
        direction_control(input("请输入方向："))


main()

