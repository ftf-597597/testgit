#!/usr/bin/python
#-*-coding:utf8-*-
# def jiuJiu():
#   for i in range(1,10):
#     for j in range(1,1+i):
#         print('{}*{}={}'.format(i,j,i*j),end=' ')
#     print()
# jiuJiu()



# txt=open('‪F:\1111.txt','r',encoding='utf8')
# a=txt.read()
# print(a)

# txt=open(r'212.txt','w',encoding='utf-8')
# a='你好'+'\n'+'\n'
# txt.write(a*100)



#
# txt=open(r'212.txt','a',encoding='utf-8')
# # def hanshu():
# for i in range(1,10):
#     for j in range(1,i+1):
#        txt.write('{}*{}={}'.format(i,j,i*j))
#     txt.write('\n')
# txt.close()
#
# a=open('333.txt','r',en)
# b=a.readlines()
# a=[]
# for i in b:
#     c=i.rstrip('\n')
#     b=a.readlines()
#     a=[]

# a=open(r'C:\Users\ftf\Pictures\20160107170247_5GX3k.thumb.700_0.jfif','rb')
# c=a.read()
# print(c)
#

# # a='dfdfd'
# # print(a.split('f'))
# #
# # b='fdjj'
# # b=b.replace('f','r',1)
# # print(b)
#
# c='fjkdjfj'
# print(c.startswith('f'))
# print(c.endswith('j'))
#
# c='jf{}djf'
# c=c.format(123)
# print(c)
#
# c='jjfj%sd'
# c=c%('张123')
# print(c)
#
# c='djfdj'
# d=c.split('f')
# e='123'.join(d)
#
# f='  hfdh  '
# print(f)
# fa=f.strip()
# print(fa)
#
# g='jjhhkk'
# ga=g.index('h')
# print(ga)
#
#
#

# with open('212.txt','r',encoding='utf-8') as a:
#     print(a.read())

# txt=open(r'‪F:\1111.txt‪','r+',encoding='utf-8')
# a=txt.red()
# print(a)




#
# def hanshu():
#     pass
#
# def hanshu1():
#     pass
#
# def hanshu2():
#     pass
#
#
# if __name__=='__main__':
#     print('hello')

# message='hello python world'
# print(message)
# message='hello python crash course world'
# print(me msage)

# first_name = 'ada'
# last_name = 'lovelace'
# full_name = first_name + ' '+ last_name
# print('hello',full_name.title() + '!')

#
# print('languages:\npython\nc\njavascript')
#
# print('\tpython')
# print('python')
#
# try:
#     dafj
# except Exception as e:
#     print('e')
#


# for i in range(50):
#     for j in range(100):
#         m=100-i-j
#         if i*2+j*1+0.5*m==100:
#             print(('公鸡{}，母鸡{}，小鸡{}').format(i,j,m))




# favorite_language = 'python       '
# print(favorite_language)


# a='     python   '
# print(a)
# b=a.lstrip()
# print(b)


# while True:
#   a=int(input('输入数字'))
#   b=int(input('输入数字'))
#   c=a+b
#   print(c)

# try:
#     'fkdfjdkfj'
# except TypeError as e:
#     print(e)
# else:
#     print('nihao')
# finally:
#     print('最终执行')

# try:
#     print('nihao')
# finally:
#     print('最终执行')
#
# print('nihao')
# raise TypeError
# print(1234)

# class Cat:
#     def __init__(self,newweiba,newcolor):
#         self.weiba=newweiba
#         self.color=newcolor
#
#     def eat(self):
#         print('----吃----')
#     def drink(self):
#         print('----喝----')
#     def prinfo(self):
#         print(self.color)
#         print(self.weiba)
# big cat=Cat('有'，'花色')
# big flower cat=Cat('有','花色')

# big_flower_cat=Cat()
# big_flower_cat.eat()
# big_flower_cat.drink()
# big_flower_cat.color='花色'
# print(big_flower_cat.color)
# big_flower_cat.weiba='有'
# print(big_flower_cat.weiba)
# big_flower_cat.leg=('四条')
# print(big_flower_cat.leg)
# big_flower_cat.prinfo()
# limao=Cat()
# limao.color='白'
# print(limao.color)
# limao.weiba='有'
# print(limao.weiba)


