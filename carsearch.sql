set names utf8;
drop database carsearch;
create database carsearch character set utf8;
use carsearch;


# table
CREATE TABLE `carsearch_fygg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL comment '发布时间',
  `title` varchar(255) DEFAULT NULL comment '公告标题',
  `value` varchar(255) DEFAULT NULL comment '公告内容',
  `courtname` varchar(255) DEFAULT NULL comment '法院名称',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE `carsearch_admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL comment '管理员名称',
  `password` int(255) DEFAULT NULL comment '密码',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;