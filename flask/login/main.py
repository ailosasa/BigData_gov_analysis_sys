# coding: utf-8

import login_sys
import pymysql
import app_login
import USQL

FORMATERROR = -1
STANDBY = 0
nSUCCESSLOGIN = 1
aSUCCESSLOGIN = 2
PAIRERROR = 3

NAMEERROR = 4
PASSWORDERROR = 5
NAMEEXIST = 6
SUCCESSREGIST = 7

statusL = []
status = STANDBY

USQL.load()
# 测试段
sele = int(input("choise:1.login 2.register 0.exit  "))
while sele != 0:
    name = input('name:')
    password = input('password:')
    status = login_sys.check(sele, name, password)
    sele = int(input("choise:1.login 2.register 0.exit  "))


