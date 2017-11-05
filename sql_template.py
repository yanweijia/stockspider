# -*- coding:utf-8 -*-

# 创建 stock 数据库
CREATE_DATABASE_STOCK = "CREATE DATABASE IF NOT EXISTS `stock` default charset=utf8"
# 使用 stock 数据库
USE_DATABASE_STOCK = "USE `stock`"
# 创建 board_info 表
CREATE_TABLE_BOARD_INFO = """
    CREATE TABLE IF NOT EXISTS `board_info` (
          `keycode` varchar(11) NOT NULL DEFAULT '' COMMENT '编号',
          `keyname` varchar(50) DEFAULT NULL COMMENT '名称',
          `keynameacronym` varchar(20) DEFAULT NULL COMMENT '首字母缩写',
          `boardcode` varchar(10) DEFAULT NULL COMMENT '板块编号',
          `boardname` varchar(50) DEFAULT NULL COMMENT '板块名称',
          PRIMARY KEY (`keycode`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='版块名称';
      """
# 创建 industry_info 表
CREATE_TABLE_INDUSTRY_INFO = """
    CREATE TABLE IF NOT EXISTS `industry_info` (
          `level2code` varchar(11) NOT NULL DEFAULT '' COMMENT '编号',
          `level2name` varchar(50) DEFAULT NULL COMMENT '名称',
          `level2nameacronym` varchar(20) DEFAULT NULL COMMENT '名称首字母缩写',
          `compcode` varchar(15) DEFAULT NULL COMMENT '公司编号',
          PRIMARY KEY (`level2code`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='工业板块信息';
    """
# 创建 company_info 表
CREATE_TABLE_COMPANY_INFO = """
    CREATE TABLE IF NOT EXISTS `company_info` (
          `compcode` int(20) unsigned NOT NULL,
          `compname` varchar(100) DEFAULT NULL COMMENT '公司名称',
          `engname` varchar(100) DEFAULT NULL COMMENT '公司英文名称',
          `comptype1` varchar(10) DEFAULT NULL,
          `comptype2` varchar(11) DEFAULT NULL,
          `founddate` date DEFAULT NULL COMMENT '成立日期',
          `orgtype` varchar(11) DEFAULT NULL COMMENT '组织形式',
          `regcapital` decimal(20,2) DEFAULT NULL COMMENT '注册资本（万元）',
          `authcapsk` int(11) DEFAULT NULL,
          `chairman` varchar(20) DEFAULT NULL COMMENT '董事长',
          `manager` varchar(20) DEFAULT NULL COMMENT '总经理',
          `legrep` varchar(20) DEFAULT NULL COMMENT '法人代表',
          `bsecretary` varchar(20) DEFAULT '' COMMENT '董秘',
          `bsecretarytel` varchar(30) DEFAULT NULL COMMENT '董秘电话',
          `basecretaryfax` varchar(30) DEFAULT NULL COMMENT '董秘传真',
          `seaffrepr` varchar(20) DEFAULT NULL,
          `seagttel` varchar(30) DEFAULT NULL,
          `seagtfax` varchar(30) DEFAULT NULL,
          `seagtemail` varchar(50) DEFAULT NULL,
          `authreprsbd` varchar(20) DEFAULT NULL,
          `leconstant` varchar(50) DEFAULT NULL,
          `accfirm` varchar(50) DEFAULT NULL,
          `regaddr` varchar(100) DEFAULT NULL,
          `officeaddr` varchar(100) DEFAULT NULL,
          `officezipcode` varchar(6) DEFAULT NULL,
          `comptel` varchar(50) DEFAULT NULL,
          `compfax` varchar(50) DEFAULT NULL,
          `compemail` varchar(50) DEFAULT NULL,
          `compurl` varchar(100) DEFAULT NULL,
          `servicetel` varchar(50) DEFAULT NULL,
          `servicefax` varchar(50) DEFAULT NULL,
          `compintro` varchar(1000) DEFAULT NULL,
          `bizscope` varchar(1000) DEFAULT NULL,
          `majorbiz` varchar(200) DEFAULT NULL,
          `bizscale` varchar(10) DEFAULT NULL,
          `compsname` varchar(50) DEFAULT NULL,
          `region` varchar(20) DEFAULT NULL,
          `regptcode` int(20) unsigned DEFAULT NULL,
          `listdate` date DEFAULT NULL,
          `issprice` decimal(10,2) DEFAULT NULL,
          `onlactissqty` int(11) DEFAULT NULL,
          `actissqty` int(11) DEFAULT NULL,
          `boardmap_list` varchar(255) DEFAULT NULL COMMENT '所属板块,用,分隔',
          `industry_list` varchar(255) DEFAULT NULL COMMENT '所属行业',
          PRIMARY KEY (`compcode`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='公司信息';
"""
# 创建 stock_company 表
CREATE_TABLE_STOCK_COMPANY = """
    CREATE TABLE IF NOT EXISTS `stock_company` (
          `compcode` int(11) unsigned NOT NULL COMMENT '公司编号',
          `symbol` varchar(11) NOT NULL DEFAULT '' COMMENT '股票代码',
          PRIMARY KEY (`symbol`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='股票代码公司对应信息';
"""

# 清空 stock_company 表
CLEAN_TABLE_STOCK_COMPANY = "DELETE FROM `stock_company`"
# 清空 board_info 表
CLEAN_TABLE_BOARD_INFO = "DELETE FROM `board_info`"
# 清空 industry_info 表
CLEAN_TABLE_INDUSTRY_INFO = "DELETE FROM `industry_info`"
# 清空company_info 表
CLEAN_TABLE_COMPANY_INFO = "DELETE FROM `company_info`"

# 插入数据到 industry_info 表
INSERT_INTO_INDUSTRY_INFO = "INSERT INTO `industry_info` (`level2code`, `level2name`, `level2nameacronym`, `compcode`)VALUES(%s,%s,%s,%s)"
# 插入数据到 company_info 表
INSERT_INTO_COMPANY_INFO = "INSERT INTO `company_info` (`compcode`, `compname`, `engname`, `comptype1`, `comptype2`, `founddate`, `orgtype`, `regcapital`, `authcapsk`, `chairman`, `manager`, `legrep`, `bsecretary`, `bsecretarytel`, `basecretaryfax`, `seaffrepr`, `seagttel`, `seagtfax`, `seagtemail`, `authreprsbd`, `leconstant`, `accfirm`, `regaddr`, `officeaddr`, `officezipcode`, `comptel`, `compfax`, `compemail`, `compurl`, `servicetel`, `servicefax`, `compintro`, `bizscope`, `majorbiz`, `bizscale`, `compsname`, `region`, `regptcode`, `listdate`, `issprice`, `onlactissqty`, `actissqty`, `boardmap_list`, `industry_list`)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# 插入数据到 board_info 表
INSERT_INTO_BOARD_INFO = "INSERT INTO `board_info` (`keycode`, `keyname`, `keynameacronym`, `boardcode`, `boardname`)VALUES(%s,%s,%s,%s,%s)"
# 插入数据到 stock_company 表
INSERT_INTO_STOCK_COMPANY = "INSERT INTO `stock_company` (`compcode`,`symbol`)VALUES(%s,%s)"
