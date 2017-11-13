# coding:utf-8
"""
Created on 2017/11/04
@author: weijia
"""
dbinfo = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'pwd': 'yanweijia',
    'db': 'stock',
    'encoding': 'utf8',
    'mincached': 1,
    'maxcached': 20,
    'use_unicode':True
}
# http请求头
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 's=fq12j9bjw5; device_id=9d599aed6cb8bcc65d6d18c81687571d; __utma=1.1712410977.1509432617.1509865950.1509882723.11; __utmz=1.1509432617.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); aliyungf_tc=AQAAAFoGejBxewwAIPihtH84XjzOZGUn; xq_a_token=6708d101a456578c98ea1779ae898687fe465bcb; xq_a_token.sig=ESOIvUPuIgPljw2oVadQTbSmYos; xq_r_token=0cbb786896425c8f2a853545bade9309fbc75601; xq_r_token.sig=SBPl2y3rvUjypwJrgx4MSiUpxWw; u=171510160456439; Hm_lvt_1db88642e346389874251b5a1eded6e3=1509432617,1509533177,1510160458; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1510160458',
    'Host': 'xueqiu.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}