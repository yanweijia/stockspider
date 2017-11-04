# -*- coding:utf-8 -*-
import MySqlConn
import time


def save_stock_compinfo(symbol, info):
    """
    保存股票公司概况信息

    :param symbol: 股票代码
    :param tqCompInfo: json数据
    :return:
    """
    mysql = MySqlConn.Mysql()
    boardmap_str = ''
    industry_str = ''
    for boardinfo in info['tqCompBoardmapList']:  # 记录股票所属板块
        sql = "INSERT INTO `board_info` (`keycode`, `keyname`, `keynameacronym`, `boardcode`, `boardname`)VALUES(%s,%s,%s,%s,%s)"
        try:
            mysql.insert_one(sql, (
                boardinfo['keycode'], boardinfo['keyname'], boardinfo['keynameacronym'], boardinfo['boardcode'],
                boardinfo['boardname']))
            mysql.commit()
        except BaseException, arguement:

            print '插入板块信息失败,原因: ', arguement
        boardmap_str += boardinfo['keycode'] + ','
    for industryinfo in info['tqCompIndustryList']:  # 记录股票所属行业
        sql = "INSERT INTO `industry_info` (`level2code`, `level2name`, `level2nameacronym`, `compcode`)VALUES(%s,%s,%s,%s)"
        try:
            mysql.insert_one(sql, (
                industryinfo['level2code'], industryinfo['level2name'], industryinfo['level2nameacronym'],
                industryinfo['compcode']))
            mysql.commit()
        except BaseException, arguement:
            print '插入行业信息失败,原因: ', arguement
        industry_str += industryinfo['level2code'] + ','
    try:
        sql = "INSERT INTO `company_info` (`compcode`, `compname`, `engname`, `comptype1`, `comptype2`, `founddate`, `orgtype`, `regcapital`, `authcapsk`, `chairman`, `manager`, `legrep`, `bsecretary`, `bsecretarytel`, `basecretaryfax`, `seaffrepr`, `seagttel`, `seagtfax`, `seagtemail`, `authreprsbd`, `leconstant`, `accfirm`, `regaddr`, `officeaddr`, `officezipcode`, `comptel`, `compfax`, `compemail`, `compurl`, `servicetel`, `servicefax`, `compintro`, `bizscope`, `majorbiz`, `bizscale`, `compsname`, `region`, `regptcode`, `listdate`, `issprice`, `onlactissqty`, `actissqty`, `boardmap_list`, `industry_list`)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        mysql.insert_one(sql, (
            info['compcode'], info['compname'], info['engname'], info['comptype1'], info['comptype2'],
            info['founddate'],
            info['orgtype'], info['regcapital'], info['authcapsk'], info['chairman'], info['manager'], info['legrep'],
            info['bsecretary'], info['bsecretarytel'], info['bsecretaryfax'], info['seaffrepr'], info['seagttel'],
            info['seagtfax'], info['seagtemail'], info['authreprsbd'], info['leconstant'], info['accfirm'],
            info['regaddr'],
            info['officeaddr'], info['officezipcode'], info['comptel'], info['compfax'], info['compemail'],
            info['compurl'],
            info['servicetel'], info['servicefax'], info['compintro'], info['bizscope'], info['majorbiz'],
            info['bizscale'],
            info['compsname'], info['region'], info['regptcode'],
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(info['listdate'] / 100))
            if (info['listdate'] is not None) else None, info['issprice'],
            info['onlactissqty'],
            info['actissqty'], boardmap_str, industry_str))
        sql = "INSERT INTO `stock_company` (`compcode`,`symbol`)VALUES(%s,%s)"
        mysql.insert_one(sql, (info['compcode'], symbol))
        mysql.commit()
    except BaseException, arguement:
        if str(arguement).find("Duplicate") == -1:  # 如果错误不是主键重复,提示用户
            print '插入股票公司概况信息失败,信息为: ', arguement
    finally:
        mysql.dispose()


def clear_table():
    mysql = MySqlConn.Mysql()
    try:
        mysql.delete("DELETE FROM stock_company", ())
        mysql.delete("DELETE FROM board_info", ())
        mysql.delete("DELETE FROM industry_info", ())
        mysql.commit()
    except BaseException, arguement:
        print '删除表失败,信息: ', arguement
    finally:
        mysql.dispose()
