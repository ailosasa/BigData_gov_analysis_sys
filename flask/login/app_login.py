#!/usr/bin/env python
# coding: utf-8
# In[4]:
import USQL
import hashlib
import os
# In[5]:
#一些宏名定义
NotLOGIN = False
HaveLOGIN = True
FORMATERROR = -1
STANDBY = 0
nSUCCESSLOGIN = 1
aSUCCESSLOGIN = 2
PAIRERROR = 3

NAMEERROR = 4
PASSWORDERROR = 5
NAMEEXIST = 6
SUCCESSREGIST = 7

# In[6]:
def md5str(s):
    #对传入的字符串进行MD5加密，返回加密后字符串
    MD5 = hashlib.md5()
    MD5.update(s.encode())
    return str(MD5.hexdigest())

# In[7]:

def regist_account(name,password,Hash,a):

    Hash.add(name,md5str(password))                 #缓存添加

    #RHash.WHash(name,md5str(password),Hash.num,a)   #本地添加
    



# In[21]:


class app_login(object):
    #用于进行登陆验证和创建新账号的对象
    def __init__(self,a):
        #初始化为未登录状态
        self.iflogin = NotLOGIN

    def regist(self,regist_name,regist_password,a):
        #对象中的注册方法

        #分别向表和本地文件中添加新帐户
        if(USQL.add(regist_name,regist_password)):
            Udata_fo = open("accounts_raw.txt","a")
            Udata_fo.writelines([regist_name,'\n'])
            Udata_fo.writelines([regist_password,'\n'])

            #向本地添加文档
            '''os.mkdir("Account_Info/"+regist_name)
            num_fo = open("Account_Info/"+regist_name+"/"+regist_name+"_List_num.py","a")
            num_fo.writelines(["0","\n"])
            num_fo.close()
            data_fo = open("Account_Info/"+regist_name+"/"+regist_name+"_List_data.py","a")
            data_fo.close()'''
            print("新账户已添加")
            return SUCCESSREGIST
                            
    def login(self,login_name,login_password,a):
        #用于验证登陆的方法

        #匹配
        if(USQL.searchP(login_name,login_password)):
            #登陆成功
            self.iflogin = HaveLOGIN
            if(a):
                print("管理员验证通过")
                return aSUCCESSLOGIN
            else:
                print("普通用户验证通过")
                return nSUCCESSLOGIN
        else:
            #
            print("用户名密码不匹配")
            return PAIRERROR