#
# class Dog():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def sit(self):
#         print(self.name.title() + "is now sitting.")
#     def roll_over(self):
#         print(self.name.title() + "rolled over")
#
#
# my_dog = Dog('willie',6)
# print('my dog name is ' + my_dog.name.title() + '.')
# print('my dog is ' + str(my_dog.age) + ' years old.')

# p=('fdfd%ajx,k{}dj123abc0011')
# print(p.upper())
# print(p.lower())
# print(p.swapcase())
# print(p.title())
# print(p.split(','))
# print(','.join(p))
# print(p.startswith('f'))
# print(p.endswith('j'))
# print(p.format(123))
# print(p%(234))
# print(p.count('f'))
# print((p.index('j')))
#
#
# o=('0b11ac')
# print(type(o))
# print(len(o))
#
# oa=hex(16)
# print(oa)
#
# ob=enumerate(123)
# print(ob)
#
# z=oct(8)
# print(z)
#
# x=bin(3)
# print(x)
#
# a=chr(97)
# print(a)
#
# a=ord(a)
# print(a)
#
# a=sum((1,2,3))
# print(a)
#
# a=min((1,2,3))
# print(a)
#
# a=max((1,2,3))
# print(a)
#
# a,b=divmod(8,4)
# print(a)
#
#
# a=[11,12,34,14]
# a.append(123)
# print(a)
#
# a=[11,22,33,44]
# a.insert(1,123)
# print(a)
#
# a=[11,0,12]
# a.remove(11)
# print(a)
#
# a=[11,22,33,44]
# a.reverse()
# print(a)
#
# a=[11,12,13,14]
# a.pop(0)
# print(a)

# a={12,11,1,4,15}
# a.add(18)
# print(a)
# a={11,12,13}
# a.remove(12)
# print(a)
#
# a={'name':'fu','age':20}
# print(a)
# print(a.values())
# for i,j in a.items():
#     print(i,j)
# a['sex']=['nan']
# print(a)
# a.pop('sex')
# print(a)
# a.popitem()
# print(a)
# b={'nianji':8}
# a.update(b)
# print(a)

# a=[11,12,13]
# a.append(14)
# print(a)
# a.remove(11)
# print(a)
# a.insert(1,123)
# print(a)
# a.pop()
# print(a)
# a.reverse()
# print(a)
#
# b=sum((1,2,3))
# print(b)
#
# a='    jfdjj    '
# print(a)
# print(a.strip())

# class Cat:
#     def __init__(self,newweiba,newcolor):
#         self.weiba=newweiba
#         self.color=newcolor
#     def __str__(self):
#     msg='有没有尾巴:'+self.weiba+'\n颜色是: '+self.color
#       return msg
# def __eat(self):
#     print('----吃----')
#     return 1
# def drink(self):
#     print('----喝----')
# XiaoHuaMao=Cat('有','花色')
# print(XiaoHuaMao)
# XiaoHuaMao=Cat('没有','白色')





# class Sweetpotato:
#   def __init__(self):
#     self.cookedLevel=0
#     self.cookedString='生的'
#     self.condiments=[]
#   def __str__(self):
#     msg='地瓜的生熟程度: '+self.cookedString
#     msg+='\n地瓜的等级为: '+str(self.cookedLevel)
#     msg+'\n添加的佐料为: '
#     if len(self.condiments)>0:
#       for i in self.condiments:
#         msg+=i+','
#       msg=msg.strip(',')
#     else:
#         msg+='当前没有添加佐料'
#     return msg
#   def cook(self,times):
#       self.cookedLevel+=times
#       if self.cookedLevel>8:
#           self.cookedString='烤成木炭了'
#       elif self.cookedLevel>5:
#           self.cookedString='烤好了'
#       elif self.cookedLevel>3:
#           self.cookedString='半生不熟'
#       else:
#           self.cookedString='生的'
#   def addcondimens(self,temp):
#       self.condiments.append(temp)
# digua=Sweetpotato()
# print(digua)
# digua.cook(4)
# digua.addcondiments('芥末')
# print(digua)
# digua.cook(3)
# digua.addcondiments('盐')
# print(digua)
# digua.cook(3)
# print(digua)
# # diggua=Sweetpotato()
# # print(diggua)


