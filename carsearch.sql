desc <table_name>
show create table carsearch_fygg;
CREATE TABLE `carsearch_fygg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `anhao` varchar(50) DEFAULT NULL comment '案号',
  `title` varchar(255) DEFAULT NULL comment '公告标题',
  `value` varchar(255) DEFAULT NULL comment '公告内容',
  `courtname` varchar(255) DEFAULT NULL comment '法院名称',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8