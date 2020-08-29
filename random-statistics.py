# -*- coding: utf-8 -* #讀取中文

#隨機模組
import random
#隨機選取
data=random.choice([1,5,6,10,20]) #選一個資料
print(data)

data2=random.sample([1,5,6,10,20],3)  #選多個資料
print(data2)

#隨機調換順序
data3=[1,5,8,20]  #洗牌
random.shuffle(data3)
print(data3)

#隨機取得亂數
data4=random.random() #0到1的隨機亂數=random.uniform(0.0,1.0)
print(data4)

#取得常態分配亂數
d5=random.normalvariate(100,10) #平均數100 標準差10，取得的資料大部分會在90~110
print(d5)

print("----------------------")

#統計模組
import statistics as stat
#平均值
mean=stat.mean(data3)
print(mean)

#中位數
median=stat.median([1,2,3,4,5,8,10])
print(median)

#標準差
stdev=stat.stdev([1,2,3,4,5,8,10])
print(stdev)