#
# class Animal():
#     def talk(self):
#         pass
# class people(Animal):
#     def talk(self):
#         print('say hello')
# class Pig(Animal):
#     def talk(self):
#         print('hengheng')
# class Dog(Animal):
#     def talk(self):
#         print('wangwang')
# people().talk()
# Dog().talk()


# class Student:
# #     def hanshu(self):
# #         print(('nihao'))
# # class KdStudent(Student):
# #     def hanshu(self):
# #         print('jfidjjfdijfjd')
# # laowang=KdStudent()
# # laowang.hanshu()

# class Home:
#     def __init__(self,newarea):
#         self.area=newarea
#         self.containsItems=[]
#     def __str__(self):
#         msg='家当前可用面积为: '+str(self.area)+'平方米\n'
#         msg+='家里目前的家具有: '
#         if len(self.containsItems)>0:
#             for i in self.containsItems:
#                 msg+=i.name+','
#             msg=msg.strip(',')
#         else:
#             msg+='当前还没有家具'
#         return msg
#     def additems(self,item):
#         if self.area>item.area:
#             self.containsItems.append(item)
#             self.area-=item.area
# class Bed:
#     def __init__(self,newname,newarea):
#         self.name=newname
#         self.area=newarea
#     def __str__(self):
#         msg='床的面积为: '+str(self.area)
#         msg+='\n床的样式为: '+self.name
#         return msg
# home=Home(110)
# print(home)
# bed=Bed('席梦思',4)
# print(bed)
# home=Home(110)
# print(home)
# home.additems(bed)



#
# import xlwt   #导入xlwt模块,只有写入的权限
# xl=xlwt.Workbook(encoding='utf8')   #设置Excle文件格式
# sheet=xl.add_sheet('fff')  #添加一个标签页（标签页的名称可以重命名）
# for i in range(1,10):
#     for j in range(1,1+i):
#
#        sheet.write(i-1,j-1,'{}*{}={}'.format(i,j,i*j))  #向标签页里写入内容，第一个行   第二个代表列    #第三个写入的是内容
# # sheet.write(1,0,'xieru')
# xl.save('a.xls')

# import xlrd
# xr=xlrd.open_workbook('a.xls')    #打开要操作的excle文件，括号里面是文件名或者是路径
# #1.获取所有标签页
# b=xr.nsheets   #获取总共有多少个标签页
# print(b)
# sheet=xr.sheets()[0] #通过索引来进入操作的标签页
# hangshu=sheet.nrows   #获取标签页中有多少行
# print(hangshu)


#
# name=xr._sheet_names
# print(name)
# sheet=xr.sheet_by_name('fff')
# hanshu=sheet.nrows
# print(hanshu)
# hang3=sheet.row_values(2) #获取标签页的第几行
# print(hang3)
# lieshu=sheet.ncols #获取标签页中有多少例
# print(lieshu)
# lie3=sheet.col_values(2) #获取标签页中的第几列
# print(lie3)
# gezi=sheet.cell(0,0).value
# print(type(gezi))

# name=input('please enter your name:')
# print('hello，'+ name + '!')
#


# import xlwt
# xl=xlwt.Workbook(encoding='utf8')
# sheet=xl.add_sheet('fff')
# for i in range(1,10):
#     for j in range(1,1+i):
#         sheet.write(i-1,j-1,'{}*{}={}'.format(j,i,i*j))
# xl.save('a.xls')

# while True:
#     number = input('请输入一个数\n>>>')
#     number = int(number)
#     if number % 10 ==0:
#         print('是10的整倍数')
#     else:
#         print('不是10的整倍数')

#
# while True:
#     number = input('请问几位用餐?\n>>>')
#     number = int(number)
#     if number>8:
#         print('无空桌')
#     else:
#         print('有空桌')

# a=1
# while a<5:
#     print(a)
#     a=a+1

