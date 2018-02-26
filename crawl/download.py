
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
    #filename = 'stocks/' + url.split('=')[-1] + '/lrb.csv'
    #print(filename)
    #if not os.path.exists('stocks/' + url.split('=')[-1]):
        #os.mkdir('stocks/' + url.split('=')[-1])
    # with open(filename, 'wb') as f:
    # f.write(r.content)

    #将json转换成dict
    r = requests.get(url, headers=headers)
    db = pymysql.connect(host="localhost", user="root", password="12345678", db="xueqiustock", port=3306,
                         charset='utf8')
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
                % (url.split('=')[-1],
                   str(int(item.get('enddate'))),
                   float(0 if item.get('biztotinco') is None else item.get('biztotinco')),
                   float(0 if item.get('biztotcost') is None else item.get('biztotcost')),
                   float(0 if item.get('salesexpe') is None else item.get('salesexpe')),
                   float(0 if item.get('manaexpe') is None else item.get('manaexpe')),
                   float(0 if item.get('finexpe') is None else item.get('finexpe')),
                   float(0 if item.get('perprofit') is None else item.get('perprofit')),
                   float(0 if item.get('nonoreve') is None else item.get('nonoreve')),
                   float(0 if item.get('nonoexpe') is None else item.get('nonoexpe')),
                   float(0 if item.get('totprofit') is None else item.get('totprofit')),
                   float(0 if item.get('incotaxexpe') is None else item.get('incotaxexpe')),
                   float(0 if item.get('netprofit') is None else item.get('netprofit'))))
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
    #filename = 'stocks/' + url.split('=')[-1] + '/zcfzb.csv'
    #print(filename)
    #if os.path.exists('stocks/' + url.split('=')[-1]):
        #os.mkdir('stocks/' + url.split('=')[-1])
    #with open(filename, 'wb') as f:
        #f.write(r.content)
    r = requests.get(url, headers=headers)
    db = pymysql.connect(host="localhost", user="root", password="12345678", db="xueqiustock", port=3306,
                         charset='utf8')
    json_response = r.content.decode()
    dict_json = json.loads(json_response)
    cursor = db.cursor()
    # 读取list中的记录
    i = 0
    for item in dict_json.get('list'):
        # print(url.split('=')[-1],str(int(item.get('enddate'))),float(0 if item.get('biztotinco') is None else item.get('biztotinco')),float(0 if item.get('biztotcost') is None else item.get('biztotcost')),float(0 if item.get('salesexpe') is None else item.get('salesexpe')),float(0 if item.get('manaexpe') is None else item.get('manaexpe')),float(0 if item.get('finexpe') is None else item.get('finexpe')),float(0 if item.get('perprofit') is None else item.get('perprofit')),float(0 if item.get('nonoreve') is None else item.get('nonoreve')),float(0 if item.get('nonoexpe') is None else item.get('nonoexpe')),float(0 if item.get('totprofit') is None else item.get('totprofit')),float(0 if item.get('incotaxexpe') is None else item.get('incotaxexpe')),float(0 if item.get('netprofit') is None else item.get('netprofit')))
        try:
            cursor.execute(
                "insert into t_zcfzb(code,date,hbzj,yspj,yszk,yfkx,ch,ldzchj,sy,cqdtfy,fldzchj,zczj,yfzk,yskx,ldfzhj,fzhj,sszb,syzqy) " \
                "values('%s','%s','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f')"
                % (url.split('=')[-1],
                   str(int(item.get('reportdate'))),
                   float(0 if item.get('curfds') is None else item.get('curfds')),
                   float(0 if item.get('notesrece') is None else item.get('notesrece')),
                   float(0 if item.get('accorece') is None else item.get('accorece')),
                   float(0 if item.get('prep') is None else item.get('prep')),
                   float(0 if item.get('inve') is None else item.get('inve')),
                   float(0 if item.get('totcurrasset') is None else item.get('totcurrasset')),
                   float(0 if item.get('goodwill') is None else item.get('goodwill')),
                   float(0 if item.get('logprepexpe') is None else item.get('logprepexpe')),
                   float(0 if item.get('totalnoncassets') is None else item.get('totalnoncassets')),
                   float(0 if item.get('totasset') is None else item.get('totasset')),
                   float(0 if item.get('accopaya') is None else item.get('accopaya')),
                   float(0 if item.get('advapaym') is None else item.get('advapaym')),
                   float(0 if item.get('totalcurrliab') is None else item.get('totalcurrliab')),
                   float(0 if item.get('totliab') is None else item.get('totliab')),
                   float(0 if item.get('paidincapi') is None else item.get('paidincapi')),
                   float(0 if item.get('righaggr') is None else item.get('righaggr'))))
            db.commit()
            i += 1
        except Exception as e:
            db.rollback()
            print("出错在位置:" + url.split('=')[-1] + '-' + item.get('reportdate'))
            print(e)

    print(url.split('=')[-1] + '负债表完成,共插入记录' + str(i) + '条')



#下载主要财务指标
def download_cwzb(url):
    r = requests.get(url, headers=headers)
    db = pymysql.connect(host="localhost", user="root", password="12345678", db="xueqiustock", port=3306,
                         charset='utf8')
    json_response = r.content.decode()
    dict_json = json.loads(json_response)
    cursor = db.cursor()
