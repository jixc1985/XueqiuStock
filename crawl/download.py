
# coding: utf-8

import requests
import os
import pymysql
from multiprocessing.dummy import Pool as ThreadPool
import json


headers = {
    'User-Agent': 'Mozilla/5.0',
    'Cookie': 'xq_a_token=5c915d14d91dc74b5f2e4c3b4753137ae66c1926'
}

#下载利润表
def download_lrb(url):
    r = requests.get(url, headers=headers)
    filename = 'stocks/' + url.split('=')[-1] + '/lrb.csv'
    #print(filename)
    db = pymysql.connect(host="localhost", user="root", password="7z5#UiWysZwA", db="xueqiustock", port=3306,
                         charset='utf8')

    #if not os.path.exists('stocks/' + url.split('=')[-1]):
        #os.mkdir('stocks/' + url.split('=')[-1])
    # with open(filename, 'wb') as f:
    # f.write(r.content)
    #将json转换成dict
    json_response = r.content.decode()
    dict_json = json.loads(json_response)
    cursor = db.cursor()
    #读取list中的记录
    i = 0
    for item in dict_json.get('list'):
        #print(url.split('=')[-1],str(int(item.get('enddate'))),float(0 if item.get('biztotinco') is None else item.get('biztotinco')),float(0 if item.get('biztotcost') is None else item.get('biztotcost')),float(0 if item.get('salesexpe') is None else item.get('salesexpe')),float(0 if item.get('manaexpe') is None else item.get('manaexpe')),float(0 if item.get('finexpe') is None else item.get('finexpe')),float(0 if item.get('perprofit') is None else item.get('perprofit')),float(0 if item.get('nonoreve') is None else item.get('nonoreve')),float(0 if item.get('nonoexpe') is None else item.get('nonoexpe')),float(0 if item.get('totprofit') is None else item.get('totprofit')),float(0 if item.get('incotaxexpe') is None else item.get('incotaxexpe')),float(0 if item.get('netprofit') is None else item.get('netprofit')))
        try:
            cursor.execute(
                "insert into t_lrb(code,date,yyzsr,yyzcb,xsfy,glfy,cwfy,yylr,yywsr,yywzc,lrze,sdsfy,jlr) " \
                "values('%s','%s','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f')"
                % (url.split('=')[-1], str(int(item.get('enddate'))),float(0 if item.get('biztotinco') is None else item.get('biztotinco')),
                   float(0 if item.get('biztotcost') is None else item.get('biztotcost')),float(0 if item.get('salesexpe') is None else item.get('salesexpe')),
                   float(0 if item.get('manaexpe') is None else item.get('manaexpe')),float(0 if item.get('finexpe') is None else item.get('finexpe')),
                   float(0 if item.get('perprofit') is None else item.get('perprofit')),float(0 if item.get('nonoreve') is None else item.get('nonoreve')),
                   float(0 if item.get('nonoexpe') is None else item.get('nonoexpe')),float(0 if item.get('totprofit') is None else item.get('totprofit')),
                   float(0 if item.get('incotaxexpe') is None else item.get('incotaxexpe')),float(0 if item.get('netprofit') is None else item.get('netprofit'))))
            db.commit()
            i += 1
        except Exception as e:
            db.rollback()
            print("出错在位置:" + url.split('=')[-1]  + '-' + item.get('enddate'))
            print(e)

    print(url.split('=')[-1] + '利润表完成,共插入记录' + str(i) + '条')

    db.close()


#下载资产负债表
def download_fzb(url):
    r = requests.get(url, headers=headers)
    filename = 'stocks/' + url.split('=')[-1] + '/zcfzb.csv'
    print(filename)
    if os.path.exists('stocks/' + url.split('=')[-1]):
        os.mkdir('stocks/' + url.split('=')[-1])
    #with open(filename, 'wb') as f:
        #f.write(r.content)

#下载现金流量表
def download_llb(url):
    r = requests.get(url, headers=headers)
    filename = 'stocks/' + url.split('=')[-1] + '/xjllb.csv'
    print(filename)
    if not os.path.exists('stocks/' + url.split('=')[-1]):
        os.mkdir('stocks/' + url.split('=')[-1])
    #with open(filename, 'wb') as f:
        #f.write(r.content)


with open('symbol.txt', 'r', encoding='utf-8') as f:
    symbol = [s.strip() for s in f.readlines()]



# 获取下载地址列表
def getURLs():
    lrb_base_url = 'http://api.xueqiu.com/stock/f10/incstatement.json?page=1&size=10000&symbol='
    llb_base_url = 'http://api.xueqiu.com/stock/f10/cfstatement.json?page=1&size=10000&symbol='
    fzb_base_url = 'http://api.xueqiu.com/stock/f10/balsheet.json?page=1&size=10000&symbol='
    cwzb_base_url = 'https://api.xueqiu.com/stock/f10/finmainindex.json?page=1&size=10000&symbol='
    lrb_urls = [lrb_base_url + i for i in symbol]
    fzb_urls = [fzb_base_url + i for i in symbol]
    llb_urls = [llb_base_url + i for i in symbol]
    cwzb_urls = [cwzb_base_url + i for i in symbol]

    return [lrb_urls,fzb_urls,llb_urls]

#----------------------------------------------------------------------------
urls = getURLs()
pool = ThreadPool(10)
pool.map(download_lrb, urls[0])
pool.close()
'''
pool.join()
pool = ThreadPool(10)
pool.map(download_fzb, urls[1])
pool.close()
pool.join()
pool = ThreadPool(10)
pool.map(download_llb, urls[2])
pool.close()
pool.join()

'''