# from xlutils.copy import copy
# import xlrd
# yuan_file=xlrd.open_workbook('a.xls')
# new_file=copy(yuan_file)   #复制文件,并不是直接写入到原文件里,而是复制一份新文件再操作,没有读取功能
# sheet=new_file.get_sheet(0)   #获取要操作的标签页,get_sheet(下标位置)
# sheet.write(0,0,1111)


# prompt = '\nTell me something,and I will repeat it back to you:'
# prompt += "\nEnter 'quit' to end the program."
# a = True
# while a:
#     message = input(prompt)
#     if message == 'quit':
#         a = False
#     else:
#         print

# a = ('你去过的city')
# a +=('\n如何去过写"quit"')
#
# while True:
#     city = input(a)
#     if city== 'quit':
#         break
#     else:
#       print('这个地方我喜欢')

# a = 0
# while a<3:
#     a+=1
#     if a%2==0:
#         continue
#     print(a)




# #
# b=int(input('请问您多大了?\n>>>'))
# a=True
# while a:
#     age = input(b)
#     if age == 'quit':
#         break
#     else:
#         age=int(age)
#         if age<3:
#           print('free')
#         elif (age>3 and age<=12):
#             print('10元')
#         else:
#             print('15元')


# while True:
#     age = input('请问你多大了？\n>>>')
#     if (age=='quit'):
#         break
#     else:
#         age=int(age)
#         if age<3:
#             print(0)
#         elif (age>=3 and age<=12):
#             print(12)
#         else:
#             print(15)

# def favourite_book(title):
#     print('One of my favourite book is !'+title.title()+'!')
# favourite_book(  '  学的是函数')

# def hanshu():
#     for i in range(1,10):
#         for j in range(1,i+1):
#             print('{}*{}={}'.format(j,i,i*j),end=' ')
#         print()
# hanshu()

# def describe_pet(animal_type,pet_name):
#     print('I have a' + animal_type + '.')
#     pr


# import time
# b=time.time()
# print(b)
# a=time.gmtime()  #utc时间
# c=time.localtime()   #本地时区的时间
# print(a)
# print(c)
# print(time.strftime('%Y0-%m-%d %X',time.localtime())) #将结构化时间转换为格式化时间
# print(time.strptime('2019/09/18 10:05:28','%Y/%m/%d %X'))  #将格式化时间转换为 结构化时间

# import time
# a=(2019,7,1,16,27,34,1,231,14)
# b=time.mktime(a)
# print(b)

# import time
# a=time.localtime()
# a=(2019,9,18,10,52,16,2,261,-1)
# b=time.mktime(a)
# print(b)

# import time
# from time import sleep
# start=time.time()
# for i in range(3):
#     sleep(3)
#     print(i)
# end=time.time()
# print(end-start)
# b=0
# a='0123'
# a=a[::-1]
# print(a)
# for i in range(len(a)):
#     for j in range(10):
#         if str(j)==a[i]:
#             b+=j*10**i
# print(b)


# def shopping_car(self):
#     while True:
#         self.show_menu()
#         i=int(input('请输入要购买的商品号：'))
#         shangpin1=['面包','泡面','可乐','水']
#         jiaqian=[0,15,20,3,5]
#         if i>0 and i <=len(shangpin1):
#             shopping_car().append(shangpin1[i - 1])
#             d.append(jiaqian[i])
#             print()
# f='商品列表如下： '
# f+="\n面包10元\n矿泉水3元\n薯片6元\n牙刷2元"
# f+='\n你想买什么东西？'
# i=f
# if i<2:
#  print('您的金额不足')


