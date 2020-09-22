import math
number = []
tag = 0
for i in [1,2,3,4]:
    for j in [1,2,3,4]:
        if j == i:
            break
        for k in [1,2,3,4]:
            if k == i,j:
                break
            else:
                number[tag] = i*100 + j*10 + k
                tag += 1
for i in len(number)-1:
    a = number[i]
    b = number[i+1]
    if a > b:
        c = a
        number[i+1] = c
        number[i] = b

j = 1
sum = 0
for i in range(5):
    j = j * (i + 1)
    sum += j
print(sum)

number = eval(input("请输入一个正整数："))
while True:
    if number%2 == 0:
        number = number/2
        print(number)
    elif number == 1:
        break
    else:
        number = number * 3 + 1
        print(number)

stature = input("请输入身高:")
weight = input("请输入体重:")
BMI = eval(weight)/(pow(eval(stature),2))
if BMI >= 28:
    print("fat")
elif BMI >= 24:
    print("overweight")
elif BMI >= 18.5:
    print("normal")
else:
    print("too thin")

for i in range(15):
    i *= 20
    print(i,end = " ")
    j = 5/9 * (i - 32)
    print("{:.2f}".format(j))


# #杨辉三角形
# def triangles():
#     while 1:
#         n += 1
#         yield n
#         for i in range(t):
#             n.append(0)
#             if i > 0:
#                 n[i] = n[i] + n[i - 1]
# n = 0
# results = []
# for t in triangles():
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
#
# for t in results:
#     print(t)

        # def findMinAndMax(L):
#     if L != []:
#         (getMin,getMax) = (L[0],L[0])
#         for i in L:
#             if getMax < i:
#                 getMax = i
#             if getMin > i:
#                 getMin = i
#         return(getMin,getMax)
#     else:
#         return(None,None)

# from PIL import Image
# from PIL import ImageFilter
# im = Image.open('birdnest.jpg')
# om = im.filter(ImageFilter.CONTOUR)
# om.save('birdnestContour.jpg')

# from PIL import Image
# from PIL import ImageFilter
# # im = Image.open("D:\\code\\python\\023c6f342789d222064450248fb0ad3b.jpg")
# im = Image.open("023c6f342789d222064450248fb0ad3b.jpg")
# im.save("tiger.png")
# r,g,b = im.split()
# om = im.filter(ImageFilter.CONTOUR)
# om.save("tigerContour.jpg")

# fname = input("请输入要写入的文件：")
# fo = open(fname,"w+")
# ls = ["唐诗","宋词","元曲"]
# fo.writelines(ls)
# fo.seek(0)
# for line in fo:
#     print(line)
# fo.close()

# fname = input("请输入要打开的文件：")
# fo = open(fname,"r")
# for line in fo.readlines():
#     print(line)
# fo.close()

# textFile = open("7.1.txt","rt")     #t表示文本文件方式
# print(textFile.readline())
# textFile.close()
# binFile = open("7.1.txt","rb")      #r表示二进制文件方式
# print(binFile.readline())
# binFile.close()