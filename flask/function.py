#!/usr/bin/python
# -*- coding: UTF-8 -*-
import data
def fun1(datas):
    result = {'求决':0,'投诉':0,'咨询':0,'建议':0,'感谢':0,'其他':0}
    for ser in datas:
        if ser[23] == 1:
            result['求决']+=1
        elif ser[23] == 2:
            result['投诉']+=1
        elif ser[23] == 3:
            result['咨询']+=1
        elif ser[23] == 4:
            result['建议']+=1
        elif ser[23] == 5:
            result['感谢']+=1
        else:
            result['其他'] += 1
    for items in result:
        if (len(datas)==0):
            return {}
        result[items] = str(result[items] / len(datas) * 100)
    return result
def fun2(datas):
    result = {}
    for ser in datas:
        if ser[5] in result:
            if ser[11] in result[ser[5]]:
                result[ser[5]][ser[11]] += 1
            else:
                result[ser[5]][ser[11]] = 1
        else:
            result[ser[5]]={ser[11]:1}
    return  result
def fun3(datas):
    result = {}
    for ser in datas:
        if ser[7] in result:
            result[ser[7]] += 1
        else:
            result[ser[7]] = 1
    return result
def fun4(datas):
    result = {'处置中':{},'超期结办':{},'按期结办':{}}
    a = 0
    b = 0
    c = 0
    for ser in datas:
        if ser[21] == 1:
            if ser[9] in result['处置中']:
                result['处置中'][ser[9]] += 1
            else:
                result['处置中'][ser[9]] = 1
            a=a+1
        elif ser[20] == 1:
            if ser[9] in result['超期结办']:
                result['超期结办'][ser[9]] += 1
            else:
                result['超期结办'][ser[9]] = 1
            b=b+1
        elif ser[22] == 1:
            if ser[9] in result['按期结办']:
                result['按期结办'][ser[9]] += 1
            else:
                result['按期结办'][ser[9]] = 1
            c = c+1
    for items in result:
        lens = 0
        for item in result[items]:
            lens = result[items][item]+lens
        for item in result[items]:
            result[items][item] = str(result[items][item]/lens*100)
    d = len(datas)
    if d==0:
        return {}
    result['处置中'] = [str(a/d*100),result['处置中']]
    result['超期结办'] = [str(b/d*100), result['超期结办']]
    result['按期结办'] = [str(c/d*100), result['按期结办']]
    return result
def fun5(datas):
    datas=bubbleSort(datas)
    result=[]
    for data in  datas:
        result.append([data[2],data[5],data[7],data[17],data[24],data[15]])
    return  result

def bubbleSort(arr):
    n = len(arr)
    import datetime
    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if (arr[j][2]-arr[j+1][2])>=datetime.timedelta(seconds=1):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return  arr

def fun(fnum,time1,time2):

    if fnum == "反馈统计":
        result = fun1(data.search(time1,time2))
    elif fnum == "社区事件统计":
        result = fun2(data.search(time1, time2))
    elif fnum == "热点社区":
        result = fun3(data.search(time1, time2))
    elif fnum == "事件及处理":
        result = fun4(data.search(time1, time2))
    elif fnum == 5:
        import datetime
        time2=str(datetime.datetime.now().replace(year=2018,month=10,day=30,microsecond=0))
        time1='2018-10-30 00:00:00'
        result = fun5(data.search(time1, time2))
    return result