# 读取list中的记录
    i = 0
    for item in dict_json.get('list'):
        # print(url.split('=')[-1],str(int(item.get('enddate'))),float(0 if item.get('biztotinco') is None else item.get('biztotinco')),float(0 if item.get('biztotcost') is None else item.get('biztotcost')),float(0 if item.get('salesexpe') is None else item.get('salesexpe')),float(0 if item.get('manaexpe') is None else item.get('manaexpe')),float(0 if item.get('finexpe') is None else item.get('finexpe')),float(0 if item.get('perprofit') is None else item.get('perprofit')),float(0 if item.get('nonoreve') is None else item.get('nonoreve')),float(0 if item.get('nonoexpe') is None else item.get('nonoexpe')),float(0 if item.get('totprofit') is None else item.get('totprofit')),float(0 if item.get('incotaxexpe') is None else item.get('incotaxexpe')),float(0 if item.get('netprofit') is None else item.get('netprofit')))
        try:
            cursor.execute(
                "insert into t_cwzb(code,date,basiceps,naps,opercashpershare,peropecashpershare,netassgrowrate,weightedroe,dilutedroe,mainbusincgrowrate,netincgrowrate,totassgrowrate,salegrossprofitrto,mainbusiincome,mainbusiprofit,totprofit,netprofit,totalassets,totalliab,totsharequi,operrevenue,invnetcashflow,finnetcflow) " \
                "values('%s','%s','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f','%f')"
                % (url.split('=')[-1],
                   str(int(item.get('reportdate'))),
                   float(0 if item.get('basiceps') is None else item.get('basiceps')),
                   float(0 if item.get('naps') is None else item.get('naps')),
                   float(0 if item.get('opercashpershare') is None else item.get('opercashpershare')),
                   float(0 if item.get('peropecashpershare') is None else item.get('peropecashpershare')),
                   float(0 if item.get('weightedroe') is None else item.get('weightedroe')),
                   float(0 if item.get('netassgrowrate') is None else item.get('netassgrowrate')),
                   float(0 if item.get('dilutedroe') is None else item.get('dilutedroe')),
                   float(0 if item.get('mainbusincgrowrate') is None else item.get('mainbusincgrowrate')),
                   float(0 if item.get('netincgrowrate') is None else item.get('netincgrowrate')),
                   float(0 if item.get('totassgrowrate') is None else item.get('totassgrowrate')),
                   float(0 if item.get('salegrossprofitrto') is None else item.get('salegrossprofitrto')),
                   float(0 if item.get('mainbusiincome') is None else item.get('mainbusiincome')),
                   float(0 if item.get('mainbusiprofit') is None else item.get('mainbusiprofit')),
                   float(0 if item.get('totprofit') is None else item.get('totprofit')),
                   float(0 if item.get('netprofit') is None else item.get('netprofit')),
                   float(0 if item.get('totalassets') is None else item.get('totalassets')),
                   float(0 if item.get('totalliab') is None else item.get('totalliab')),
                   float(0 if item.get('totsharequi') is None else item.get('totsharequi')),
                   float(0 if item.get('operrevenue') is None else item.get('operrevenue')),
                   float(0 if item.get('invnetcashflow') is None else item.get('invnetcashflow')),
                   float(0 if item.get('finnetcflow') is None else item.get('finnetcflow'))))
            db.commit()
            i += 1
        except Exception as e:
            db.rollback()
            print("出错在位置:" + url.split('=')[-1] + '-' + item.get('reportdate'))
            print(e)

    print(url.split('=')[-1] + '财务指标完成,共插入记录' + str(i) + '条')

# 获取下载地址列表
def getURLs():
    lrb_base_url = 'http://api.xueqiu.com/stock/f10/incstatement.json?page=1&size=10000&symbol='
    fzb_base_url = 'http://api.xueqiu.com/stock/f10/balsheet.json?page=1&size=10000&symbol='
    #llb_base_url = 'http://api.xueqiu.com/stock/f10/cfstatement.json?page=1&size=10000&symbol='
    cwzb_base_url = 'https://api.xueqiu.com/stock/f10/finmainindex.json?page=1&size=10000&symbol='
    with open('symbol.txt', 'r', encoding='utf-8') as f:
        symbol = [s.strip() for s in f.readlines()]
    lrb_urls = [lrb_base_url + i for i in symbol]
    fzb_urls = [fzb_base_url + i for i in symbol]
    #llb_urls = [llb_base_url + i for i in symbol]
    cwzb_urls = [cwzb_base_url + i for i in symbol]

    return [lrb_urls,fzb_urls,cwzb_urls]

#----------------------------------------------------------------------------

urls = getURLs()
'''
pool = ThreadPool(10)
pool.map(download_lrb, urls[0])
pool.close()
pool.join()
'''


'''
pool = ThreadPool(10)
pool.map(download_fzb, urls[1])
pool.close()
pool.join()
'''
pool = ThreadPool(10)
pool.map(download_cwzb, urls[2])
pool.close()
pool.join()

