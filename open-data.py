# -*- coding: utf-8 -* #讀取中文
#網路連線、取得公開資料
import urllib.request as request
# src="https://www.ntu.edu.tw/"
# with request.urlopen(src) as res:
#   data = res.read().decode("utf-8")
# print(data)

#連到公開資料，內湖科技園區api(json檔)
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=296acfa2-5d93-4706-ad58-e83cc951863c"
with request.urlopen(src) as res:
  data = json.load(res) #用json模組讀取資料
#print(data)                                      #可以看到統編欄位是\ufeff統編，未來若要輸出不能只打"統編"

#取得公司名稱
companyL=data["result"]["results"]
# print(companyL)
for company in companyL:
   print(company["\ufeff統編"]+company["公司名稱"]+" [ "+company["公司地址"]+" ] ")

# #把名稱放進檔案中
with open("company.txt",mode="w") as file:   
   for company in companyL:
     file.write(company["\ufeff統編"]+company["公司名稱"]+" [ "+company["公司地址"]+" ] "+"\n")