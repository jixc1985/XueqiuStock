import pymysql
import pandas as pd
import os
from multiprocessing.dummy import Pool as ThreadPool

def importLRB(filename):
    # 使用cursor()方法获取操作游标
    db = pymysql.connect(host="localhost", user="root", password="7z5#UiWysZwA", db="xueqiustock", port=3306,
                         charset='utf8')
    cursor = db.cursor()
    #读取csv
    df = pd.read_csv(filename, encoding="uts-8")

    # 将dt数据插入数据库表
    for row in df.iterrows():
        try:
            cursor.execute(
                "insert into t_lrb(code,date,yyzsr,yyzcb,xsfy,glfy,cwfy,yylr,yywsr,yywzc,lrze,sdsfy,jlr) "\
                "values('%s','%s','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f')"
                % (list, str(int(row[1][1])), float(row[1][2]), float(row[1][22]), float(row[1][22]), float(row[1][22]), float(row[1][22]), float(row[1][22]), float(row[1][22]), float(row[1][22]), float(row[1][22]), float(row[1][22]), float(row[1][22])))

            db.commit()
        except Exception as e:
            db.rollback()
            print(list + "出错在位置" + str(i))
            print(e)

    print(list + '利润表完成,共插入记录' + str(i) + '条')
    i = 0

    print('共插入' + str(num) + '条记录')
    db.close()

def startImport():
    rootdir = "C:/Users/Administrator/PycharmProjects/XueqiuStock/crawl/stocks"
    dirlist =  os.listdir(rootdir)
    filelist = []
    for code in dirlist:
        file = rootdir + '/' + code + '/lrb.csv'
        filelist.append(file)

    pool = ThreadPool(10)
    pool.map(importLRB(), filelist)
    pool.close()
    pool.join()

startImport()