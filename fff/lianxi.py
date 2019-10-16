#!/usr/bin/python
#-*-coding:utf8-*-

#os 实现python与操作系统之间交互的
import os

#popen()  执行cmd命令

# dd = os.popen('notepad')
# print(dd.read())

#getcwd  获取当前所在的目录
# print(os.getcwd())

#chdir 切换目录
# os.chdir('C:')
# print(os.getcwd())

#mkdir 创建目录
# os.mkdir('aaa')

#创建递归目录
# os.makedirs('eee/qqq/www')


#删除递归目录
# os.removedirs('eee/qqq/www')


#删除空目录
# os.rmdir('aaa')

#删除文件
# os.remove('111.txt')

#文件重命名
# os.rename('11.txt','1212.txt')


#获取目录下的所有文件 listdir
# print(os.listdir('C:'))

#将文件名与路径分隔开

#将文件后缀名与路径分隔开

#判断文件名是否是个目录
# a = os.path.isdir(r'‪')
# print(a)


# a,b=0,0
# for i in os.listdir():
#     if os.path.isdir(i):
#         a+=1
#     else:
#         b+=1
#         print(a,b)
#
# input('请输入>>>')
# if


# while True:
#     year=int(input("输入一个年份："))
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('%d年是闰年' %year)
#         else:
#             print('%d年不是闰年' %year)
#     else:
#         if year%4==0:
#             print('%d年是闰年' %year)
#         else:
#             print('%d年不是闰年' %year)


#
# u = 'yangfan'
# p = 'a123'
# 设定正确的用户名和密码
import datetime
# 导入datetime模块

# count=0
# while count<3:
#     count+=1
# # 使用while循环，计数器从0开始，循环3次
#
#     username = input('请输入用户名：').strip()
#     pwd = input('请输入密码：').strip()
#     # input接收输入的用户名和密码，strip方法去掉两端的空格
#     if username ==u and pwd==p:
#         today=datetime.date.today()
#         welcome='欢迎%s登录，今天的日期是%s!'%(username,today) #使用格式化字符串，显示输入的姓名和今天的日期
#         print(welcome)
#         break #登录成功，跳出整个循环
#     elif username == '' or pwd =='':
#         print('账号或密码不能为空！')
#         continue #登录失败，结束本次循环，开始下一次循环
#     elif (username != u or pwd != p) and(username != '' or pwd !=''):
#         print('账号/密码错误，请重新登录!')
#         continue
#
# else:print('失败次数过多!')


# a='w'
# b='123'
# import datetime
# count=0
# while count<3:
#     count+=1
#     username=input('请输入用户名').strip()
#     pwd=input('请输入密码').strip()
#     if username==a and pwd==b:
#         today=datetime.date.today()
#         # welcome = '欢迎%s登录，今天的日期是%s!' % (username, today)
#         print('欢迎%s登陆，今天的日期是%s'% (username,today))
#         break
#
#     elif username=='' or pwd == '':
#         print('账号或者密码不能为空')
#         continue
#
#     elif username != 'u' or pwd != 'p':
#         print('账号或密码错误')
#         continue
#
# else:
#         print('输入次数过多')


# 写一个登陆的小程序
# username = xiaoming
# passwd = 123456
# 1、输入账号密码,输入正确就登陆成功，
# 　　提示：欢迎xxxx登陆，今天的日期是xxx。
# 2、输入错误时提示：账号/密码错误，请重新登陆
# 3、失败次数超过3次，提示，失败次数过多
# 4、要校验输入是否为空，如果输入为空，提示账号/密码不能为空。
# 　　什么都不输入和输入一个空格多个空格都算空。
# 　　输入为空也算操作错误一次

# u='x'
# p='123'
# import datetime
# count=0
# while count<3:
#     count+=1
#     username = (input('请输入用户名'))
#     pwd = (input('请输入密码'))
#     if username == u.strip() and pwd ==p.strip():
#         today = datetime.date.today()
#         print('欢迎%s登陆，今天是%s'%(u,today))
#         break
#
#     elif username == '' or pwd == '':
#         print('账号或者密码不能为空')
#         continue
#
#     elif (username != u or pwd != p) and (username != '' or pwd != ''):
#         print('输入有错误')
#         continue
#
# else:
#     print('输入次数过多')


# def hanshu():
#     print('测量开始')
#     wendu=39
#     shidu=50
#     print('测量结束')
#     return (wendu,shidu)
# result=hanshu()
# print

# b = open('aaaa','w')
# b.write('hello1\n'*10)
# b.close()
#
#
# a = open('aaaa')
# text = a.read()
# print(text)
# a.close()

#import xlwt
#def hanshu():
    # xl=xlwt.Workbook(encoding='utf8')
    # sheet=xl.add_sheet('sheet1')
    # for i in range(1,10):
    #     for j in range(1,i+1):
    #         sheet.write(i-1,j-1,'%d*%d=%d'%(i,j,i*j))
    # xl.save('fc.xls')
 #   print('over')
