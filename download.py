import requests
import json
import random
import time
import tkinter.messagebox
from headers import Heders
from bs4 import BeautifulSoup
from dbcollecter import Dbcollecter
import threading
from pymysql import err
class Download(Heders, Dbcollecter):
    def download_song(self, song_list, lists,a_user):
        ips = self.get_proxy_ip()
        for n in lists:  # 遍历所选歌曲
            song = song_list[n]   # 在列表中找到所选歌曲
            headers = {'user-agent': Heders.get_user_agent(self)}   # 随机获得一个浏览器头
            vkey_url = 'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?&jsonpCallback=MusicJsonCallback&cid=205361747&songmid=' + song.get(
                'mid') + '&filename=C400' + song.get('media_mid') + '.m4a&guid=6612300644'
            #proxy_list = self.get_proxy_ip()  # ip池还没用
            #proxy_ip = random.choice(proxy_list)
            #proxies = {'http': proxy_ip}
            try:
                 resp_2 = requests.get(vkey_url, headers=headers)   # 发送请求
            except Exception :
                tkinter.messagebox.showinfo('提示', '歌曲解析失败')

            resp_2 = json.loads(resp_2.text)   # json解析
            vkey = resp_2['data']['items'][0]['vkey']   # 获得歌曲'vkey'
            song_url = 'http://dl.stream.qqmusic.qq.com/C400' + song.get('media_mid') + '.m4a?vkey=' + \
                       vkey + '&guid=6612300644&uin=0&fromtag=66'   # 获得歌曲url
            title = song.get('song_title')   # 歌名
            name = song.get('singer_name')   # 歌手
            id = str(song.get('id'))     # 歌曲id
            song_name = title + '-' + name + '-' + id   # 歌曲信息

            try:
                response = requests.get(song_url, stream=True, headers=headers)
               # t2 = threading.Thread(target=run_thread, args=(8,))
            except Exception :
                    tkinter.messagebox.showinfo('提示', '歌曲下载失败')

            try:
                Dbcollecter.save_song(self, title, name, id, a_user)   # 保存下载的歌曲到数据库
                with open(song_name + '.mp3', 'wb') as file:   # 保存歌曲到本地
                    file.write(response.content)
                tkinter.messagebox.showinfo('提示', '下载成功')
            except (err.IntegrityError):
                tkinter.messagebox.showinfo('提示', '已下载过本歌曲')
                break
            time.sleep(1)   # 休息会哈


    def get_proxy_ip(self):   # 一个未完工的ip池
        url = 'http://www.89ip.cn/'
        self.headers = {'user-agent': Heders.get_user_agent(self)}
        resp = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        url = 'http://www.89ip.cn/'
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'lxml')
        ip = soup.select('tbody > tr > td:nth-child(1)')
        ips = []
        for i in ip:
            ips.append(i.text[4:-2])
        return ips
