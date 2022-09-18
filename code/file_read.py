#coding:utf-8
fp=open('D:/python/LSTM/data/poetry.txt', "r",encoding='UTF-8')
l=fp.readline()
print(l)
print(fp.tell())
for line in fp:
        print(line)
        print (fp.tell())

fp.close()
