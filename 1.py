from tkinter import *
from dbcollecter import Dbcollecter
import tkinter.messagebox
from pymysql import err
from user import *
from register import Register


class Login(Register):
    def the_tops(self):
        self.tops = Tk()  # 实例化一个Tk对象
        self.tops.geometry("350x200+600+250")  # 窗口尺寸
        self.tops.title("登陆界面")   # 标题
        self.tops.attributes("-alpha", 0.94)  # 实现窗口小透明
        photo = PhotoImage(file='qq3.gif')
        Label(self.tops, image=photo).grid(row=0, column=1, sticky=W)  # 加载一张图标
        self.create_pages()  # 设置界面
        mainloop()

    def login_in(self):
        self.username = self.the_Name.get()
        password = self.the_Pass.get()
        if self.username == '' or password == '':
            tkinter.messagebox.showinfo('警告', '账号和密码不能为空')
        else:
            conn = Dbcollecter.get_connect(self)  # 连接到数据库
            cursor = conn.cursor()  # 游标
            sql = 'select * from userss'
            cursor.execute(sql)
            result = cursor.fetchall()
            a = 0
            for i in result:
                print(i[0]+i[1])
                if self.username == i[0] and password == i[1]:  # 进入下载界面，为每个用户新建一个表
                    tkinter.messagebox.showinfo('提示', '恭喜你！登陆成功啦！')
                    a = 1
                    self.change_to_interface()
                    break
            if not a:
                tkinter.messagebox.showinfo('警告', '该用户名密码错误或未注册')

    def change_to_register(self):
        self.t = Tk()
        Register.the_register(self, self.t)

    def change_to_interface(self):
        self.tops.withdraw()
        #self.t.withdraw()
        top = Tk()
        View(top,self.username)

    def create_pages(self):

        Label(self.tops, text="用户名:", font=("楷体", 15)).grid(row=2, column=0)  # 用户名
        self.the_Name = Entry(self.tops, font=("楷体", 15))
        self.the_Name.grid(row=2, column=1, sticky=W, pady=10)

        Label(self.tops, text="密码:", font=("楷体", 15)).grid(row=3, column=0)  # 密码
        self.the_Pass = Entry(self.tops, show='*', font=("楷体", 15))
        self.the_Pass.grid(row=3, column=1, padx=1, pady=10, sticky=W)

        Button(self.tops, text="注册账号", font=("楷体", 15), command=self.change_to_register).grid(row=4, column=1, sticky=E, pady=10)
        Button(self.tops, text="登陆", font=("楷体", 15), command=self.login_in).grid(row=4, column=0)


a = Login()
a.the_tops()


