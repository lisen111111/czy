-- MySQL dump 10.13  Distrib 5.7.31, for Linux (x86_64)
--
-- Host: localhost    Database: zxjyts
-- ------------------------------------------------------
-- Server version	5.7.31

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `zxjyts`
--

/*!40000 DROP DATABASE IF EXISTS `zxjyts`*/;

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `zxjyts` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `zxjyts`;

--
-- Table structure for table `config`
--

DROP TABLE IF EXISTS `config`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `config` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(100) NOT NULL COMMENT '配置参数名称',
  `value` varchar(100) DEFAULT NULL COMMENT '配置参数值',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COMMENT='配置文件';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `config`
--

LOCK TABLES `config` WRITE;
/*!40000 ALTER TABLE `config` DISABLE KEYS */;
INSERT INTO `config` VALUES (1,'picture1','upload/picture1.jpg'),(2,'picture2','upload/picture2.jpg'),(3,'picture3','upload/picture3.jpg');
/*!40000 ALTER TABLE `config` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `duzhe`
--

DROP TABLE IF EXISTS `duzhe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `duzhe` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `zhanghao` varchar(200) NOT NULL COMMENT '账号',
  `mima` varchar(200) NOT NULL COMMENT '密码',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  `xingbie` varchar(200) DEFAULT NULL COMMENT '性别',
  `shouji` varchar(200) DEFAULT NULL COMMENT '手机',
  `shenfenzheng` varchar(200) DEFAULT NULL COMMENT '身份证',
  `youxiang` varchar(200) DEFAULT NULL COMMENT '邮箱',
  `dizhi` varchar(200) DEFAULT NULL COMMENT '地址',
  PRIMARY KEY (`id`),
  UNIQUE KEY `zhanghao` (`zhanghao`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COMMENT='读者';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `duzhe`
--

LOCK TABLES `duzhe` WRITE;
/*!40000 ALTER TABLE `duzhe` DISABLE KEYS */;
INSERT INTO `duzhe` VALUES (11,'2022-04-09 08:44:36','账号1','123456','姓名1','男','13823888881','440300199101010001','773890001@qq.com','地址1'),(12,'2022-04-09 08:44:36','账号2','123456','姓名2','男','13823888882','440300199202020002','773890002@qq.com','地址2'),(13,'2022-04-09 08:44:36','账号3','123456','姓名3','男','13823888883','440300199303030003','773890003@qq.com','地址3'),(14,'2022-04-09 08:44:36','账号4','123456','姓名4','男','13823888884','440300199404040004','773890004@qq.com','地址4'),(15,'2022-04-09 08:44:36','账号5','123456','姓名5','男','13823888885','440300199505050005','773890005@qq.com','地址5'),(16,'2022-04-09 08:44:36','账号6','123456','姓名6','男','13823888886','440300199606060006','773890006@qq.com','地址6');
/*!40000 ALTER TABLE `duzhe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guihaijilu`
--

DROP TABLE IF EXISTS `guihaijilu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `guihaijilu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `guihaibianhao` varchar(200) DEFAULT NULL COMMENT '归还编号',
  `zuozhe` varchar(200) DEFAULT NULL COMMENT '作者',
  `tushumingcheng` varchar(200) DEFAULT NULL COMMENT '图书名称',
  `tushutupian` varchar(200) DEFAULT NULL COMMENT '图书图片',
  `zhanghao` varchar(200) DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  `shuliang` float DEFAULT NULL COMMENT '数量',
  `jieshuriqi` date DEFAULT NULL COMMENT '借书日期',
  `haishuriqi` datetime DEFAULT NULL COMMENT '还书日期',
  `userid` bigint(20) DEFAULT NULL COMMENT '用户id',
  PRIMARY KEY (`id`),
  UNIQUE KEY `guihaibianhao` (`guihaibianhao`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8 COMMENT='归还记录';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guihaijilu`
--

LOCK TABLES `guihaijilu` WRITE;
/*!40000 ALTER TABLE `guihaijilu` DISABLE KEYS */;
INSERT INTO `guihaijilu` VALUES (51,'2022-04-09 08:44:36','1111111111','作者1','图书名称1','upload/guihaijilu_tushutupian1.jpg','账号1','姓名1',1,'2022-04-09','2022-04-09 16:44:36',1),(52,'2022-04-09 08:44:36','2222222222','作者2','图书名称2','upload/guihaijilu_tushutupian2.jpg','账号2','姓名2',2,'2022-04-09','2022-04-09 16:44:36',2),(53,'2022-04-09 08:44:36','3333333333','作者3','图书名称3','upload/guihaijilu_tushutupian3.jpg','账号3','姓名3',3,'2022-04-09','2022-04-09 16:44:36',3),(54,'2022-04-09 08:44:36','4444444444','作者4','图书名称4','upload/guihaijilu_tushutupian4.jpg','账号4','姓名4',4,'2022-04-09','2022-04-09 16:44:36',4),(55,'2022-04-09 08:44:36','5555555555','作者5','图书名称5','upload/guihaijilu_tushutupian5.jpg','账号5','姓名5',5,'2022-04-09','2022-04-09 16:44:36',5),(56,'2022-04-09 08:44:36','6666666666','作者6','图书名称6','upload/guihaijilu_tushutupian6.jpg','账号6','姓名6',6,'2022-04-09','2022-04-09 16:44:36',6);
/*!40000 ALTER TABLE `guihaijilu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jieyuejilu`
--

DROP TABLE IF EXISTS `jieyuejilu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jieyuejilu` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jieyuebianhao` varchar(200) DEFAULT NULL COMMENT '借阅编号',
  `zuozhe` varchar(200) DEFAULT NULL COMMENT '作者',
  `tushumingcheng` varchar(200) DEFAULT NULL COMMENT '图书名称',
  `tushutupian` varchar(200) DEFAULT NULL COMMENT '图书图片',
  `zhanghao` varchar(200) DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  `shuliang` float DEFAULT NULL COMMENT '数量',
  `jieshuriqi` datetime DEFAULT NULL COMMENT '借书日期',
  `daoqiriqi` datetime DEFAULT NULL COMMENT '到期日期',
  `beizhu` varchar(200) DEFAULT NULL COMMENT '备注',
  `userid` bigint(20) DEFAULT NULL COMMENT '用户id',
  PRIMARY KEY (`id`),
  UNIQUE KEY `jieyuebianhao` (`jieyuebianhao`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8 COMMENT='借阅记录';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jieyuejilu`
--

LOCK TABLES `jieyuejilu` WRITE;
/*!40000 ALTER TABLE `jieyuejilu` DISABLE KEYS */;
INSERT INTO `jieyuejilu` VALUES (41,'2022-04-09 08:44:36','1111111111','作者1','图书名称1','upload/jieyuejilu_tushutupian1.jpg','账号1','姓名1',1,'2022-04-09 16:44:36','2022-04-09 16:44:36','备注1',1),(42,'2022-04-09 08:44:36','2222222222','作者2','图书名称2','upload/jieyuejilu_tushutupian2.jpg','账号2','姓名2',2,'2022-04-09 16:44:36','2022-04-09 16:44:36','备注2',2),(43,'2022-04-09 08:44:36','3333333333','作者3','图书名称3','upload/jieyuejilu_tushutupian3.jpg','账号3','姓名3',3,'2022-04-09 16:44:36','2022-04-09 16:44:36','备注3',3),(44,'2022-04-09 08:44:36','4444444444','作者4','图书名称4','upload/jieyuejilu_tushutupian4.jpg','账号4','姓名4',4,'2022-04-09 16:44:36','2022-04-09 16:44:36','备注4',4),(45,'2022-04-09 08:44:36','5555555555','作者5','图书名称5','upload/jieyuejilu_tushutupian5.jpg','账号5','姓名5',5,'2022-04-09 16:44:36','2022-04-09 16:44:36','备注5',5),(46,'2022-04-09 08:44:36','6666666666','作者6','图书名称6','upload/jieyuejilu_tushutupian6.jpg','账号6','姓名6',6,'2022-04-09 16:44:36','2022-04-09 16:44:36','备注6',6);
/*!40000 ALTER TABLE `jieyuejilu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `messages` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `userid` bigint(20) NOT NULL COMMENT '留言人id',
  `username` varchar(200) DEFAULT NULL COMMENT '用户名',
  `content` longtext NOT NULL COMMENT '留言内容',
  `cpicture` varchar(200) DEFAULT NULL COMMENT '留言图片',
  `reply` longtext COMMENT '回复内容',
  `rpicture` varchar(200) DEFAULT NULL COMMENT '回复图片',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8 COMMENT='留言板';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (71,'2022-04-09 08:44:36',1,'用户名1','留言内容1','upload/messages_cpicture1.jpg','回复内容1','upload/messages_rpicture1.jpg'),(72,'2022-04-09 08:44:36',2,'用户名2','留言内容2','upload/messages_cpicture2.jpg','回复内容2','upload/messages_rpicture2.jpg'),(73,'2022-04-09 08:44:36',3,'用户名3','留言内容3','upload/messages_cpicture3.jpg','回复内容3','upload/messages_rpicture3.jpg'),(74,'2022-04-09 08:44:36',4,'用户名4','留言内容4','upload/messages_cpicture4.jpg','回复内容4','upload/messages_rpicture4.jpg'),(75,'2022-04-09 08:44:36',5,'用户名5','留言内容5','upload/messages_cpicture5.jpg','回复内容5','upload/messages_rpicture5.jpg'),(76,'2022-04-09 08:44:36',6,'用户名6','留言内容6','upload/messages_cpicture6.jpg','回复内容6','upload/messages_rpicture6.jpg');
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tushufenlei`
--

DROP TABLE IF EXISTS `tushufenlei`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tushufenlei` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `fenlei` varchar(200) DEFAULT NULL COMMENT '分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COMMENT='图书分类';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tushufenlei`
--

LOCK TABLES `tushufenlei` WRITE;
/*!40000 ALTER TABLE `tushufenlei` DISABLE KEYS */;
INSERT INTO `tushufenlei` VALUES (21,'2022-04-09 08:44:36','分类1'),(22,'2022-04-09 08:44:36','分类2'),(23,'2022-04-09 08:44:36','分类3'),(24,'2022-04-09 08:44:36','分类4'),(25,'2022-04-09 08:44:36','分类5'),(26,'2022-04-09 08:44:36','分类6');
/*!40000 ALTER TABLE `tushufenlei` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tushuxinxi`
--

DROP TABLE IF EXISTS `tushuxinxi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tushuxinxi` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `tushubianhao` varchar(200) NOT NULL COMMENT '图书编号',
  `tushumingcheng` varchar(200) DEFAULT NULL COMMENT '图书名称',
  `zuozhe` varchar(200) DEFAULT NULL COMMENT '作者',
  `fenlei` varchar(200) DEFAULT NULL COMMENT '分类',
  `jiage` varchar(200) DEFAULT NULL COMMENT '价格',
  `chubanshe` varchar(200) DEFAULT NULL COMMENT '出版社',
  `chubanriqi` date DEFAULT NULL COMMENT '出版日期',
  `shuliang` float DEFAULT NULL COMMENT '数量',
  `tushutupian` varchar(200) DEFAULT NULL COMMENT '图书图片',
  `tushujianjie` longtext COMMENT '图书简介',
  `tushuweizhi` varchar(200) DEFAULT NULL COMMENT '图书位置',
  PRIMARY KEY (`id`),
  UNIQUE KEY `tushubianhao` (`tushubianhao`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8 COMMENT='图书信息';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tushuxinxi`
--

LOCK TABLES `tushuxinxi` WRITE;
/*!40000 ALTER TABLE `tushuxinxi` DISABLE KEYS */;
INSERT INTO `tushuxinxi` VALUES (31,'2022-04-09 08:44:36','1111111111','图书名称1','作者1','分类1','价格1','出版社1','2022-04-09',1,'upload/tushuxinxi_tushutupian1.jpg','图书简介1','图书位置1'),(32,'2022-04-09 08:44:36','2222222222','图书名称2','作者2','分类2','价格2','出版社2','2022-04-09',2,'upload/tushuxinxi_tushutupian2.jpg','图书简介2','图书位置2'),(33,'2022-04-09 08:44:36','3333333333','图书名称3','作者3','分类3','价格3','出版社3','2022-04-09',3,'upload/tushuxinxi_tushutupian3.jpg','图书简介3','图书位置3'),(34,'2022-04-09 08:44:36','4444444444','图书名称4','作者4','分类4','价格4','出版社4','2022-04-09',4,'upload/tushuxinxi_tushutupian4.jpg','图书简介4','图书位置4'),(35,'2022-04-09 08:44:36','5555555555','图书名称5','作者5','分类5','价格5','出版社5','2022-04-09',5,'upload/tushuxinxi_tushutupian5.jpg','图书简介5','图书位置5'),(36,'2022-04-09 08:44:36','6666666666','图书名称6','作者6','分类6','价格6','出版社6','2022-04-09',6,'upload/tushuxinxi_tushutupian6.jpg','图书简介6','图书位置6');
/*!40000 ALTER TABLE `tushuxinxi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tushuxujie`
--

DROP TABLE IF EXISTS `tushuxujie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tushuxujie` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  `jieyuebianhao` varchar(200) DEFAULT NULL COMMENT '借阅编号',
  `zuozhe` varchar(200) DEFAULT NULL COMMENT '作者',
  `tushumingcheng` varchar(200) DEFAULT NULL COMMENT '图书名称',
  `tushutupian` varchar(200) DEFAULT NULL COMMENT '图书图片',
  `jieshuriqi` varchar(200) DEFAULT NULL COMMENT '借书日期',
  `zhanghao` varchar(200) DEFAULT NULL COMMENT '账号',
  `xingming` varchar(200) DEFAULT NULL COMMENT '姓名',
  `xujieriqi` datetime DEFAULT NULL COMMENT '续借日期',
  `xujiebeizhu` varchar(200) DEFAULT NULL COMMENT '续借备注',
  //`sfsh` varchar(200) DEFAULT '否' COMMENT '是否审核',
  //`shhf` longtext COMMENT '审核回复',
  `userid` bigint(20) DEFAULT NULL COMMENT '用户id',
  PRIMARY KEY (`id`),
  UNIQUE KEY `jieyuebianhao` (`jieyuebianhao`)
) ENGINE=InnoDB AUTO_INCREMENT=67 DEFAULT CHARSET=utf8 COMMENT='图书续借';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tushuxujie`
--

LOCK TABLES `tushuxujie` WRITE;
/*!40000 ALTER TABLE `tushuxujie` DISABLE KEYS */;
INSERT INTO `tushuxujie` VALUES (61,'2022-04-09 08:44:36','1111111111','作者1','图书名称1','upload/tushuxujie_tushutupian1.jpg','借书日期1','账号1','姓名1','2022-04-09 16:44:36','续借备注1','是','',1),(62,'2022-04-09 08:44:36','2222222222','作者2','图书名称2','upload/tushuxujie_tushutupian2.jpg','借书日期2','账号2','姓名2','2022-04-09 16:44:36','续借备注2','是','',2),(63,'2022-04-09 08:44:36','3333333333','作者3','图书名称3','upload/tushuxujie_tushutupian3.jpg','借书日期3','账号3','姓名3','2022-04-09 16:44:36','续借备注3','是','',3),(64,'2022-04-09 08:44:36','4444444444','作者4','图书名称4','upload/tushuxujie_tushutupian4.jpg','借书日期4','账号4','姓名4','2022-04-09 16:44:36','续借备注4','是','',4),(65,'2022-04-09 08:44:36','5555555555','作者5','图书名称5','upload/tushuxujie_tushutupian5.jpg','借书日期5','账号5','姓名5','2022-04-09 16:44:36','续借备注5','是','',5),(66,'2022-04-09 08:44:36','6666666666','作者6','图书名称6','upload/tushuxujie_tushutupian6.jpg','借书日期6','账号6','姓名6','2022-04-09 16:44:36','续借备注6','是','',6);
/*!40000 ALTER TABLE `tushuxujie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `username` varchar(100) NOT NULL COMMENT '用户名',
  `password` varchar(100) NOT NULL COMMENT '密码',
  `role` varchar(100) DEFAULT '管理员' COMMENT '角色',
  `addtime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '新增时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='用户表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'abo','abo','管理员','2022-04-09 08:44:36');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-19 21:39:11
