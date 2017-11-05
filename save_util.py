# -*- coding:utf-8 -*-
import MySqlConn
import time
import sql_template


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
        try:
            mysql.insert_one(sql_template.INSERT_INTO_BORAD_INFO, (
                boardinfo['keycode'], boardinfo['keyname'], boardinfo['keynameacronym'], boardinfo['boardcode'],
                boardinfo['boardname']))
            mysql.commit()
        except BaseException, arguement:

            print '插入板块信息失败,原因: ', arguement
        boardmap_str += boardinfo['keycode'] + ','
    for industryinfo in info['tqCompIndustryList']:  # 记录股票所属行业
        try:
            mysql.insert_one(sql_template.INSERT_INTO_INDUSTRY_INFO, (
                industryinfo['level2code'], industryinfo['level2name'], industryinfo['level2nameacronym'],
                industryinfo['compcode']))
            mysql.commit()
        except BaseException, arguement:
            print '插入行业信息失败,原因: ', arguement
        industry_str += industryinfo['level2code'] + ','
    try:
        # 插入公司信息
        mysql.insert_one(sql_template.INSERT_INTO_COMPANY_INFO, (
            info['compcode'],
            info['compname'],
            info['engname'],
            info['comptype1'],
            info['comptype2'],
            info['founddate'],
            info['orgtype'],
            info['regcapital'],
            info['authcapsk'],
            info['chairman'],
            info['manager'],
            info['legrep'],
            info['bsecretary'],
            info['bsecretarytel'],
            info['bsecretaryfax'],
            info['seaffrepr'],
            info['seagttel'],
            info['seagtfax'],
            info['seagtemail'],
            info['authreprsbd'],
            info['leconstant'],
            info['accfirm'],
            info['regaddr'],
            info['officeaddr'],
            info['officezipcode'],
            info['comptel'],
            info['compfax'],
            info['compemail'],
            info['compurl'],
            info['servicetel'],
            info['servicefax'],
            info['compintro'],
            info['bizscope'],
            info['majorbiz'],
            info['bizscale'],
            info['compsname'],
            info['region'],
            info['regptcode'],
            None if (info['listdate'] is None) else time.strftime('%Y-%m-%d %H:%M',
                                                                  time.localtime(info['listdate'] / 1000)),
            info['issprice'],
            info['onlactissqty'],
            info['actissqty'],
            boardmap_str if boardmap_str is not None else None,
            industry_str if industry_str is not None else None))
        mysql.commit()
    except BaseException, arguement:
        if str(arguement).find("Duplicate") == -1:  # 如果错误不是主键重复,提示用户
            print '插入股票公司概况信息失败,信息为: ', str(arguement)
    try:
        # 插入股票代码和公司对应信息表
        mysql.insert_one(sql_template.INSERT_INTO_STOCK_COMPANY, (info['compcode'], symbol))
    except BaseException, arguement:
        print '插入股票代码对应公司信息失败,信息为: ', str(arguement)
    finally:
        mysql.dispose()


def create_and_clear_table():
    """
    创建数据库,创建相关数据表,并清空其中的信息

    :return:
    """
    mysql = MySqlConn.Mysql()
    try:
        mysql.update(sql_template.CREATE_DATABASE_STOCK, ())
        mysql.update(sql_template.USE_DATABASE_STOCK, ())

        mysql.update(sql_template.CREATE_TABLE_BOARD_INFO, ())
        mysql.update(sql_template.CREATE_TABLE_INDUSTRY_INFO, ())
        mysql.update(sql_template.CREATE_TABLE_COMPANY_INFO, ())
        mysql.update(sql_template.CREATE_TABLE_STOCK_COMPANY, ())

        mysql.delete(sql_template.CLEAN_TABLE_COMPANY_INFO, ())
        mysql.delete(sql_template.CLEAN_TABLE_STOCK_COMPANY, ())
        mysql.delete(sql_template.CLEAN_TABLE_BOARD_INFO, ())
        mysql.delete(sql_template.CLEAN_TABLE_INDUSTRY_INFO, ())
        mysql.commit()
    except BaseException, arguement:
        print '删除表失败,信息: ', arguement
    finally:
        mysql.dispose()
