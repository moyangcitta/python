def findMinAndMax(L):
    if L != []:
        (getMin,getMax) = (L[0],L[0])
        for i in L:
            if getMax < i:
                getMax = i
            if getMin > i:
                getMin = i
        return(getMin,getMax)
    else:
        return(None,None)

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