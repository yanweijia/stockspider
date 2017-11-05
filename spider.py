# -*- coding:utf-8 -*-

# 参考:
# Python-第三方库requests详解  http://blog.csdn.net/shanzhizi/article/details/50903748


import requests, threading, json, logging, sys
import save_util

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'aliyungf_tc=AQAAAHbeHVwTlgoA7n9aZZOl8v+bX73z; s=fq12j9bjw5; xq_a_token=469ea9edce5537d5d8297aaffcd3474cc8d12273; xq_r_token=819ae94ba56378cc0665670983c2afafc34c275b; u=891509432616809; device_id=9d599aed6cb8bcc65d6d18c81687571d; __utma=1.1712410977.1509432617.1509440772.1509454565.3; __utmc=1; __utmz=1.1509432617.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); Hm_lvt_1db88642e346389874251b5a1eded6e3=1509432617; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1509455639',
    'Host': 'xueqiu.com',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}


def main(symbol_prefix='SH', start_code=000000, end_code=999999):
    save_util.create_and_clear_table()  # 创建表并清空相关表信息
    for i in range(start_code, end_code, 1):
        symbol = symbol_prefix + str(i).zfill(6)
        params = {'symbol': symbol}
        res = requests.get("https://xueqiu.com/stock/f10/compinfo.json", params=params, headers=headers, timeout=10000,
                           verify=False)
        if (res.status_code == 200):
            tqCompInfo = json.loads(res.content, encoding='utf-8')['tqCompInfo']
            if tqCompInfo == None:
                print '无此编号:' + symbol
            else:
                save_util.save_stock_compinfo(symbol, tqCompInfo)
                print '成功下载编号为: ', symbol, ' 的股票信息'
        else:
            print "下载错误,download fail, http response code is:" + res.status_code
            print res.headers
            print res
            break


if __name__ == '__main__':
    symbol_prefix = sys.argv[1] if sys.argv[1] is not None else 'SH'
    start_code = int(sys.argv[2]) if sys.argv[2] is not None else 000000
    end_code = int(sys.argv[3]) if sys.argv[3] is not None else 999999
    main(symbol_prefix, start_code, end_code)