# product_list = [
#     ('iphone',5000),
#     ('coffee',31),
#     ('bicyle',888),
#     ('iwatch',2666),
#     ('Mac Pro',12000),
#     ('book',88)
# ]
# shopping_list = []#空列表，存放购买的商品
#
#
# salary = input("请输入你的工资:")
# if salary.isdigit():# isdigit() 方法检测字符串是否只由数字组成,是则返回True,否则返回False
#     salary = int(salary)
#     while True:
#         for index,i in enumerate(product_list):#index作为下标索引
#             print(index,i)
# #enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
#         user_choice = input("请输入你要购买的商品:")
#         if user_choice.isdigit():
#             user_choice = int(user_choice)
#             if user_choice < len(product_list) and user_choice >= 0:
#                 product_choice = product_list[user_choice]
#                 if product_choice[1] < salary:#买得起
#                     shopping_list.append(product_choice)#买得起，就放入购物车
#                     salary -= product_choice[1]
#                     print("Add %s into your shopping_list,your balance is \033[31;1m%s\033[0m"%(product_choice,salary))
#                 else:
#                     print("\033[41;1m你的余额只剩%s啦，还买个叼啊！\033[0m"%salary)
#                     print("---------shopping list-----------")
#                     for s_index, s in enumerate(shopping_list):
#                         print(s_index, s)
#                     print("---------shopping list-----------")
#                     print("你的余额为：\033[31;1m%s\033[0m" % salary)
#             else:
#                 print("没有这个商品")
#         elif user_choice == "q":
#             print("---------shopping list-----------")
#             for s_index,s in enumerate(shopping_list):
#                 print(s_index,s)
#             print("---------shopping list-----------")
#             print("你的余额为：\033[31;1m%s\033[0m"%salary)
#             exit()
#         else:
#             print("输入错误")
# else:
#     print("输入错误")


# def a_pet(pet_name,animal_type):
#     print('\n我有一只'+animal_type+'.')
#     print('我的'+animal_type+'叫'+pet_name)
# a_pet('狗','libai')
# a_pet('猪','zhangfei')
# a_pet('猫','你')
#
# a_pet(pet_name='mingshingyin',animal_type='羊')
# a_pet('ww','马')
# a_pet()




# def a_name(first_name,last_name,middle_name=''):
#     if middle_name:
#      full_name=(first_name + ' ' + middle_name+ ' ' + last_name + ' ')
#     # return full_name.title()
#     else:
#      full_name=(first_name +' '+last_name)
#      # return full_name.title()
# b = a_name('li','bai')
# print(b)
# b = a_name

# def a_name(frirst_name,last_name,middle_name=''):
#     if middle_name:
#         name = frirst_name + ' ' + middle_name +' '+ last_name
#     else:
#         name = frirst_name + ' '+ last_name
#         return name.title()
#
# # b = a_name('li','bai')
# # print(b)
#
# b = a_name('li','bai','du')
# print(b)

# def build_person(first_name,last_name,age=''):
#     person = {'first':first_name,'last':last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi','hendrix','age=27')
# print(musician)

# def a_users(names):
#     for i in names:
#         j = 'hello, '+i.title()+ '!'
#         print(j)
# usernames = ['libai','dufu','zhangyang']
# a_users(usernames)


# def show_magicians(names):
#     for name in names:
#         j = 'hello, '+name.title()+'!'
#         print(j)
# s_magicians=['libai','lifji','fjdj','jfjdjf']
# show_magicians(s_magicians)
#

# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
# my_new_car = Car('audi','a4',2018)
# print(my_new_car.get_descriptive_name())



# class Car:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#        self.odometer_reading=0
#     # def get_descriptive_name(self):
#      def read_odometer(self):
#         print('This car has ' + str(self.odometer_reading) + 'miles on it.')
# # my_new_car = Car('audi','a4',2018)
# # print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

# row = 1
# while row<=5:
#     #每一行打印的星星就是和当前的行数是一致的
#     #增加一个小的循环，专门负责当前行中，第一‘列’的星星显示
#     print('*')
#     row+=1

# import requests
# import re
# a = 'http://www.quanshuwang.com/book/143/143843/39964985.html'
# b = requests.get(a)
# c=b.content.decode('gbk')
# # print(c)
# guolv=re.compile('</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">style6()',re.S)
# answer=guolv.findall(c)
# for i in answer:
#   print(i)
#     # print(i





# 接收响应内容的第一种text
# c=b.text
# print(c)
# 接收响应内容第二种content:以字节的方式接收
# c=b.content
# print(c)




# with open('视频下载.mp4','wb') as f:
#     f.write(c)
#




