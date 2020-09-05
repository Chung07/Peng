from flask import Flask

#實體物件app
app=Flask(__name__) #__name__代表目前執行的模組

@app.route("/") #函式的裝飾(Decorator):以函式為基礎，提供附加的功能
def home():
    return "幫我送飯來!"

@app.route("/test") #要處理的網站路徑
def test():
    return "Test Sucseed!"

if __name__=="__main__":  #如果以主程式執行
    app.run() #立刻啟動伺服器 Running on http://127.0.0.1:5000/測試用網址