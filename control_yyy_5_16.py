# 增加了三个方法 add_worker(...)，delete_worker(...)和change_workers（...）,
# 并将原来更新工人的犯罪记录的方法由change_workers（...）的名字改为了update_workers（...）
# 修改了WnobTime出现的不合理逗号问题

# 二次更新
# 增加了三个函数
# def change_time(self,timestr)求时间，为数据库端示警器功能做准备 注好像python有个datetime类，能对DtimeOfdate 和DPointOfTime 更好操作，出于不熟悉我仍然将其转化为字符串后进行操作
# def add_DateInfo(self,Dname,Dnum,DtimeOfdate,DPointOfTime)增加日期时间表
# def return_DateInfo(self,DtimeOfdate)返回按日期查询的违规数据

import pymysql


class SQL_Y():
    def __init__(self):
        # 登陆数据库
        pwd = "yangyue123Q1W2E3"
        self.key = self.connect_wxremit_db(pwd)

    # ============连接数据库==========
    def connect_wxremit_db(self, pwd):
        # yangyu123Q1W2E3
        # pwd = input("请输入密码：")
        conn = pymysql.connect(host="localhost", user="root", password=pwd, port=3306, database="HafetyHelmet",
                               charset="utf8")
        cursor = conn.cursor()
        sql = 'select * from workers'
        ret = cursor.execute(sql)
        cursor.close()
        if ret:
            print("登录成功！")
        else:
            print("登录失败！")
        return conn

    # ======================显示所有工人的信息表========================
    def print_data_workers(self):  # 显示workersconn=key
        cur = self.key.cursor()
        sql = "select * from workers"
        try:
            cur.execute(sql)
            results = cur.fetchall()
            print("Wname", " Wnum  ", "     Wsex", "Wage ", "Wjointime  ", "Wdepartment ", "Wimgpath                ",
                  "WnumberOfBreak   ", "WnobTime")
            for row in results:
                Wname = row[0]
                Wnum = row[1]
                Wsex = row[2]
                Wage = row[3]
                Wjointime = row[4]
                Wdepartment = row[5]
                Wimgpath = row[6]
                WnumberOfBreak = row[7]  # 违规时间
                WnobTime = row[8]  # 违规时间戳
                print(Wname, " ", Wnum, Wsex, " ", Wage, "  ", Wjointime, " ", Wdepartment, " ", Wimgpath, "     ",
                      WnumberOfBreak, "         ", WnobTime)
        except Exception as e:
            raise e

    '''显示工人表中所有信息'''

    # ================按时间显示犯罪的数据===============
    def print_data_info(self):  # 显示info
        cur = self.key.cursor()
        sql = "select * from Info"
        try:
            cur.execute(sql)
            results = cur.fetchall()
            print("infotime            ", "imgpath                ", "      带安全帽人数", "未带安全帽人数")
            for row in results:
                Info = row[0]
                Imgpath = row[1]
                Iwearer = row[2]
                Iunwearer = row[3]
                print(Info, ' ', Imgpath, '    ', Iwearer, '    ', '     ', Iunwearer)
        except Exception as e:
            raise e

    # ===============添加info的函数===========
    def add_info(self, Info, Imgpath, Iwearer, Iunwerer):
        cur = self.key.cursor()
        sql = 'insert into Info(Info,Imgpath,Iwearer,Iunwearer)value(%s,%s,%s,%s);'
        data = [(Info, Imgpath, Iwearer, Iunwerer)]
        cur.executemany(sql, data)
        self.key.commit()

    # def xxx(时间戳,字符串类型的文件名地址, 佩戴人数, 未佩戴人数):
    #    功能:存入时间戳表
    #    对于字符串类型的文件名地址，如C:\\Users\\ASUS\\Pictures\\4.png，在数据库中存时，会将双斜杠变为当斜杠，即通过数据库可视化工具
    #    查看数据库时效果为C:\Users\ASUS\Pictures\4.png 返回的字符串为C:\\Users\\ASUS\\Pictures\\4.png
    #    当然如果你存时就为C:\Users\ASUS\Pictures\4.png，那么效果为C:UsersASUSPictures4.png，返回的字符串为C:\Users\ASUS\Pictures\4.png

    # =========更新工人的犯罪记录============
    def update_workers(self, Wnum, NewTime):
        cur = self.key.cursor()
        sql = 'select * from workers where Wnum=%s;'
        cur.execute(sql, [Wnum])
        result = cur.fetchone()
        if result == None:
            return None
        else:
            WnumberOfBreak = result[7]
            WnobTime = result[8]
            WnumberOfBreak = WnumberOfBreak + 1
            if WnobTime == "":
                WnobTime = NewTime
            else:
                WnobTime = WnobTime + ' , ' + NewTime
            sql = 'update workers set WnumberOfBreak=%s where Wnum=%s'
            data = (WnumberOfBreak, Wnum)
            cur.execute(sql, data)
            sql = 'update workers set WnobTime=%s where Wnum=%s'
            data = (WnobTime, Wnum)
            cur.execute(sql, data)
            self.key.commit()

    # ================得到info数据================
    def return_Info(self, Info):
        '''def xx取(时间戳):
            “返回值类型：”
            xxx
            return 字符串 文件名, 佩戴人数, 未佩戴人数(元组形式)
        '''
        cur = self.key.cursor()
        sql = 'select * from info where Info=%s;'
        cur.execute(sql, [Info])
        return cur.fetchone()

    # ==========通过工牌获取公认的违规信息==========
    def return_workers(self, Wnum):
        '''def xx取(工号)：
            return 名片，名字，工号， 违规次数，违规对应时间戳…(返回值为元组形式)
            ["test.png", "叶凡", "123", "3", "x月x日,x月x日,x月x日"]
        '''
        cur = self.key.cursor()
        sql = 'select * from workers where Wnum=%s;'
        cur.execute(sql, (Wnum))
        result = cur.fetchone()
        tup = []
        if result is not None:
            tup = [result[6], result[0], result[1], str(result[7]), result[8]]
        return tup

    def return_workers_from_name(self, Wname):
        "SELECT column_name(s) FROM table_name LIMIT number"
        cur = self.key.cursor()
        sql = 'select * from workers where Wname=%s limit 1;'
        cur.execute(sql, (Wname))
        result = cur.fetchone()
        tup = []
        if result is not None:
            tup = [result[6], result[0], result[1], str(result[7]), result[8]]
        return tup

    def close(self):
        self.key.close()

    def add_worker(self, Wname, Wnum, Wsex, Wage, Wjointime, Wdepartment, Wimgpath, WnumberOfBreak, WnobTime):
        cur = self.key.cursor()
        sql = 'insert into workers(Wname,Wnum,Wsex,wage,Wjointime,Wdepartment,Wimgpath,WnumberOfBreak,WnobTime)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        data = [(Wname, Wnum, Wsex, Wage, Wjointime, Wdepartment, Wimgpath, WnumberOfBreak, WnobTime)]
        cur.executemany(sql, data)
        self.key.commit()

    # 个人认为127，129和130行代码可为
    # def add_worker(self,Wname,Wnum,Wsex,Wage,Wjointime,Wdepartment,Wimgpath):
    # sql = 'insert into workers(Wname,Wnum,Wsex,wage,Wjointime,Wdepartment,Wimgpath,WnumberOfBreak,WnobTime)values(%s,%s,%s,%s,%s,%s,%s)'
    # data = [(Wname , Wnum , Wsex , Wage , Wjointime , Wdepartment , Wimgpath)]
    # 即工人违规次数和违规时间不应人工添加，由数据库默认设置即可
    # 九个参数，为数据库工人信息表增加新信息
    def delete_worker(self, Wnum):
        cur = self.key.cursor()
        sql = 'delete from workers where Wnum=%s'
        cur.execute(sql, [Wnum])
        self.key.commit()

    # 按学号删除工人信息表数据
    # =========修改工人的犯规记录============
    def change_workers(self, Wnum):
        cur = self.key.cursor()
        sql = 'select * from workers where Wnum=%s;'
        cur.execute(sql, [Wnum])
        result = cur.fetchone()
        if result == None:
            return None
        else:
            WnumberOfBreak = result[7]
            WnobTime = result[8]
            print("工号为{0}的工人的记录违规次数为{1}，记录违规时间为{2}".format(Wnum, result[7], result[8]))
            WnumberOfBreak = input("请输入新的违规次数")
            WnobTime = input("请输入新的违规时间")
            sql = 'update workers set WnumberOfBreak=%s where Wnum=%s'
            data = (WnumberOfBreak, Wnum)
            cur.execute(sql, data)
            sql = 'update workers set WnobTime=%s where Wnum=%s'
            data = (WnobTime, Wnum)
            cur.execute(sql, data)
            self.key.commit()

    # ======通过工号返回id_card地址，姓名======
    def return_id_name(self,Wnum):
        cur = self.key.cursor()
        sql = 'select * from workers where Wnum=%s;'
        cur.execute(sql, (Wnum))
        result = cur.fetchone()
        #      姓名(字符串)      地址（字符串）
        tup = (result[0], result[6])
        return tup
    def change_time(self, timestr):
        # 功能：给add_DateInfo和return_DateInfo内部调用
        # 参数：timestr（时分秒[格式：12:55:25）
        # 返回值：换算成分钟的int形式
        hour = timestr[0] + timestr[1]
        hour = list(map(int, hour))
        minute = timestr[3] + timestr[4]
        minute = list(map(int, minute))
        return hour[0] * 10 * 60 + hour[1] * 60 + minute[0] * 10 + minute[1]

    def add_DateInfo(self, Dname, Dnum, DtimeOfdate, DPointOfTime):
        # 功能：将人脸比对之后的个人信息以及时间添加到记录表（DateInfo）中
        # 参数：（Dname, Dnum, DtimeOfdate, DPointOfTime)--》(姓名，编号，年月日[格式：2020-03-12] ，时分秒[格式：12:55:25])
        # 返回值：魔幻
        cur = self.key.cursor()
        sql = 'select * from DateInfo where Dnum=%s;'
        cur.execute(sql, [Dnum])
        results = cur.fetchall()
        # 得到最新的一条
        result = results[len(results) - 1]
        DB_DtimeOfdate = result[2] # 数据库返回最新一条的年月日如：“2020-05-05“

        print(DB_DtimeOfdate)
        if (result[0] == Dname):
            if((self.change_time(DPointOfTime) - self.change_time(str(result[3])) <= 30) and (str(DB_DtimeOfdate) == str(DtimeOfdate))):
                print("该员工仍在警示期")
                return 0
            else:
                sql = 'insert into DateInfo(Dname,Dnum,DtimeOfdate,DPointOfTime)value(%s,%s,%s,%s)'
                data = [(Dname, Dnum, DtimeOfdate, DPointOfTime)]
                cur.executemany(sql, data)
                self.key.commit()
                return 1
        else:
            print("工人名字和工号不匹配,请重新输入！")
            return -1



    def return_DateInfo(self, DtimeOfdate):
        # 功能：返回当天 如“2020-03-03” 所有记录。
        # 参数：DtimeOfdate须有年份，且有严格格式要求即全部为YYYY-MM-DD或全部为YYYY.MM.DD
        # 返回值：(Dname,Dnum,DtimeOfdate,DPointOfTime)--》（工号，姓名 违规日期 违规时间）
        cur = self.key.cursor()
        sql = 'select * from DateInfo where DtimeOfdate=%s;'
        cur.execute(sql, [DtimeOfdate])
        return cur.fetchall()

    def update_workers_and_DateInfo(self, Dname, Dnum, DtimeOfdate, DPointOfTime):
        # 功能：同时更新Workers和DateInfo两个数据表
        # 参数：（Dname, Dnum, DtimeOfdate, DPointOfTime)--》(姓名，编号，年月日[格式：2020-03-12] ，时分秒[格式：12:55:25])
        # 返回：flag: 1需要提醒，0已经提醒过，-1输入参数不正确
        flag = self.add_DateInfo(Dname, Dnum, DtimeOfdate, DPointOfTime)
        NewTime = str(DtimeOfdate) +" "+str(DPointOfTime)
        if flag == 1:
            self.update_workers(Dnum, NewTime)
        return flag



