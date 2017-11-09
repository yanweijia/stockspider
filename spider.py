# -*- coding:utf-8 -*-

# 参考:
# Python-第三方库requests详解  http://blog.csdn.net/shanzhizi/article/details/50903748


import requests, threading, json, logging, sys, getopt, warnings
import save_util

warnings.filterwarnings("ignore")  # 忽略警告信息的提示

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


def spider_company(symbol_prefix='SH', start_code=000000, end_code=999999, clean_db=False, verify_website=False):
    """
    抓取上市公司信息,对应股票代码来抓取

    :param symbol_prefix: 股票代码前缀,分类
    :param start_code: 开始爬虫的股票代码
    :param end_code: 结束爬虫的股票代码
    :param clean_db: 是否清空数据库并重新建表
    :param verify_website: 是否验证 https 网站
    :return:
    """
    if clean_db:
        save_util.create_and_clear_table()  # 创建表并清空相关表信息
    for i in range(start_code, end_code, 1):
        symbol = symbol_prefix + str(i).zfill(6)
        params = {'symbol': symbol}
        try:
            res = requests.get("https://xueqiu.com/stock/f10/compinfo.json", params=params, headers=headers,
                               timeout=10000,
                               verify=verify_website)
            if res.status_code == 200:
                tqCompInfo = json.loads(res.content, encoding='utf-8')['tqCompInfo']
                if tqCompInfo is None:
                    print '无此编号:' + symbol
                else:
                    save_util.save_stock_compinfo(symbol, tqCompInfo)
                    print '成功下载编号为: ', symbol, ' 的股票信息'
            else:
                print "下载错误,download fail, http response code is:" + res.status_code
                print res.headers
                print res
                break
        except BaseException, arguement:
            print "爬取失败: ", str(arguement)


def print_help():
    print ' stock_spider 使用方法:'
    print ' 参数说明:'
    print '\t --type 爬取种类, companyinfo 为公司信息(默认),stockhistory 为股票历史数据, stockrealtime 为股票实时数据'
    print '\t --symbol=SH 为上证,SZ为深证,默认SH'
    print '\t -s 股票区间开始代码,默认000000,这里从600000开始爬取'
    print '\t -e 股票区间结束代码,默认999999,这里到600299结束'
    print '\t -c 是否删除并清空所有数据表重建,默认 False'
    print '\t -v 是否验证https链接,默认False'
    print '\t --code=600148  爬取SH600148的信息,仅爬取当前股票,会忽略-s -e 参数'
    print ' 爬取公司信息:'
    print '\t python spider.py --type=companyinfo --symbol=SH -s 600000 -e 602999 -c False -v True'
    print ' 爬取股票历史信息:'
    print '\t python spider.py --type=stockhistory --symbol=SH --code=600148 -c False -v True'
    print '\t 或 python spider.py --type=stockhistory --symbol=SH -s 600000 -e 600299 -c False -v True'
    print ' 爬取股票实时信息:'
    print '\t python spider.py --type=stockrealtime --symbol=SH --code=600148 -c False -v True'
    print '\t 或 python spider.py --type=stockrealtime --symbol=SH -s 600000 -e 600299 -c False -v True'


if __name__ == '__main__':
    # 预定义值:
    spider_type = 'companyinfo'
    symbol_prefix = 'SH'
    start_code = 000000
    end_code = 999999
    clean_db = False
    verify_website = False
    # 参考:Python 获得命令行参数的方法  http://www.cnblogs.com/saiwa/articles/5253713.html
    opts, args = getopt.getopt(sys.argv[1:], "s:e:c:v:", ["help", "type=", "symbol="])
    for op, value in opts:
        if op == "--type":
            spider_type = value
        elif op == "--symbol":
            symbol_prefix = value
        elif op == "--help":
            print_help()
            sys.exit(0)
        elif op == "-s":
            start_code = int(value)
        elif op == "-e":
            end_code = int(value)
        elif op == "-c":
            clean_db = bool(value)
        elif op == "-v":
            verify_website = bool(verify_website)

    if spider_type == 'companyinfo':
        print '开始抓取股票公司信息...'
        spider_company(symbol_prefix, start_code, end_code, clean_db, verify_website)
    elif spider_type == 'stockhistory':
        print '开始抓取历史信息...'
    elif spider_type == 'stockrealtime':
        print '开始抓取股票实时信息...'
    else:
        print '无法识别输入的符号: --type=', spider_type
        sys.exit(-1)
