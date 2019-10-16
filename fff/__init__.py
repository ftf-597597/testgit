#!/usr/bin/python
#-*-coding:utf8-*-


# import pymysql   #用来连接与操作数据库的
# conn=pymysql.connect(host='192.168.2.135',port=3306,user='root',passwd='1024')  #连接数据库的
#
# #创建游标
# cusor=conn.cursor()
# #执行sql语句
# cusor.execute('create database pachong')
# cusor.execute('show databases;')

# import xlwt
# xl=xlwt.Workbook(encoding='utf-8')
# sheet=xl.add_sheet('sheet3')
# for i in range(1,10):
#     for j in range(1,1+i):
#         sheet.write(i,j,'%s*%s=%s'%(i,j,i*j))
# xl.save('b.xls')
# print('over')




# import xlwt
# xl=xlwt.Workbook(encoding='utf-8')
# sheet=xl.add_sheet('sheet1')
# for i in range(1,10):
#     for j in range(1,1+i):
#         sheet.write(i-1,j-1,('%s*%s=%s')%(i,j,i*j))
# xl.save('b.xls')
# print('over')

# a = int(input('请输入'))
# for i in range(len(a)):

# while True:
#     str=input("please input a string:")#输入一个字符串
#     length=len(str)#求字符串长度
#     left=0#定义左右‘指针’
#     right=length-1
#     while left<=right:#判断
#         if str[left]==str[right]:
#             left+=1
#             right-=1
#         else:
#             break;
#     if left>right:
#         print("yes")
#     else :
#         print

# a=1
# b=0
# while a<= 100:
#     print(i)
#     i+=1
#     a+=1
# print("%s"%a)

# b=0
# i=0
# while i<=100:
#     print(i)
#     b += i
#     i+=1
#
# print(b)

# def qwe(**kwargs):
#    print(kwargs)
# qwe(name=123,age=456)
#
#
# def qwe(*args):
#    print(args)
# qwe(123)

# def qwe():
# a=0
# for i in range(101):
#     a=a+i
# qwe()

# import xlrd
# xr = xlrd.open_workbook('b.xls')
# a = xr.nsheets
# name = xr.sheet_names()
# sheet = xr.sheet_by_name('nei')
# hangshu = sheet.nrows
# lieshu = sheet.ncols
# with open('999.txt','w',encoding='utf-8') as x:
#     for i in range(hangshu):
#         for j in range(lieshu):
#             hang = sheet.cell(i,j).value
#             x.write(hang+' ')

# file = open('aaaa')
# text =file.read()
# print(text)
# file.close()

# file = open('aaaa','w')
# file.write(('nihao\n')*5)
# file.close()
#
# file = open('aaaa')
# text = file.read()
# print(text)
# file.close

# file = open('aaaa','w')
# file.write(('nihao!\n')*10)
# file.close()
#
# file = open('aaaa')
# text = file.read()
# print(text)
# file.close()

# a = int(input('》》》'))
# b = int(input('》》》'))
# c = int(input('》》》'))
# n = [a,b,c]
# n.sort()
# if n[0]+n[1]>n[2]:
#     if n[0]**2+n[1]**2==n[2]**2:
#         print('直角三角形')
#     elif n[0]**2+n[1]**2>n[2]**2:
#         print('锐角三角形')
#     elif n[0]**2+n[1]**2<n[2]**2:
#         print('钝角三角形')
# else:
#     print('不是三角形')

# a=input('>>>')
# b=list(a)
# c=list(reversed(b))
# if b==c:
#     print('回文')
# else:
#     print('非回文')

# a=[5,2,4,0]
# for i in range(len(a)):
#     for j in range(1,len(a)):
#         if a[j-1]>a[j]:
#             a[j-1],a[j]=a[j],a[j-1]
#             print(a)

# a=[15,22,22,38,38,18,2,38]
# # # for i in range(len(a)):
# # #     for j in range(len(a)-1):
# # #         if a[j]>a[j+1]:
# # #             a[j],a[j+1]=a[j+1],a[j]
# # # print(a)
# # # b=[]
# # # for i in a:
# # #     if i not in b:
# # #         b.append(i)
# # # print(b)

# import paramiko
# ssh12 = paramiko.SSHClient()
# ssh12.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh12.connect(hostname='192.168.10.56',port=22,username='root',password='123456')
# stuin,stuout,stuerr = ssh12.exec_command('ls -al')
# aa = stuout.read().decode('utf-8')
# print(aa)
# ssh12.close()


# import paramiko
# #创建一个ssh客户端
# ssh123 = paramiko.SSHClient()
#
# #将第一次连接的主机通过验证，并添加到know_host文件中
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh123.connect(hostname='192.168.10.56',port=22,username='root',password='123456')
# stuin,stuout,stuerr = ssh123.exec_command('ls -al')
# #stuin 指的是输入的命令,直接有结果的命令    (这三个量也可以是其它的,例a,b,c)
# #stuout 命令运行后的结果
# #stuerr 命令的报错
# aa = stuout.read().decode('utf-8')
# print(aa)
# #断开连接
# ssh123.close()

# import paramiko
# # # ssh123 = paramiko.SSHClient()
# # # ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# # # ssh123.connect(hostname='192.168.10.56',port=22,username='root',password='123456')
# # # stuin,stuout,stuerr = ssh123.exec_command('ls -al')
# # # aa = stuout.read().decode('utf-8')
# # # print(aa)
# # # ssh123.close()
#http://www.quanshuwang.com/book/7/7709
# import requests
# import re
# url = 'http://www.quanshuwang.com/book/7/7709'
# response = requests.get(url)
# response.encoding = 'gbk'
# html = response.text
# dl = re.findall(r'<DIV class="clearfix dirconone">(.*?)</Div>',html,re.S)
# print(dl)

#
# import xlwt
# xl = xlwt.Workbook(encoding='uft-8')
# sheet = xl.add_sheet('sheet1')
# for i in range(0,10):
#     for j in range(0,10):
#         sheet.write(i,j,'a')
# xl.save('qaz.xls')


#http://www.quanshuwang.com/book/1/1612



import requests
from pyquery import PyQuery as pq
response = requests.get('http://www.quanshuwang.com/book/1/1612')
response.encoding = response.apparent_encoding
doc = pq(response.text)
links = doc('div >li a')
for link in links.items():
    print('http://www.quanshuwang.com/book/1/1612'+link.attr.href)



    response = requests.get('http://www.quanshuwang.com/book/1/1612'+link.attr.href)
    response.encoding = response.apparent_encoding
    #print(response.text)
    doc = pq(response.text)
    title = doc('.bookInfo > h1:nth-child(1)').text()
    content = doc('#content').text()

    # print(title)
    # print(content)
    with open('很纯很爱昧.txt',mode='a+',encoding='utf-8') as f:
        f.write(title)
        f.write(content)
        f.write('\n')