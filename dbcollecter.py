import pymysql


class Dbcollecter():

    def get_connect(self):   # 连接到本地数据库
        host = 'localhost'
        port = 3306
        user = 'root'
        password = '123456'
        db = 'learing'
        charset = 'utf8'
        conns = pymysql.connect(host=host, port=port, user=user, passwd=password, db=db, charset=charset)
        return conns

    def save_song(self, singer_name, song_title, id, table_name):
        conn = self.get_connect()   # 连接到数据库
        cursor = conn.cursor()   # 游标
        sql_2 = 'insert into {} (singer_names,title_names,ids) values(%s,%s,%s)'   # 插入歌曲信息
        cursor.execute(sql_2.format(table_name), (singer_name, song_title, id))
        conn.commit()   # 提交内容
        cursor.close()  # 关闭连接
        conn.close()



'''
sql = 'select username from userss '
        cursor.execute(sql)
        result = cursor.fetchall()
        a = 0
        for i in result:
            if i[0] == table_name:
                a=1
                break
        if not a:
              sql_1 = 'create table {} (singer_names varchar(20),title_names varchar(20),ids varchar(20) primary key) character set utf8'
              cursor.execute(sql_1.format(table_name))   # 建表
'''

