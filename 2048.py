#!usr/bin/env python3
#-*- coding:utf-8 -*-
#practice_2048
import random
location = [[0,0,0,0],                                 #建立基础列表
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

def number_make():                                      #生成随机数字
    while 1:                                            #循环消除相同位置的数字
        number_location_f_l = random.random() * 4       #产生随机列位置
        number_location_c_l = "{0:.0f}".format(number_location_f_l + 1)
        number_location_l = eval(number_location_c_l)
        number_location_f_h = random.random() * 4       #产生随机行位置
        number_location_c_h = "{0:.0f}".format(number_location_f_h + 1)
        number_location_h = eval(number_location_c_h)
        location_h = location[number_location_h]
        if location_h[number_location_l] != 0:          #判断是否存在相同数字
            continue
        else:
            location_h[number_location_l] = 2
            location[number_location_h] = location_h
        for i in range(4):                              #画出数字所在位置
            location_h = location[1]
            for j in range(4):
                print("{0:.0f}\t".format(location_h[j]),end = "")
            print("\n")

def direction_control(a):                               #方向控制
    if a == "w":


def main():
    while 1:
        number_make()
        direction_control(input("请输入方向："))


main()

