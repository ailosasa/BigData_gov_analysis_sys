# coding: utf-8
""" 

"""
import pymysql
import hashlib


db = pymysql.connect("10.249.86.29", "root", "root", "govdata", charset='utf8')

def md5str(s):
    #对传入的字符串进行MD5加密，返回加密后字符串
    MD5 = hashlib.md5()
    MD5.update(s.encode())
    return str(MD5.hexdigest())
 
def load():

    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS user_table")

    sql = """CREATE TABLE user_table (
                `ID` VARCHAR(20) NOT NULL,
                `password` VARCHAR(32) NOT NULL,
                `Hashpswd` VARCHAR(32) NOT NULL,
            PRIMARY KEY(ID))
            """
    cursor.execute(sql)

    acct_fo = open("accounts_raw.txt", 'r')
    accts = acct_fo.readlines()
    Unum = int(len(accts)/2)
    j = 0
    ID = []; pw = []; Hpw = []

    for i in range(Unum):                 #截取账户名、密码录入数据库
        ID.append(accts[j].strip('\n'))
        #print(ID)
        pw.append(accts[j+1].strip('\n'))
        Hpw.append(md5str(pw[i]))
        sql = "INSERT INTO `user_table`(\
            `ID` ,\
            `password`,\
            `Hashpswd` \
            ) VALUES ('%s','%s','%s')" \
          % (ID[i], pw[i], Hpw[i])
        try:
            cursor.execute(sql)
            db.commit()
        except:
            print('Fail to load.')
            db.rollback()
        j += 2

def searchP(ID,pw):
    cursor = db.cursor()
    sql = "SELECT * FROM user_table WHERE \
            ID='%s' AND password='%s'" \
            % (ID,pw)
    try:
        cursor.execute(sql)
        rs = cursor.fetchall()
        if len(rs) == 1:
            return True
    finally:
        cursor.close()
    return False

def searchID(ID):
    cursor = db.cursor()
    sql = "SELECT * FROM user_table WHERE \
            ID='%s'" \
            % (ID)
    try:
        cursor.execute(sql)
        rs = cursor.fetchall()
        if len(rs) == 1:
            return True
    finally:
        cursor.close()
    return False


def add(ID,pw):
    cursor = db.cursor()
    Hpw = md5str(pw)
    sql = "INSERT INTO user_table ( \
            ID, password, Hashpswd) VALUES ('%s','%s','%s')" \
            % (ID,pw,Hpw)
    try:
        cursor.execute(sql)
        db.commit()
        if cursor.rowcount == 1:
            return True
    except:
        print('Fail to add.(username exists)')
        db.rollback()
    finally:
        cursor.close()
    return False