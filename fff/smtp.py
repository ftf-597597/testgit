#!/usr/bin/python
#-*-coding:utf8-*-

#发送邮件  smtplib

# import smtplib   #封装了smtp协议
# # import email.mime.text   #处理正文中的数据
# # import email.mime.multipart   #封装的是邮件的格式
# #
# # sender = 'ftf597597@163.com'  #定义一个发送者
# # reser = '1129414282@qq.com'    #接收者
# # server = 'smtp.163.com'
# #
# # #授权码
# # passwd = 'ftf597'
# #
# # #创建一个空邮件
# # message = email.mime.multipart.MIMEMultipart()
# #
# # #添加发件人、收件人、主题
# # message['from'] = sender
# # message['To'] = reser
# # message['Subject'] = 'python_learn'
# # aa = """台湾是中国的
# # """
# # cc = email.mime.text.MIMEText(aa)
# #
# # #将正文添加到邮件里
# # message.attach(cc)
# #
# # #定义发送邮件的服务器和端口号
# # smtp123 = smtplib.SMTP_SSL(server,465)  #465是端口号
# #
# # #登陆服务器
# # smtp123.login(sender,passwd)
# #
# # #发送邮件
# # smtp123.sendmail(sender,reser,message.as_string())  #.as_string() 需要用这个函数去处理
# #
# # #断开连接
# # smtp123.close()

import xlrd
import xlwt
with open('11.txt','w',encoding='utf-8')as a:
    a.write('aa,bb,cc,dd,ee,ff\n'*10)

xl = xlwt.Workbook(encoding='utf-8')
sheet = xl.add_sheet('python_text')

with open('11.txt','r',encoding='utf-8') as x:
    b = x.readlines()
    for i,j in enumerate(b):
        k = j.split(',')
        for m,n in enumerate(k):
            sheet.write(i,m,n)
xl.save('a.xls')

with open('222.txt','w',encoding='utf-8') as a:
    rd=xlrd.open_workbook('a.xls')
    aa=rd.sheet_by_name('python_test')
    hangshu=aa.nrows
    for l in range(hangshu):
        for k in aa.row_values(l):
           # a.write((k))
            print(k)