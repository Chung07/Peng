#類別有兩種方法
#1.類別與類別屬性
#2.類別與實體物件、實體屬性、實體方法


# 定義類別與類別屬性(封裝在類別中的變數和函式)
# 定義一個類別IO，有兩個屬性supportedSrcs和read
class IO:
    supportedSrcs = ["console", "file"]
    def __init__(self,src):
        self.src=src
    
    def read(self):
        if self.src not in IO.supportedSrcs:
            print("Not Supported")
        else:
            print("Read from", self.src)


# 使用類別
print(IO.supportedSrcs)  # 取得支援列表
IO.read("file")  # 呼叫類別中的函式
IO.read("Internet")
