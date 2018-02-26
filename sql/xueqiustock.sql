/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50720
Source Host           : localhost:3306
Source Database       : xueqiustock

Target Server Type    : MYSQL
Target Server Version : 50720
File Encoding         : 65001

Date: 2018-02-26 16:12:04
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for t_cwzb
-- ----------------------------
DROP TABLE IF EXISTS `t_cwzb`;
CREATE TABLE `t_cwzb` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `basiceps` decimal(15,2) DEFAULT NULL COMMENT '基本每股收益',
  `naps` decimal(15,2) DEFAULT NULL COMMENT '每股净资产',
  `opercashpershare` decimal(15,2) DEFAULT NULL COMMENT '每股现金流',
  `peropecashpershare` decimal(15,2) DEFAULT NULL COMMENT '每股经营性现金流',
  `netassgrowrate` decimal(15,2) DEFAULT NULL COMMENT '净资产增长率',
  `weightedroe` decimal(15,2) DEFAULT NULL COMMENT '净资产收益率（加权）',
  `dilutedroe` decimal(15,2) DEFAULT NULL COMMENT '净资产收益率（摊薄）',
  `mainbusincgrowrate` decimal(15,2) DEFAULT NULL COMMENT '主营业务增长率',
  `netincgrowrate` decimal(15,2) DEFAULT NULL COMMENT '净利润增长率',
  `totassgrowrate` decimal(15,2) DEFAULT NULL COMMENT '总资产增长率',
  `salegrossprofitrto` decimal(15,2) DEFAULT NULL COMMENT '销售毛利率',
  `mainbusiincome` decimal(15,2) DEFAULT NULL COMMENT '主营业务收入',
  `mainbusiprofit` decimal(15,2) DEFAULT NULL COMMENT '主营业务利润',
  `totprofit` decimal(15,2) DEFAULT NULL COMMENT '利润总额',
  `netprofit` decimal(15,2) DEFAULT NULL COMMENT '净利润',
  `totalassets` decimal(15,2) DEFAULT NULL COMMENT '资产总额',
  `totalliab` decimal(15,2) DEFAULT NULL COMMENT '负债总额',
  `totsharequi` decimal(15,2) DEFAULT NULL COMMENT '股东权益合计',
  `operrevenue` decimal(15,2) DEFAULT NULL COMMENT '经营现金流净额',
  `invnetcashflow` decimal(15,2) DEFAULT NULL COMMENT '投资现金流净额',
  `finnetcflow` decimal(15,2) DEFAULT NULL COMMENT '筹资现金流净额',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6273 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_lrb
-- ----------------------------
DROP TABLE IF EXISTS `t_lrb`;
CREATE TABLE `t_lrb` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `yyzsr` decimal(15,2) DEFAULT NULL COMMENT '营业总收入',
  `yyzcb` decimal(15,2) DEFAULT NULL COMMENT '营业总成本',
  `xsfy` decimal(15,2) DEFAULT NULL COMMENT '销售费用',
  `glfy` decimal(15,2) DEFAULT NULL COMMENT '管理费用',
  `cwfy` decimal(15,2) DEFAULT NULL COMMENT '财务费用',
  `yylr` decimal(15,2) DEFAULT NULL COMMENT '营业利润',
  `yywsr` decimal(15,2) DEFAULT NULL COMMENT '营业外收入',
  `yywzc` decimal(15,2) DEFAULT NULL COMMENT '营业外支出',
  `lrze` decimal(15,2) DEFAULT NULL COMMENT '利润总额',
  `sdsfy` decimal(15,2) DEFAULT NULL COMMENT '所得税费用',
  `jlr` decimal(15,2) DEFAULT NULL COMMENT '净利润',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13229 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_xjllb
-- ----------------------------
DROP TABLE IF EXISTS `t_xjllb`;
CREATE TABLE `t_xjllb` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `jyhdcsdxjje` decimal(15,2) DEFAULT NULL COMMENT '经营活动产生的现金流量净额',
  `tzhdcsdxjje` decimal(15,2) DEFAULT NULL COMMENT '投资活动产生的现金流量净额',
  `czhdcsdxjje` decimal(15,2) DEFAULT NULL COMMENT '筹资活动产生的现金净额',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_zcfzb
-- ----------------------------
DROP TABLE IF EXISTS `t_zcfzb`;
CREATE TABLE `t_zcfzb` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `code` varchar(10) NOT NULL,
  `date` date NOT NULL,
  `hbzj` decimal(15,2) DEFAULT NULL COMMENT '货币资金',
  `yspj` decimal(15,2) DEFAULT NULL COMMENT '应收票据',
  `yszk` decimal(15,2) DEFAULT NULL COMMENT '应收账款',
  `yfkx` decimal(15,2) DEFAULT NULL COMMENT '预付款项',
  `ch` decimal(15,2) DEFAULT NULL COMMENT '存货',
  `ldzchj` decimal(15,2) DEFAULT NULL COMMENT '流动资产合计',
  `sy` decimal(15,2) DEFAULT NULL COMMENT '商誉',
  `cqdtfy` decimal(15,2) DEFAULT NULL COMMENT '长期待摊费用',
  `fldzchj` decimal(15,2) DEFAULT NULL COMMENT '非流动资产合计',
  `zczj` decimal(15,2) DEFAULT NULL COMMENT '资产总计',
  `yfzk` decimal(15,2) DEFAULT NULL COMMENT '应付账款',
  `yskx` decimal(15,2) DEFAULT NULL COMMENT '预收款项',
  `ldfzhj` decimal(15,2) DEFAULT NULL COMMENT '流动负债合计',
  `fzhj` decimal(15,2) DEFAULT NULL COMMENT '负债合计',
  `sszb` decimal(15,2) DEFAULT NULL COMMENT '实收资本（股本）',
  `syzqy` decimal(15,2) DEFAULT NULL COMMENT '所有者权益',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7545 DEFAULT CHARSET=utf8;