#hanshu()


# a = open('aaaa','w')
# a.write('hello8\n'*10)
# a.close()
#
# b = open('aaaa')
# c = b.read()
# print(c)
# b.close()
# hanshu()


# import requests
# import json
# url='https://map.baidu.com/?qt=subwayscity&t=1569032818612'
# html=requests.get(url)
# geshi=html.text
# result=json.loads(geshi)
# i=0
# while True:
#     try:
#         city=result['subway_city']['cities'][i]['cn_name']
#         print(city)
#         i+=1
#     except:
#         break

# import requests
# def hanshu():
#     a='https://video.pearvideo.com/mp4/adshort/20190929/cont-1607746-14436913_adpkg-ad_hd.mp4'
#     b=requests.get(a)
#     print(b)
#     c=b.content
#     print(c)
#     with open('视频.mp4','wb') as f:
#         f.write(c)
# hanshu()


#
# import os
# # os.chdir('C:')
# # print(os.getcwd())

# a=[5,2,6,0]
# for i in range(len(a)):
#     for j in range(1,len(a)):
#         if a[j-1]>a[j]:
#             a[j-1],a[j]=a[j],a[j-1]
#             print

# path = "‪C:\Users\ftf\Desktop\456.txt"
# dirs = os.listdir

# a,b=0,0
# for i in os.listdir():
#     if os.path.isdir(i):
#         a+=1
#     else:
#         b+=1
# print

# import requests
# from pyquery import PyQuery as pq
# response = requests.get('http://www.jianlaixiaoshuo.com/')
# response.encoding = response.apparent_encoding
# doc = pq(response.text)
# links = doc('dl >dd a')
# for links in links.items():
#     print('http://www.jianlaixiaoshuo.com/'+links.attr.href)
#     response = requests.get('http://www.jianlaixiaoshuo.com/'+ links.attr.href)
#     response.encoding = response.apparent_encoding
#     # print(response.text)
#     doc = pq(response.text)
#     title = doc('#BookCon > h1').text()
#     content = doc('#BookText').text()
#     # print(content)
#     with open('剑来小说.txt',mode='a+',encoding='utf-8') as f:
#         f.write(title)
#         f.write(content)
#         f.write('\n')


# import requests
# from pyquery import PyQuery as pq
# response = requests.get('http://www.jianlaixiaoshuo.com/')
# response.encoding = response.apparent_encoding
# doc = pq(response.text)
# links = doc('dl >dd a')
# for links in links.items():
#     print('http://www.jianlaixiaoshuo.com/'+links.attr.href)
#     response = requests.get('http://www.jianlaixiaoshuo.com/'+ links.attr.href)
#     response.encoding = response.apparent_encoding
#     # print(response.text)
#     doc = pq(response.text)
#     title = doc('#BookCon > h1').text()
#     content = doc('#BookText').text()
#     # print(content)
#     with open('剑来小说.txt',mode='a+',encoding='utf-8') as f:
#         f.write(title)
#         f.write(content)
#         f.write('\n')
#
# def demo(num_list):
#     print('函数内部代码')
#     num_list.append(9)
#     print(num_list)
#     print('函数执行完成')
#
# gl_list=[1,2,3]
# demo(gl_list)
# print(gl_list)

# def demo(num,*nums,**person):
#     print(num)
#     print(nums)
#     print(person)
# # demo(1)
# # demo(2,3,4,5)
# demo('name=小明','age=18'

# class Cat():
# #     def eat(self):
# #         print('小猫要吃鱼')
# #     def drink(self):
# #         print('小猫爱喝水')
# #     def go(self):
# #         print('小猫想去玩')
# #
# # tom = Cat()
# # tom.eat()
# # tom.drink()
# # tom.go()

#socket：本机自带的模块   作用：socket：套接字，封装的源端口号
#目的端口号，源ip和目的ip,提供的是双方通信功能
#tcp协议 通信
#服务器端
#创建一个套接字（创建一个有接收能力和发送能力的对象）
#AF_INET:代表的是IPV4
#SOCK_STREAM  #TCP套接字类型
#SOCK_DGRAM   #UDP套接字类型
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定ip地址和端口号
s.bind(('192.168.2.137',808))
#监听，启用服务器以接受连接
s.listen(3) #数字代表最大的等待数
while True:
    #接收请求
    #第一个值，建立连接的信息
    #第二个，客户端的IP地址和端口号
    client,addr=s.accept()
    #接收客户端发送的请求最大1024个字节
    recive=client.recv((1024))
    #将接收过来的信息解码打印
    print(recive.decode('utf8'))
    #发送响应
    #输入响应的内容
    response=input('请响应：')
    #将输入的响应内容发送
    client.send(response.encode('utf-8'))

