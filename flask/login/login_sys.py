#!/usr/bin/env python
# coding: utf-8
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


USQL.load()
def check(sele,name,password):
    # connector.getAccount(name,password)
    # login_verify.login(name,password)
    a = 0
    if name == '' or password == '' or len(name)>20 or len(password)>32:
        print("Format Error!\n")
        status = FORMATERROR
        print("status=",status)
        return FORMATERROR
    elif name[0] == 'a':
            a = 1
    applogin = app_login.app_login(a)

    if sele == 1:
        status = applogin.login(name, password, a)
        print("status=",status)

    elif sele == 2:
        status = applogin.regist(name, password, a)
        print("status=",status)

    return -2
