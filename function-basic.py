# 定義函式
# def 函式名稱(參數名稱):
#  程式碼
#
# 參數名稱可不打

# 呼叫函式
# 函式名稱

def sayhello():
    print("hello")


sayhello()


def say(msg):
    print(msg)

say("自訂message")


def add(a, b):
    ans = a+b
    print(ans)


add(14, 16)

#RETURN-p

def say2(msg):
    print(msg)
    return  # 結束函式，回傳None


val=say("Hello Function")
print(val)


def add2(a, b):
    ans2=a+b
    return "Hello"


val2 = add2(14, 16)
print(val2)  # 印出Hello


def multi(a, b):
    result = a*b
    return result


out = multi(3, 5)
print(out)

