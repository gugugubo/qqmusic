import pymysql
class Dbcollecter():
    def get_connect(self):   # 连接到本地数据库
        host='localhost'
        port = 3306
        user = 'root'
        password = 'A1195550354'
        db = 'learing'
        charset = 'utf8'
        conns = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset)
        return conns

    def save_song(self, singer_name, song_title, id):
        conn = self.get_connect()   # 连接到数据库
        cursor = conn.cursor()   # 游标
        #cursor.execute('create table usbaggs (singer_names varchar(20),title_names varchar(20),ids varchar(20)) CHARACTER SET utf8')   # 建表
        sql = 'insert into usbaggs (singer_names,title_names,ids) values(%s,%s,%s)'   # 插入歌曲信息
        cursor.execute(sql, (singer_name, song_title, id))
        conn.commit()   # 提交内容
        cursor.close()  # 关闭连接
        conn.close()

