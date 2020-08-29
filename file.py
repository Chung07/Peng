# -*- coding: utf-8 -* #讀取中文

#儲存檔案
# file=open("data.txt",mode="w") #open file ＃中文,encoding="utf-8"
# file.write("Hellow File\nSecond line\n中文輸入") #操作
# file.close()  #close file
#出現一個新的檔案data.txt

#較好的寫入語法
with open("data.txt",mode="w") as file:
    file.write("這是較好的寫法\n中文好棒棒")

# 讀取檔案
with open("data.txt",mode="r") as file:
    data=file.read() #把檔案資料放進變數data
print(data) #u印出data.txt

#把檔案中的數字資料一行一行加起來
with open("sum.txt",mode="w") as file:
    file.write("3\n5")
sum=0
with open("sum.txt",mode="r") as file:
    for line in file: #一行一行的讀取
        sum+=int(line)     #把讀到的字串轉換成數字加到總和裡
print(sum)


