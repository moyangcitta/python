#打印程序的介绍性信息
#获得程序运行需要的参数，即probA,probB,n
#利用球员A和B的能力值probA和probB，模拟n次比赛
from random import random

def printIntro():
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("程序运行需要A和B的能力值（以0到1之间的小数表示）")


def getInputs():
    a = eval(input("请输入选手A的能力值（0-1）："))
    b = eval(input("请输入选手B的能力值（0-1）："))
    n = eval(input("模拟比赛的场次："))
    return a,b,n

def simNGames(n,probA,probB):
    winsA,winsB = 0,0
    for i in range(n):
        scoreA,scoreB = simOneGame(probA,probB)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA,winsB

def simOneGame(probA,probB):
    scoreA,scoreB = 0,0
    serving = "A"
    while not gameOver(scoreA,scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA,scoreB


def gameOver(a,b):
    return a==15 or b==15


def printSummary(winsA,winsB):
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA, winsA / n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB, winsB / n))


def main():
    printIntro()                                                #输出介绍信息
    probA,probB,n = getInputs()                                 #获得用户输入
    winsA,winsB = simNGames(n,probA,probB)                      #模拟n次比赛
    printSummary(winsA,winsB)                                   #输出结果


main()