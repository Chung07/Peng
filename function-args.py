#參數的預設資料
def power(base,exp):
    print(base**exp)

power(3,2)
#預設0次方
def power2(base,exp=0):
    print(base**exp)

power2(3)

print("--------------------------")
#使用參數名稱對應
def divide(a,b):
    print(a/b)
divide(2,4)
divide(b=5,a=10)


print("--------------------------")
#無限參數資料
def avg(*num):
    sum=0
    for n in num:
        sum+=n
    print(sum/len(num))
avg(3,4)