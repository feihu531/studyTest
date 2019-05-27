# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 14:58
# @Author  : zhujg
# @File    : register.py
# @Software: PyCharm

# 接收输入账号密码，并进行合法性校验
def talk():
    while True:
        username = input('请输入你的用户名：').strip()
        if username.isalpha():
            break
        else:
            print('用户名必须为字母')

    while True:
        password1 = input('请输入你的密码：').strip()
        password2 = input('请再次输入你的密码：').strip()
        if password1 == password2:
            break
        else:
            print('两次输入密码不一致')

    return username,password1

# 账号密码拼成固定的格式
def register_interface(username,password):
    format_str = '%s:%s\n' %(username,password)
    return format_str

#将拼接好的格式写入文件
def handle_file(format_str,filepath):
    with open(r'%s' %filepath,'at',encoding='utf-8') as f:
        f.write(format_str)

def register():
    user,pwd=talk()
    format_str=register_interface(user,pwd)
    handle_file(format_str,'user.txt')

register()