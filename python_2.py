# -*- coding:UTF-8 -*-
#课堂小案例
# import os
# html = '''<html>
# 	<head>
# 		<title>VVSEC</title>
# 	</head>
# 	<body>
# 		<p>VVSEC</p>
# <script>
#
# {
#
# alert("我是对话框的内容");
#
# }
#
# </script>
# 	</body>
# </html>'''
#
# with open('vvsec.html','a+') as ff:
#     print('偶要创建：' + html)
#     ff.write(html)
#     ff.close()
#
# os.system('start vvsec.html')


#example2
# user_pass_dic = {'小红':'xiahong','xiaozhang':'admin','xiaoli':'d2a2a2a'}
# User_Name = input('请输入用户名：')
# Pass_Word = input('请输入密码：')
# userlist = []
# def judege_password():
#     Pass_Word = input('请输入密码：')
#     print(password)
#     if Pass_Word == password:
#         print('密码正确！')
#         exit()
#     else:
#         print('密码错误！')
# for user,password in user_pass_dic.items():
#     if User_Name == user:
#         print('用户名输入正确！')
#         while Pass_Word != password:
#             judege_password()
#         # if Pass_Word == password:
#         #     print('用户密码正确！')
#         # else:
#         #     print('密码错误！')
#     else:
#         continue
#     print('账号是:%s,密码是:%s'%(user,password))
# if User_Name in user_pass_dic[]



#example1
# def input_info():
#     User_Name = input('请输入账号：')
#     if User_Name == 'admin':
#         print('账号正确')
#         return 'user'
#
# def input_pass():
#     Pass_Word = input('请输入密码：')
#     if Pass_Word == 'pass':
#         print('密码正确！')
#         return 'pwd'
#
# User_Name = input('请输入账号：')
# if User_Name == 'admin':
#     Pass_Word = input('请输入密码：')
#     if Pass_Word == 'pass':
#         print('密码正确！')
#     else:
#         print('密码错误,请重新输入.')
#         while input_pass() != 'pwd':
#             input_pass()
# else:
#     print('账号错误,请重新输入.')
#     while   input_info() != 'user':
#         input_info()