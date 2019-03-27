import tkinter.messagebox
import requests
import json
from urllib import parse
class Pars():
    def find_songs(self, word):
        # 浏览器头部
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
        # 歌曲信息url
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=64768420417553403&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&\
         p=1&n=100&{}&g_tk=1531112714&loginUin=3237707674&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
        dict = {'w': word}
        url_data = parse.urlencode(dict)   # 将word编码

        try:
            resp = requests.get(url.format(url_data), headers=headers)  # 发送请求
        except Exception:
            tkinter.messagebox.showinfo('提示', '歌曲解析失败')

        self.all_songs = json.loads(resp.text)['data']['song']['list']   # json解析