# -*- coding: utf-8 -* #讀取中文

# 使用json格式讀取，複寫檔案
import json
with open("config.json",mode="r") as file:
    data=json.load(file) #讀取json資料，是一個字典資料 放入data
print(data)
print("name",data["name"])
print("version",data["version"])

data["name"]="New Name" #修改變數資料
#把新的資料寫回檔案中
with open("config.json",mode="w") as file:
    json.dump(data,file)