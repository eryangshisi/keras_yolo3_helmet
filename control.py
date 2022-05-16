import pymysql

# ===========完善部分==========
# 1.添加主键时候冲突的处理办法
#

# =====数据库登录=====
def connect_wxremit_db():
    # yangyu123Q1W2E3
    pwd = input("请输入密码：")
    conn = pymysql.connect(host="localhost", user="root", password=pwd, port=3306, database="HafetyHelmet", charset="utf8")
    cursor = conn.cursor()        #获取一个光标，等待输入SQL语句
    sql = 'select * from workers'
    ret = cursor.execute(sql)
    cursor.close()
    if ret:
        print("登录成功！")
    else:
        print("登录失败！")
    return conn

def print_data_workers(key):  #显示workersconn=key
    cur = key.cursor()
    sql = "select * from workers"
    try:
        cur.execute(sql)
        results = cur.fetchall()
        print("Wname"," Wnum  ","     Wsex","Wage ","Wjointime  ","Wdepartment ","Wimgpath                ","WnumberOfBreak   ","WnobTime")
        for row in results:
            Wname=row[0]
            Wnum=row[1]
            Wsex=row[2]
            Wage=row[3]
            Wjointime=row[4]
            Wdepartment=row[5]
            Wimgpath=row[6]
            WnumberOfBreak=row[7]         #违规时间
            WnobTime=row[8]              #违规时间戳
            print(Wname," ",Wnum,Wsex," ",Wage,"  ",Wjointime," ",Wdepartment," ",Wimgpath,"     ",WnumberOfBreak,"         ",WnobTime)
    except Exception as e:
        raise e
'''显示工人表中所有信息'''

def print_data_info(key):  #显示info
    cur = key.cursor()
    sql = "select * from Info"
    try:
        cur.execute(sql)
        results=cur.fetchall()
        print("infotime            ","imgpath                ","      带安全帽人数","未带安全帽人数")
        for row in results:
            Info=row[0]
            Imgpath=row[1]
            Iwearer=row[2]
            Iunwearer=row[3]
            print(Info,' ',Imgpath,'    ',Iwearer,'    ','     ',Iunwearer)
    except Exception as e:
        raise e

def add_info(key, Info, Imgpath, Iwearer, Iunwerer):
    cur = key.cursor ()
    sql='insert into Info(Info,Imgpath,Iwearer,Iunwearer)value(%s,%s,%s,%s);'
    data=[(Info,Imgpath,Iwearer,Iunwerer)]
    cur.executemany(sql,data)
    key.commit()
# def xxx(时间戳,字符串类型的文件名地址, 佩戴人数, 未佩戴人数):
#    功能:存入时间戳表
#    对于字符串类型的文件名地址，如C:\\Users\\ASUS\\Pictures\\4.png，在数据库中存时，会将双斜杠变为当斜杠，即通过数据库可视化工具
#    查看数据库时效果为C:\Users\ASUS\Pictures\4.png 返回的字符串为C:\\Users\\ASUS\\Pictures\\4.png
#    当然如果你存时就为C:\Users\ASUS\Pictures\4.png，那么效果为C:UsersASUSPictures4.png，返回的字符串为C:\Users\ASUS\Pictures\4.png


def change_workers(key,Wnum,NewTime):
    cur=key.cursor()
    sql = 'select * from workers where Wnum=%s;'
    cur.execute(sql,[Wnum])
    result = cur.fetchone ()
    if result==None:
        return ;
    else:
        WnumberOfBreak=result[7]
        WnobTime=result[8]
        WnumberOfBreak=WnumberOfBreak+1
        if WnobTime==None:
            WnobTime = NewTime
        else:
            WnobTime=WnobTime+' , '+NewTime
        sql='update workers set WnumberOfBreak=%s where Wnum=%s'
        data=(WnumberOfBreak,Wnum)
        cur.execute(sql,data)
        sql = 'update workers set WnobTime=%s where Wnum=%s'
        data = (WnobTime,Wnum)
        cur.execute(sql,data)
        key.commit();
#通过工号，匹配后，更新违规信息，包括增加时间戳和违规次数

def return_Info(key,Info):
    cur=key.cursor()
    sql='select * from info where Info=%s;'
    cur.execute(sql,[Info])
    return cur.fetchone()
'''def xx取(时间戳):
	“返回值类型：”
	xxx
	return 字符串 文件名, 佩戴人数, 未佩戴人数(元组形式)
'''
def return_workers(key,Wnum):
    cur = key.cursor ()
    sql = 'select * from workers where Wnum=%s;'
    cur.execute(sql,(Wnum))
    result=cur.fetchone()
    tup=(result[7],result[8])
    return tup
'''def xx取(工号)：
	return 违规次数，违规对应时间戳…(返回值为元组形式)'''

if __name__ == '__main__':
    key=connect_wxremit_db()   #key为登录数据库钥匙
    # 显示工人基本信息函数
    print_data_workers(key)
    # 显示一时间为顺序的函数
    print_data_info(key)
    # 添加info的函数
    add_info(key, "2020-03-12 17:55:25", "C:\\Users\\ASUS\\Pictures\\4.png", 5, 0)
    # 更新工人的犯罪记录
    change_workers(key, '20200303004', '2020.03.23')
    # 通过时间戳得到info记录
    print(return_Info(key, '2020-03-12 12:55:25'))
    # 通过工号得到工人的信息
    print(return_workers(key, '20200303001'))
    key.close()
