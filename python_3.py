# -*- coding:UTF-8 -*-

#python的变量类型：数字 字符串 列表 元组 字典 集合

#-----------------------------------数字
#数字类型没有引号，字符串是有引号的
#数字运算， /  // ，前一个是整除，后一个是取整
# 绝对值 abs
#取最大值 max(a,b)
#range 去从a 到 b-1  (a,b)
#-----------------------------------字符串
#可以加减，但是加减要统一类型
#定位,定位索引
#len
# if str in str2包含关系
#格式化字符串
#str字符串的替换
#-----------------------------------列表
#列表的删除 过程不能成为变量否则是None type
#列表的添加
#列表取值
#列表
#去重
#-----------------------------------集合
# s = {1,2,3}
# print(type(s))
# print(s)
# ss = set((1,2,3))
# print(ss)
# ss.add(4)
# print(ss)
# ss.remove(4)
# print(ss)
#-----------------------------------字典
# key = {'admin':'123456','yum':'456789','yim':[123456,123]}
# print(type(key))
# print(key)
# print(key['admin'])
# print(type(key.values()))
# print(key.values())
# for num in range(0,3):
#     for i in key.values():
#         print(i)
#         print('Num' + str(num))
#         if num  == 2:
#             print(type(i))
#             print(i)
#             for sss in i:
#                 print(sss)

#课后作业：
    # 社工字典生成器 网站邮箱 网站弱口令 手机号 QQ 姓名 【混淆】
    # 1.网站备份（备份扫描器）


# #网站备份
# .rar .zip .gz .tar.gz .7z
# 网站名称 备份 beifen www www_xxx_com
# #网站邮箱
# whois查询到的邮箱 域名邮箱 手机邮箱 QQ邮箱 126
# #常见弱口令

# 生成器
# 输入 字符串操作 文档储存
# 网站备份生成器
# wwwroot = input("""请输入如下名称，例如：wwww.baidu.com
# 请输入：""")
# wwwroot_rel = wwwroot.split('.')
# print(wwwroot_rel)
# www_xxx_com = wwwroot_rel[0] + '_' + wwwroot_rel[1] + '_' + wwwroot_rel[2]
# list_www = ['备份','backup','beifen','www','wwwroot',wwwroot_rel[1],www_xxx_com]
# list = ['.rar','.zip','.tar','gz','.7z']
# for last_name in list:
#     for first_name in list_www:
#         results = first_name + last_name
#         print(results)
# 社工字典生成器生成器
# low = ['123','1234','12345','888','666','88888888','admin','manage','manager']
# def notwork(url):
#     print('生成关于网站的弱密码')
#     for lowpass in low:
#         first_lowpass = lowpass + url.split('.')[1]
#         print(first_lowpass)
#     for lowpass in low:
#         last_lowpass = url.split('.')[1] + lowpass
#         print(last_lowpass)
# def userinfo(tel,mail,user):
#     if len(tel) == 0 or len(mail) == 0 :
#         if len(user) == 0:
#             if len(tel) == 0:
#                 for lowpass in low:
#                     first_mail_str = lowpass + mail
#                     print(first_mail_str)
#                     last_mail_str = mail + lowpass
#                     print(last_mail_str)
#             else:
#                 for lowpass in low:
#                     first_mail_str = lowpass + mail
#                     print(first_mail_str)
#                     last_mail_str = mail + lowpass
#                     print(last_mail_str)
#                 for lowpass in low:
#                     first_user_str = lowpass + user
#                     print(first_user_str)
#                     last_user_str = user + lowpass
#                     print(last_user_str)
#         else:
#             if len(mail) == 0:
#                 for lowpass in low:
#                     first_tel_str = lowpass + tel
#                     print(first_tel_str)
#                     last_tel_str = tel + lowpass
#                     print(last_tel_str)
#             else:
#                 for lowpass in low:
#                     first_mail_str = lowpass + mail
#                     print(first_mail_str)
#                     last_mail_str = mail + lowpass
#                     print(last_mail_str)
#                 for lowpass in low:
#                     first_user_str = lowpass + user
#                     print(first_user_str)
#                     last_user_str = user + lowpass
#                     print(last_user_str)
#     else:
#         print('mail tel != 0')
# userinfo('','admin@admin.com','wangchaoyue')
# #列表
# list = [1,2,3,4,5,6]
# list.pop(2)
# list.remove(6)
# print(list)
# #字典
# dict = {'ee': 'ssr', 'f': 7, 't': 'a'}
#
# del dict['ee']  # 删除键 'Name'
# #取集合不同部分
# a= {"app", "a", "ch"}
# b = {"A", "r", "a"}
#
# z = a.symmetric_difference(b)
#
# #集合
# a = set(('1','2','5','v','8','o','6','k'))
# # 添加
# a.update({6,6})
# print(a)
# b = {x for x in 'fanjknakgnjakgnakjlg' if x not in 'abc'}
# print(b)
# #移除
# a.remove(6)
# print(a)