# for i in range(0,50):
#     for j in range(0,100):
#         n=100-i-j
#         if 2*i+j*1+0.5*n==100:
#             print(i,j,n)

# for i in range(100,1000):
#     a=i//100
#     b=i//10%10
#     c=i%10
#     if a**3+b**3+c**3==i:
#         print(i)
#
# a=[5,3,2,0]
# for i in range(len(a)):
#     for j in range(1,len(a)):
#         if a[j-1]>a[j]:
#             a[j-1],a[j]=a[j],a[j-1]
#             print(a)


#
# import re
# zifu='4wqe\nQfwq123qfQwqw4'
# guolv=re.compile('q(.*?)q',re.S)
# answer=re.findall(guolv,zifu)
# answer1=guolv.findall(zifu)
# print(answer1)


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
# import json
# url='https://map.baidu.com/?qt=subwayscity&t=1569032818612'
# html=requests.get(url)
# geshi=html.text
# result=json.loads(geshi)
# i=0
# while True:
#     try:
#         city=result['subways_city']['cities'][i]['cn_name']
#         print(city)
#         i+=1
#     except:
#         break

# for i in range(50):
#     for j in range(100):
#         n=100-i-j
#         if 2*i+1*j+0.5*n==100:
#             print(('公鸡{},母鸡{},小鸡{}').format(i,j,n))

# a=[1,5,4,6,0]
# for i in range(len(a)):
#     for j in range(1,len(a)):
#         if a[j-1]>a[j]:
#             a[j-1],a[j]=a[j],a[j-1]
#         print(a)


# row = 1
# while row<= 9:
#     col = 1
#     while col <= row:
#         print('*',end='')
#         col +=1
#     # print('%d'% row)
#     print('')
#     row += 1


# i = 1
# while i <= 3:
#     print('Hello python')
#     i =i + 1


# i = 0
# while i <=100:
#     print(i)
#     i += 1

# result = 0
# i=0
# while i <= 100  :
#     if i % 2 == 0:
#      print(i)
#      result += i
#
#     i += 1
# print('0-100之间偶数相加结果 = %d'% result)

# i = 0
# while i <10:
#     if i == 3:
#         break
#     print(i)
#     i += 1
# print('over')


# i = 0
# while i <10:
#     if i == 3:
#         i += 1
#         break
#     print(i)
#     i += 1
#
# row = 1
# while row <=5:
#     print('*' * row)
#     row += 1

# row = 1
# while row <= 5:
#     col = 1
#     while col <= row:
#         # print
#         print('* v       ')
#         col += 1
#     print('第 %d 行'% row)
#     row += 1

# file = open('aaaa')
# text = file.read()
# print(text)
# print(len(text))
#
# print('-' * 50)
#
# text = file.read()
# print(text)
# print(len(text))
#
# file.close()
#
# file = open('aaaa','w')
# file.write('hello,python')
# file.close()


#1、打开
# file_read = open('aaaa')
# file_write = open('212.txt','w')
# #读写
# text = file_read.read()
# file_write.write(text)
# #关闭
# file_read.close()
# file_write.close()
#



#
# a=[1,5,20,2,12,0]
# for i in range(len(a)):
#     for j in range(1,len(a)):
#         if a[j-1]>a[j]:
#             a[j-1],a[j]=a[j],a[j-1]
#             print(a)


# import xlwt
# xl = xlwt.Workbook(encoding = 'utf-8')
# sheet = xl.add_sheet('sheet1')
# for i in range(1,10):
#     for j in range(1,1+i):
#
#       sheet.write(i,j,'%s*%s=%s'%(i,j,i*j))
#
# xl.save('212.xls')
# print('over!')


#
# import xlwt
# xl=xlwt.Workbook(encoding='utf8')
# sheet=xl.add_sheet('sheet2')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i,j,'%s*%s=%s'%(i,j,i*j))
# xl.save('312.xls')
# print('over')

# for num in[1,2,3]:
#     print(num)
#     if num==2:
#         break
# else:
#     print('会执行吗')
# print('循环结束')

#
# import xlwt
# xl=xlwt.Workbook(encoding='utf8')
# sheet=xl.add_sheet('sheet2')
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'%s*%s=%s'%(i,j,i*j))
# xl.save('212.xls')
# print('over')

