# qq_music
# qq_music V 0.0

####  1.py是主程序入口，操作界面，可以搜索音乐，并将所选的歌曲下载到本地

* 
#### header.py中用于随机选择一个浏览器头部
tkinter库，可视化必备！

* random库，用于随机选择一个headers

#### dowmload.py是用于获得下载url并下载保存歌曲，在下载成功时提示下载成功，并将歌曲信息同步到数据库。

*  requests库，发送get请求，获得网页信息

* json库，将获得的josn进行解码


*  time库，在下载一首歌曲后休息一会，反防爬

* tkinter.messagebox 用于提示下载信息

* BeautifulSoup 解析网页

* from pymysql import err 捕抓sql错误
#### parse.py解析歌曲搜索页面内容，将歌曲信息发送到可视化窗口

* json，requests和tkinter.messagebox，作用同上
#### dbcollecter.py连接到数据库，并将传入的歌曲信息保存到数据库，在下载已下载过的歌曲时发出提示！

*  pymysql连接到数据库啊！
