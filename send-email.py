#send email
#準備訊息物件設定
import email.message

msg=email.message.EmailMessage()
msg["From"]="dylocochung@gmail.com"
msg["To"]="chung30130@gmail.com"
msg["Subject"]="Hello chung"

#寄送純文字內容
# msg.set_content("This is an email from a python program!")

#寄送比較多樣式內容（html)
msg.add_alternative("<h3>三號標題</h3>郵件內容",subtype="html")

#連線到SMTP Server，驗證寄件人身份並發送郵件
import smtplib
#到網路上搜尋gmail smtp server或yahoo smtp server
#連線到gmail主機寄件人就要用gmail帳號
server=smtplib.SMTP_SSL("smtp.gmail.com",465) #port 465
server.login("dylocochung@gmail.com","Nhu03010808") 
server.send_message(msg)
server.close()