if __name__ == '__main__':
    # key=connect_wxremit_db()   #key为登录数据库钥匙
    # # 显示工人基本信息函数
    # print_data_workers(key)
    # # 显示一时间为顺序的函数
    # print_data_info(key)
    # # 添加info的函数
    # add_info(key, "2020-03-12 17:55:25", "C:\\Users\\ASUS\\Pictures\\4.png", 5, 0)
    # # 更新工人的犯罪记录
    # change_workers(key, '20200303004', '2020.03.23')
    # # 通过时间戳得到info记录
    # print(return_Info(key, '2020-03-12 12:55:25'))
    # # 通过工号得到工人的信息
    # print(return_workers(key, '20200303001'))
    # key.close()
    db = SQL_Y()
    # ====[√]测试print===
    # db.print_data_info()
    # ====[√]测试更新犯罪数据=====
    # db.print_data_workers()
    # db.change_workers('20200303001', '20200430')
    # db.print_data_workers()
    # =====[√]测试info=====
    # db.print_data_info()
    # db.add_info("2020-04-30 17:55:25", "C:\\U\\S\\Pictures\\3.png", 2, 3)
    # db.print_data_info()
    # ==[]工号查询===
    # Q: return_workers返回不正确：(1, ' , 20200430')
    # Wname  Wnum        Wsex Wage  Wjointime   Wdepartment          Wimgpath                WnumberOfBreak      WnobTime
    # 显示： 李明   20200303001 男   22    2020-03-04   运输部   C:\Users\ASUS\Pictures\1.png       1           ,  20200430
    # TODO: WnobTime存入不正确," , 20200430"
    # print(db.return_workers('20200303001'))
    # print(db.return_Info('2020-04-30 17:55:25'))
    # db.print_data_workers()
    # db.change_workers('20200303005','2020.03.03')
    # db.change_workers ( '20200303005' , '2020.03.03 19:26:52' )
    # db.change_workers('20200303005')
    # db.print_data_workers()Wname, Wnum, Wsex, Wage, Wjointime, Wdepartment, Wimgpath, WnumberOfBreak, WnobTime
    # db.add_worker("李王", "20200303004", "男", "22", "2020-03-04", "运输部", "C:\\Users\\ASUS\\Pictures\\1.png", "1", "")
    db.update_workers_and_DateInfo('李王', '20200303004', '2020-05-05', '19:00:25')
    # db.add_DateInfo('李王', '20200303004', '2020-03-03', '12:55:25')
    # db.add_DateInfo('xx', '20200303004', '2020-03-03', '16:55:25')
    results = db.return_DateInfo('2020-05-05')
    for row in results:
        print(row[0] + " " + row[1] + " " + str(row[2]) + " " + str(row[3]))