# import xlwt
# xr=xlwt.open_workbook('212.xls')
# b=xr.nsheets
# print(b)
# sheet=xr.sheets[0]
# hangshu=sheet.nrows
# print(hangshu)


#爬虫：第一部：分析网址的变化
#第二步：分析网页源代码，通过正则表达式过滤
#第三步：根据过滤出来的内容，保存
 #https://www.douban.com/
 #
 # import requests
 # import re
 # class Douban(object):
 #     def qing_qiu(self):
 #         url = f'https://movie.douban.com/top250'
 #         head = {https://movie.douban.com/top250?stsrt=25&filter=}
 #         res = requests.get(url=url,headers=head)
 #
 #         h = res.content.decode('utf-8')
 #         return h
 #     def guo_lv(self,html):
 #         patt = re.compile((r'<img'))


# import requests
# import re
#
# class Douban(object):
#     def qing_qiu(self, page):
#         url = f'https://movie.douban.com/top250?start={page}&filter='
#         head = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
#         }
#         # 发送请求，并将结果赋值给res
#         res = requests.get(url=url, headers=head)
#         # 读取结果
#         h = res.content.decode('utf-8')
#         return h
#
#     def guo_lv(self, html):
#         patt = re.compile(r'<span class="title">(.*?)</span>', re.S)
#         items = patt.findall(html)
#
#         for i in items:
#             if '&nbsp' in i:
#                 items.remove(i)
#         return items
#
#     def save(self, shuju):
#         with open('a.txt', 'a', encoding='utf-8') as f:
#             for i in shuju:
#                 f.write(i + '\n')
#
#
# dd = Douban()
# for i in range(25, 100, 25):
#     hh = dd.qing_qiu(i)
#     shuju = dd.guo_lv(hh)
#     dd.save(shuju)


# import pymysql   #用来连接与操作数据库的
# conn=pymysql.connect(host='192.168.2.135',port=3306,user='root',passwd='1024',db='pachong')  #连接数据库的

#创建游标
# cusor=conn.cursor()
#执行sql语句
#cusor.execute('create database pachong') 创建数据库
#cusor.execute('create table biaoming(name char);')
# cusor.execute('show tables;')
# print(cusor.execute('show tables;'))
# conn.commit() #提交数据
# conn.close()   #断开连接



# import pymysql      #l；用来连接和操作数据库
# conn=pymysql.connect(host='192.168.2.101',port=3306,user='root',passwd='1024',db='pachong')
#
# #创建游标
# cusor=conn.cursor()
# #执行sql语句
# #cusor.execute('create database pachong;')      #创建数据库
# cusor.execute('show databases;')    #查看数据库
# cusor.execute('create table biaoming(name char);')     #创建表名
# cusor.execute('show tables;')        #查看表
# print(cusor.fetchall())        #查看上一句sql语句执行结果
# #cusor.execute('show tables;')
# #print(cusor.fetchall()) #默认只显示结果的第一个值
# conn.commit()   #提交数据
# # conn.close()  #断开连接


# import pymysql
# class mysql_learn(object):
#     def __init__(self):
#         conn = pymysql.connect(host='192.168.2.136',port=3306,user='root',password='123456')  #连接数据库
#         self.su = conn.cursor()   #设置游标
#     def cao_zuo(self):
#                #执行sql语句 execute 也能获取sql语句的结果的个数
#             self.su.execute('show databases;')
#              #提交数据，只有在对某个表的数据进行添加（insert），删除(delete)，更改(alter)
#             self.su.execute('use 111;')
#             self.su.execute('delete from biao;')
#             self.conn.commit() #提交
#                #断开连接
#             self.conn.close()
#             # self.su.execute('show tables;')
#             #读取上一个sql语句执行的结果
#                #fetchall 读取所有的内容
#                #fetchmany 读取多条内容，默认是一条
#                #fetchone  读取一条内容，写几个读几个
#             print(self.su.fetchone())
#             print(self.su.fetchall())
# d = mysql_learn()
# d.cao_zuo()


