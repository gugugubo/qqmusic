from tkinter import *
from dbcollecter import Dbcollecter
import tkinter.messagebox
from pymysql import err
from user import *


class Register(object):
    def the_register(self, a_tk):
        self.windows = a_tk       # 一个Tk对象
        self.windows.geometry("350x200+300+250")  # 窗口尺寸和位置
        self.windows.title("账号注册")      # 标题
        self.windows.attributes("-alpha", 0.94)  # 实现窗口小透明
        self.create_page()    # 设置界面
        mainloop()

    def create_page(self):
        Label(self.windows, text="用户名:", font=("楷体", 15)).grid(row=2, column=0)  # 用户名
        self.userName = Entry(self.windows, font=("楷体", 15))
        self.userName.grid(row=2, column=1, sticky=W, pady=10)

        Label(self.windows, text="密码:", font=("楷体", 15)).grid(row=3, column=0)  # 密码
        self.userPassword = Entry(self.windows, show='*', font=("楷体", 15))
        self.userPassword.grid(row=3, column=1, padx=1, pady=10)

        Label(self.windows, text="确认密码:", font=("楷体", 15)).grid(row=4, column=0)  # 确认密码
        self.userPassword_second = Entry(self.windows, show='*', font=("楷体", 15))
        self.userPassword_second.grid(row=4, column=1, padx=1, pady=10)

        Button(self.windows, text="立即注册", font=("楷体", 15), command=self.save_user).grid(row=5, column=1, pady=10)

    def save_user(self):
        username = self.userName.get()
        password = self.userPassword.get()
        second_password = self.userPassword_second.get()
        if username == '' or password == '':
            tkinter.messagebox.showinfo('警告', '账号或密码不能为空')
        elif second_password != password:
            tkinter.messagebox.showinfo('警告', '两次输入的密码不同')
        else:
            conn = Dbcollecter.get_connect(self)  # 连接到数据库
            cursor = conn.cursor()  # 游标
            # cursor.execute('create table userss (username varchar(20) primary key, password varchar(20)) character set utf8')   # 建表
            sql = 'insert into userss(username, password) values(%s,%s)'  # 插入用户信息

            sql_1 = 'create table {} (singer_names varchar(20),title_names varchar(20),ids varchar(20) primary key) character set utf8'  # 为每个用户建表


            try:

                cursor.execute(sql, (username, password))
                cursor.execute(sql_1.format(username))  # 建表
                tkinter.messagebox.showinfo('提示', '注册成功')
            except err.IntegrityError:
                tkinter.messagebox.showinfo('警告', '该用户名已经注册')
            conn.commit()  # 提交内容
            cursor.close()  # 关闭连接
            conn.close()
            self.windows.withdraw()