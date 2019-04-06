from tkinter import *
from dbcollecter import Dbcollecter
import tkinter.messagebox
from pymysql import err
from user import *
#from login import login
class Login():
    def the_tops(self):
        self.tops = Tk()  # 实例化一个Tk对象
        self.tops.geometry("350x200+600+250")  # 窗口尺寸
        self.tops.title("研发真棒！")   # 标题
        self.tops.attributes("-alpha", 0.94)  # 实现窗口小透明
        photo = PhotoImage(file='qq.gif')
        Label(self.tops, image=photo, compound=CENTER).grid(row=0, column=1)
        #Label(self.tops).grid(row=1)
        Label(self.tops, text="用户名:", font=("楷体", 15)).grid(row=2, column=0)  # 用户名
        self.the_Name = Entry(self.tops, font=("楷体", 15))
        Label(self.tops, text="密码:", font=("楷体", 15)).grid(row=3, column=0)   # 密码
        self.the_Name.grid(row=2, column=1,sticky=W,pady=10)
        self.the_Pass = Entry(self.tops,show='*', font=("楷体", 15))
        self.the_Pass.grid(row=3, column=1,padx=1,pady=10)
        Button(self.tops, text="注册账号", font=("楷体", 15), command = self.save_user).grid(row=4, column=1,sticky=E,pady=10)
        Button(self.tops, text="登陆", font=("楷体", 15), command = self.login_in).grid(row=4, column=0)
        self.page=Frame(self.tops)
        self.login()
        mainloop()

    def login_in(self):
        username = self.the_Name.get()
        password = self.the_Pass.get()
        if username == '' or password == '':
            tkinter.messagebox.showinfo('警告', '账号和密码不能为空')
        else:
            conn = Dbcollecter.get_connect(self)  # 连接到数据库
            cursor = conn.cursor()  # 游标
            sql = 'select * from userss'
            cursor.execute(sql)
            result = cursor.fetchall()
            a = 0
            for i in result:
                if username == i[0] and password == i[1]:  # 进入下载界面，为每个用户新建一个表
                    tkinter.messagebox.showinfo('提示', '恭喜你！登陆成功啦！')
                    a =1
                    self.change()
                    break
            if not a:
                tkinter.messagebox.showinfo('警告', '该用户名密码错误或未注册')

    def save_user(self):
        username = self.the_Name.get()
        password = self.the_Pass.get()
        if username == '' or password == '':
            tkinter.messagebox.showinfo('警告', '账号或密码不能为空')
        else:
            conn =Dbcollecter.get_connect(self)   # 连接到数据库
            cursor = conn.cursor()   # 游标
            #cursor.execute('create table userss (username varchar(20) primary key, password varchar(20)) character set utf8')   # 建表
            sql = 'insert into userss(username, password) values(%s,%s)'   # 插入用户信息
            try:
                cursor.execute(sql, (username, password))
                tkinter.messagebox.showinfo('提示', '注册成功')
            except err.IntegrityError:
                tkinter.messagebox.showinfo('警告', '该用户名已经注册')
            conn.commit()   # 提交内容
            cursor.close()  # 关闭连接
            conn.close()

    def change(self):
        self.tops.withdraw()
        top = Tk()
        View(top)

    def login(self):
        t=tkinter.Toplevel(self.tops)
        Label(t, text="用户名:", font=("楷体", 15)).grid(row=2, column=0)



a = Login()
a.the_tops()


