#Point實體物件的設計:平面座標上的點
class Point:
    def __init__(self,x,y): #定義初始化函式
        self.x=x
        self.y=y

p1=Point(3,4) #建立實體物件p1
print(p1.x,p1.y) #呼叫實體物件屬性

#建立第二個實體物件
p2=Point(5,6)
#操作物件
print(p2.x,p2.y)

print("-------------------------\n")

#FullName實體物件的設計:分開紀錄姓、名資料的全名
class FullName:
    def __init__(self,first,last):
        self.first=first
        self.last=last

n1=FullName("L.C","Chung")
print(n1.first,n1.last)

n2=FullName("Y.C","Liu")
print(n2.first,n2.last)