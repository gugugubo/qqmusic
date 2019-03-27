from tkinter import *
from parse import Pars
from download import Download
class View(Pars,Download):  #继承dowmload和pars类
    def show_songs(self):
        self.clear()
        word = self.key_word.get()   # 输入的歌名
        Pars.find_songs(self, word)   # 找到歌曲
        self.result_list = []      # 保存歌曲信息
        for song in self.all_songs:
            result = {}
            result['id'] = song.get('id')    # 歌曲id
            result['mid'] = song.get('mid')
            result['media_mid'] = song.get('file').get('media_mid')    # midia_mid
            result['song_title'] = song.get('title')  # 歌名
            result['singer_name'] = song.get('singer')[0].get('name')  # 歌手
            self.result_list.append(result)
            musics = '>>>' + result['singer_name'] + '-' + result['song_title'] + '-' + str(result['id'])
            self.text.insert(END, musics)     # 将歌曲信息显示

    def tops(self):
        top = Tk()  # 实例化一个Tk对象
        top.geometry("910x500+80+100")  # 窗口尺寸
        top.title("研发真棒！")   # 标题
        top.attributes("-alpha", 1)  # 实现窗口小透明
        Label(top, text="请输入搜索音乐关键词:", font=15).grid(row=0, column=0, sticky=E)  # 提示搜索标签

        self.key_word = Entry(top, font=15)  # 搜索框
        self.key_word.grid(row=0, column=1, sticky=W)

        Button(top, text='立即搜索', command=self.show_songs, font=15).grid(row=0, column=2, sticky=W)   # 搜索按钮

        sb = Scrollbar(top)   # 滚动条
        sb.grid(sticky=W, row=1, column=2, ipady=150)
        self.text = Listbox(top, selectmode=MULTIPLE, font=15, width=80, height=18, yscrollcommand=sb.set) # 文本显示框
        self.text.grid(row=1, columnspan=2)
        sb.config(command=self.text.yview)

        Button(top, text="清空列表", font=15, command=self.clear).grid(row=2, column=0)  # 清空列表按钮
        Button(top, text="下载所选歌曲", font=15, command=self.down).grid(row=2, column=1)  # 下载按钮
        self.text.bind("<<ListboxSelect>>", self.showselection)   # 鼠标选择操作
    def clear(self):    # 清空显示内容
        self.text.delete(0, END)

    def insert_song(self, song):     # 显示歌曲
        self.text.insert(END, song)

    def showselection(self, *args):  # 存取所选歌曲
        self.lists = self.text.curselection()

    def down(self):   # 下载歌曲
        Download.download_song(self, self.result_list, self.lists)

music = View()   # 实例化一个对象
music.tops()
mainloop()  # 进入主事件循环


