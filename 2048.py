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
            location_h = location[i]
            for j in range(4):
                print("{0:.0f}\t".format(location_h[j]),end = "")
            print("\n")

def count_h():                                          #计算每次行移动之和,提交行方向和列方向，判断是否有相同数字，完成功能
    for i in range(3):
        count_1 = location[i]
        count_2 = location[i + 1]
        for j in count_1,count_2:
            if count_1[j] == count_2[j]:
                count_1[j] = count_1[j] + count_2[j]
            elif count_1[j] == 0:
                count_1[j] = count_2[j]
            else:
                continue
        i += 1
    for i in range(3):
        count_1 = location[i]
        count_2 = location[i + 1]
        for j in count_1,count_2:
            if count_1[j] == 0:
                count_1[j] = count_2[j]
            else:
                continue

def count_l():                                          #计算每次列移动之和,提交行方向和列方向，完成功能
    for i in location:
        count = location[i]
        for j in range(3):
            if count[j] == count[j+1]:
                count[j] = count[j] + count[j+1]
            elif count[j] == 0:
                count[j] = count[j+1]
            else:
                continue
        i += 1
    for i in location:
        count = location[i]
        for j in range(3):
            if count[j] == 0:
                count[j] = count[j+1]
            else:
                continue

def direction_control(a):                               #方向控制
    if a == "w":                                        #自顶向下，列方向相加,先提交行，再提交列
        count_h()
    elif a == "a":
        count_l()
    elif a == "s":
        count_h()
        i = 4
        while i>1:
            count_1 = location[i]
            count_2 = location[i - 1]
            for j in count_1, count_2:
                if count_1[j] == 0:
                    count_1[j] = count_2[j]
                else:
                    continue
            i -= 1
    elif a == "d":
        count_l()
        i = 4
        while i>1:
            count = location[i]
            while j>0:
                if count[j] == 0:
                    count[j] = count[j-1]
                else:
                    continue
            i -= 1

def game_end():
    for i in location:
        location_sub = location[i]
        for j in location_sub:
            if location_sub[j] == 2048:
                return 1


def main():
    while 1:
        number_make()
        direction_control(input("请输入方向："))
        if game_end() == 1:
            print("游戏胜利")
        else:
            print("游戏结束")

main()

