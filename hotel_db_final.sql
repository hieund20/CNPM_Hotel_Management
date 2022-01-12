-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: hotel_management_db
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('5d183fecee28');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `booking_room`
--

DROP TABLE IF EXISTS `booking_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking_room` (
  `id` int NOT NULL AUTO_INCREMENT,
  `room_id` int NOT NULL,
  `room_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `price` float DEFAULT NULL,
  `receive_day` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `pay_day` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `person_amount` int DEFAULT NULL,
  `rental_voucher_detail_id` int DEFAULT NULL,
  `image` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`,`room_id`),
  KEY `rental_voucher_detail_id` (`rental_voucher_detail_id`),
  KEY `room_id` (`room_id`),
  CONSTRAINT `booking_room_ibfk_1` FOREIGN KEY (`rental_voucher_detail_id`) REFERENCES `rental_voucher_detail` (`id`),
  CONSTRAINT `booking_room_ibfk_2` FOREIGN KEY (`room_id`) REFERENCES `room` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `booking_room`
--

LOCK TABLES `booking_room` WRITE;
/*!40000 ALTER TABLE `booking_room` DISABLE KEYS */;
INSERT INTO `booking_room` VALUES (19,9,'Phòng Standard',1134500,'12/25/2021','12/25/2021',1,1,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403690/rooms_images/standard-room-1_xfjsmn.jpg'),(20,6,'Phòng Superior',1679970,'12/25/2021','12/25/2021',1,1,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg'),(21,6,'Phòng Superior',1679970,'12/25/2021','12/25/2021',1,1,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg'),(22,6,'Phòng Superior',1679970,'12/25/2021','12/25/2021',1,1,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg'),(23,6,'Phòng Superior',1679970,'12/25/2021','12/25/2021',1,1,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg'),(24,6,'Phòng Superior',1679970,'12/25/2021','12/25/2021',1,1,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg'),(25,6,'Phòng Superior',1679970,'12/25/2021','12/25/2021',1,1,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg'),(26,6,'Phòng Superior',1679970,'12/25/2021','12/25/2021',1,1,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg'),(27,6,'Phòng Superior',1679970,'12/25/2021','12/25/2021',1,1,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg'),(28,6,'Phòng Superior',1679970,'12/25/2021','12/25/2021',1,1,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg'),(29,6,'Phòng Superior',1679970,'12/25/2021','12/25/2021',1,1,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg'),(30,6,'Phòng Superior',1679970,'12/25/2021','12/25/2021',1,1,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg'),(31,6,'Phòng Superior',1679970,'12/25/2021','12/25/2021',1,118,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg'),(32,6,'Phòng Superior',1679970,'12/25/2021','12/25/2021',1,118,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg'),(36,29,'Phòng Standard',1134500,'12/25/2021','12/25/2021',1,120,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403690/rooms_images/standard-room-1_xfjsmn.jpg');
/*!40000 ALTER TABLE `booking_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `change_policy_number`
--

DROP TABLE IF EXISTS `change_policy_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `change_policy_number` (
  `id` int NOT NULL AUTO_INCREMENT,
  `foreign_visitor_number` float DEFAULT NULL,
  `domestic_visitor_number` float DEFAULT NULL,
  `quantity_types_visitors` int DEFAULT NULL,
  `quantity_types_rooms` int DEFAULT NULL,
  `max_visitors_in_a_room` int DEFAULT NULL,
  `number_price` float DEFAULT NULL,
  `amount_extra` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `change_policy_number`
--

LOCK TABLES `change_policy_number` WRITE;
/*!40000 ALTER TABLE `change_policy_number` DISABLE KEYS */;
/*!40000 ALTER TABLE `change_policy_number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `comment` (
  `id` int NOT NULL AUTO_INCREMENT,
  `content` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `room_id` int NOT NULL,
  `user_id` int NOT NULL,
  `created_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `room_id` (`room_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `room` (`id`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,'đâsdsa',11,1,'2022-01-09 09:51:51'),(2,'Phòng tốt',13,1,'2022-01-09 09:51:51'),(3,'Phòng tuyệt vời',13,1,'2022-01-09 09:51:51'),(4,'đẹp',6,1,'2022-01-11 09:34:46'),(5,'Phòng tôts',6,1,'2022-01-11 09:34:46');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receipt`
--

DROP TABLE IF EXISTS `receipt`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receipt` (
  `id` int NOT NULL AUTO_INCREMENT,
  `visitor_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `address` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `price` float DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipt`
--

LOCK TABLES `receipt` WRITE;
/*!40000 ALTER TABLE `receipt` DISABLE KEYS */;
/*!40000 ALTER TABLE `receipt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receipt_detail`
--

DROP TABLE IF EXISTS `receipt_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receipt_detail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `room_id` int NOT NULL,
  `room_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `price` float DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `receive_day` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `pay_day` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `person_amount` int DEFAULT NULL,
  `receipt_id` int DEFAULT NULL,
  PRIMARY KEY (`id`,`room_id`),
  KEY `room_id` (`room_id`),
  KEY `receipt_detail_ibfk_2` (`receipt_id`),
  CONSTRAINT `receipt_detail_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `room` (`id`),
  CONSTRAINT `receipt_detail_ibfk_2` FOREIGN KEY (`receipt_id`) REFERENCES `receipt` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=199 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receipt_detail`
--

LOCK TABLES `receipt_detail` WRITE;
/*!40000 ALTER TABLE `receipt_detail` DISABLE KEYS */;
/*!40000 ALTER TABLE `receipt_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rental_voucher`
--

DROP TABLE IF EXISTS `rental_voucher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rental_voucher` (
  `id` int NOT NULL AUTO_INCREMENT,
  `booking_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=119 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rental_voucher`
--

LOCK TABLES `rental_voucher` WRITE;
/*!40000 ALTER TABLE `rental_voucher` DISABLE KEYS */;
INSERT INTO `rental_voucher` VALUES (1,'2022-01-04 19:56:56'),(2,'2022-01-04 20:05:09'),(3,'2022-01-04 20:05:21'),(4,'2022-01-04 20:11:53'),(5,'2022-01-04 20:15:04'),(6,'2022-01-04 20:15:30'),(7,'2022-01-04 20:15:46'),(8,'2022-01-04 20:16:08'),(9,'2022-01-04 20:17:21'),(10,'2022-01-04 20:17:30'),(11,'2022-01-04 20:17:40'),(12,'2022-01-04 20:18:16'),(13,'2022-01-04 20:18:25'),(14,'2022-01-04 20:18:34'),(15,'2022-01-04 20:18:49'),(16,'2022-01-04 20:19:05'),(17,'2022-01-04 20:20:04'),(18,'2022-01-04 20:21:23'),(19,'2022-01-04 20:21:33'),(20,'2022-01-04 20:21:37'),(21,'2022-01-04 20:22:20'),(22,'2022-01-04 20:24:17'),(23,'2022-01-04 20:25:53'),(24,'2022-01-04 20:26:11'),(25,'2022-01-04 20:27:15'),(26,'2022-01-04 20:27:46'),(27,'2022-01-04 20:28:52'),(28,'2022-01-04 20:30:25'),(29,'2022-01-04 20:41:19'),(30,'2022-01-04 20:45:10'),(31,'2022-01-05 09:50:24'),(32,'2022-01-06 11:38:50'),(33,'2022-01-06 21:17:12'),(34,'2022-01-07 08:29:13'),(35,'2022-01-07 08:30:43'),(36,'2022-01-07 08:37:33'),(37,'2022-01-07 08:41:10'),(38,'2022-01-07 08:41:29'),(39,'2022-01-07 08:41:37'),(40,'2022-01-07 08:42:50'),(41,'2022-01-07 08:45:18'),(42,'2022-01-07 08:58:41'),(43,'2022-01-07 09:18:05'),(44,'2022-01-07 09:18:47'),(45,'2022-01-07 09:28:43'),(46,'2022-01-07 09:29:20'),(47,'2022-01-07 09:30:52'),(48,'2022-01-07 09:31:53'),(49,'2022-01-07 09:37:15'),(50,'2022-01-07 09:39:24'),(51,'2022-01-07 10:49:58'),(52,'2022-01-07 10:52:27'),(53,'2022-01-07 10:53:14'),(54,'2022-01-07 10:55:14'),(55,'2022-01-07 10:55:24'),(56,'2022-01-07 10:57:33'),(57,'2022-01-07 10:57:41'),(58,'2022-01-07 10:58:06'),(59,'2022-01-07 11:00:02'),(60,'2022-01-07 11:00:14'),(61,'2022-01-07 11:00:38'),(62,'2022-01-07 11:04:05'),(63,'2022-01-07 11:06:18'),(64,'2022-01-07 13:15:34'),(65,'2022-01-07 13:17:05'),(66,'2022-01-07 13:17:16'),(67,'2022-01-07 13:18:05'),(68,'2022-01-07 13:20:00'),(69,'2022-01-07 13:21:52'),(70,'2022-01-07 13:22:49'),(71,'2022-01-07 13:23:55'),(72,'2022-01-07 13:26:06'),(73,'2022-01-07 13:47:19'),(74,'2022-01-07 13:47:59'),(75,'2022-01-07 13:48:49'),(76,'2022-01-07 13:49:28'),(77,'2022-01-07 13:51:08'),(78,'2022-01-07 13:52:57'),(79,'2022-01-07 13:53:52'),(80,'2022-01-07 13:58:20'),(81,'2022-01-07 20:15:08'),(82,'2022-01-08 10:51:40'),(83,'2022-01-08 11:08:08'),(84,'2022-01-08 11:23:36'),(85,'2022-01-08 11:27:56'),(86,'2022-01-08 11:28:48'),(87,'2022-01-08 11:30:34'),(88,'2022-01-08 11:33:46'),(89,'2022-01-08 11:36:46'),(90,'2022-01-08 11:39:20'),(91,'2022-01-08 11:40:20'),(92,'2022-01-08 11:41:54'),(93,'2022-01-08 11:42:23'),(94,'2022-01-08 11:44:16'),(95,'2022-01-08 11:44:42'),(96,'2022-01-08 11:45:37'),(97,'2022-01-08 11:47:27'),(98,'2022-01-08 11:48:13'),(99,'2022-01-08 11:50:45'),(100,'2022-01-08 11:51:14'),(101,'2022-01-08 11:51:50'),(102,'2022-01-08 11:55:17'),(103,'2022-01-08 12:12:11'),(104,'2022-01-08 15:34:53'),(105,'2022-01-08 15:37:04'),(106,'2022-01-08 17:28:26'),(107,'2022-01-08 17:30:02'),(108,'2022-01-08 17:36:19'),(109,'2022-01-08 17:37:52'),(110,'2022-01-08 17:38:28'),(111,'2022-01-08 17:39:31'),(112,'2022-01-08 17:46:59'),(113,'2022-01-08 17:47:36'),(114,'2022-01-09 10:05:52'),(115,'2022-01-09 15:42:54'),(116,'2022-01-11 08:55:37'),(117,'2022-01-11 13:54:48'),(118,'2022-01-12 10:35:07');
/*!40000 ALTER TABLE `rental_voucher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rental_voucher_detail`
--

DROP TABLE IF EXISTS `rental_voucher_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rental_voucher_detail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `visit_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `type_visit_id` int NOT NULL,
  `phone_number` int DEFAULT NULL,
  `rental_voucher_id` int NOT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `visit_name_id` int NOT NULL,
  `nation` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`,`type_visit_id`,`rental_voucher_id`),
  KEY `type_visit_id` (`type_visit_id`),
  KEY `rental_voucher_id` (`rental_voucher_id`),
  CONSTRAINT `rental_voucher_detail_ibfk_1` FOREIGN KEY (`type_visit_id`) REFERENCES `type_visit` (`id`),
  CONSTRAINT `rental_voucher_detail_ibfk_2` FOREIGN KEY (`rental_voucher_id`) REFERENCES `rental_voucher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=121 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rental_voucher_detail`
--

LOCK TABLES `rental_voucher_detail` WRITE;
/*!40000 ALTER TABLE `rental_voucher_detail` DISABLE KEYS */;
INSERT INTO `rental_voucher_detail` VALUES (1,'d',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(2,'d',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(3,'d',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(4,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(5,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(6,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(7,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(8,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(9,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(10,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(11,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(12,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(13,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(14,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(15,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(16,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(17,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(18,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(19,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(20,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(21,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(22,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(23,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(24,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(25,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(26,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(27,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(28,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(29,'HNNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(30,'HNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(31,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(32,'HNNN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(33,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(34,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(35,'HNN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(36,'HN',1,1692737598,1,'1954052027hieu@ou.edu.vn',1,'VN'),(37,'HN',1,1692737598,1,'hieund898@gmail.com',1,'VN'),(38,'HN',1,1692737598,1,'hieund898@gmail.com',1,'VN'),(39,'HN',1,1692737598,1,'hieund898@gmail.com',1,'VN'),(40,'HN',1,1692737598,1,'hieund898@gmail.com',1,'VN'),(41,'HN',1,1692737598,1,'hieund898@gmail.com',1,'VN'),(42,'HN',1,1692737598,1,'hieund898@gmail.com',1,'VN'),(43,'HN',1,1692737598,1,'hieund898@gmail.com',1,'VN'),(44,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(45,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(46,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(47,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(48,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(49,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(50,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(51,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'vn'),(52,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(53,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(54,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(55,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(56,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(57,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(58,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(59,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(60,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(61,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(62,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(63,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(64,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(65,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(66,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(67,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(68,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(69,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(70,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(71,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(72,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(73,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(74,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(75,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(76,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(77,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(78,'HNN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(79,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(80,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(81,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(82,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(83,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(84,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(85,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(86,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(87,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(88,'GN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(89,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(90,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(91,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(92,'a',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(93,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(94,'a',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(95,'a',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(96,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(97,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(98,'j',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(99,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(100,'hn',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(101,'hn',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(102,'hn',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(103,'hn',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(104,'a',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(105,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(106,'Nguyễn',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(107,'Nguyễn Đức Hiếu',1,1692737598,1,'hieutk200301@gmail.com',1,'Việt Nam'),(108,'HN',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(109,'Nguyễn Đức Hiếu',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(110,'Nguyễn Đức Hiếu',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(111,'Nguyễn Đức Hiếu',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(112,'Nguyễn Đức Hiếu',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(113,'Nguyễn Đức Hiếu',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(114,'Nguyễn Đức Hiếu',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(115,'Nguyễn Đức Hiếu',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(116,'Nguyễn Đức Hiếu',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(117,'Nguyễn Đức Hiếu',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(118,'Nguyễn Đức Hiếu',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(119,'Nguyễn Đức Hiếu',1,1692737598,1,'hieutk200301@gmail.com',1,'VN'),(120,'Nguyễn Đức Hiếu',1,1692737598,1,'hieutk200301@gmail.com',1,'VN');
/*!40000 ALTER TABLE `rental_voucher_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room` (
  `id` int NOT NULL AUTO_INCREMENT,
  `quantity_bed` int NOT NULL,
  `price` float NOT NULL,
  `status` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `type_room_id` int NOT NULL,
  `rental_voucher` int DEFAULT NULL,
  `image` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `descriptions` varchar(20000) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `type_room_id` (`type_room_id`),
  KEY `rental_voucher` (`rental_voucher`),
  CONSTRAINT `room_ibfk_1` FOREIGN KEY (`type_room_id`) REFERENCES `type_room` (`id`),
  CONSTRAINT `room_ibfk_2` FOREIGN KEY (`rental_voucher`) REFERENCES `rental_voucher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES (4,2,2450070,'Trống',1,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403256/rooms_images/suite-room-1_nfdg9o.jpg','Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry\'s standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum'),(5,2,2040060,'Trống',2,1,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403444/rooms_images/deluxe-room-1_wlxdqy.jpg','Nội dung mô tả'),(6,3,1679970,'Trống',3,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg','Nội dung mô tả'),(7,3,2450070,'Trống',1,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403256/rooms_images/suite-room-1_nfdg9o.jpg','Nội dung mô tả'),(8,3,2040060,'Trống',2,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403444/rooms_images/deluxe-room-1_wlxdqy.jpg','Nội dung mô tả'),(9,3,1134500,'Trống',4,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403690/rooms_images/standard-room-1_xfjsmn.jpg','Nội dung mô tả'),(10,3,1679970,'Trống',3,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg','Nội dung mô tả'),(11,3,1134500,'Trống',4,3,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403690/rooms_images/standard-room-1_xfjsmn.jpg','Nội dung mô tả'),(12,3,1679970,'Trống',3,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg','Nội dung mô tả'),(13,3,1679970,'Trống',3,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg','Nội dung mô tả'),(14,3,1679970,'Trống',3,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg','Nội dung mô tả'),(15,3,1679970,'Trống',3,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg','Nội dung mô tả'),(16,3,1679970,'Trống',3,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg','Nội dung mô tả'),(17,3,1679970,'Trống',3,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg','Nội dung mô tả'),(18,3,1679970,'Trống',3,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg','Nội dung mô tả'),(19,3,1679970,'Trống',3,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg','Nội dung mô tả'),(20,3,1679970,'Trống',3,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg','Nội dung mô tả'),(21,3,1679970,'Trống',3,2,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403591/rooms_images/superior-room-1_yf3plb.jpg','Nội dung mô tả'),(22,2,2040060,'Trống',2,3,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403444/rooms_images/deluxe-room-1_wlxdqy.jpg','Nd'),(24,2,2450070,'Trống',1,0,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403256/rooms_images/suite-room-1_nfdg9o.jpg','Nội dung mô tả'),(25,2,2450070,'Trống',1,0,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403256/rooms_images/suite-room-1_nfdg9o.jpg','Nội dung mô tả'),(26,2,2450070,'Trống',1,0,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403256/rooms_images/suite-room-1_nfdg9o.jpg','Nội dung mô tả'),(27,2,2450070,'Trống',1,0,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403256/rooms_images/suite-room-1_nfdg9o.jpg','Nội dung mô tả'),(28,2,2450070,'Trống',1,0,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403256/rooms_images/suite-room-1_nfdg9o.jpg','Nội dung mô tả'),(29,2,1134500,'Trống',4,0,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403690/rooms_images/standard-room-1_xfjsmn.jpg','Nội dung mô tả'),(30,2,1134500,'Trống',4,0,'https://res.cloudinary.com/dwgjmgf6o/image/upload/v1640403690/rooms_images/standard-room-1_xfjsmn.jpg','Nội dung mô tả');
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_room`
--

DROP TABLE IF EXISTS `type_room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type_room` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type_room_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_room`
--

LOCK TABLES `type_room` WRITE;
/*!40000 ALTER TABLE `type_room` DISABLE KEYS */;
INSERT INTO `type_room` VALUES (1,'Phòng Suite'),(2,'Phòng Deluxe'),(3,'Phòng Superior'),(4,'Phòng Standard');
/*!40000 ALTER TABLE `type_room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `type_visit`
--

DROP TABLE IF EXISTS `type_visit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `type_visit` (
  `id` int NOT NULL AUTO_INCREMENT,
  `type_visit_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `type_visit`
--

LOCK TABLES `type_visit` WRITE;
/*!40000 ALTER TABLE `type_visit` DISABLE KEYS */;
INSERT INTO `type_visit` VALUES (1,'Khách nội địa'),(2,'Khách nước ngoài');
/*!40000 ALTER TABLE `type_visit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `avatar` varchar(200) COLLATE utf8_unicode_ci DEFAULT NULL,
  `joined_date` datetime DEFAULT NULL,
  `user_role` enum('ADMIN','USER','EMPLOYEE') COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'hieund','202cb962ac59075b964b07152d234b70','hieund@gmail.com','https://res.cloudinary.com/dwgjmgf6o/image/upload/v1641054396/user_image/default_xojj6r.png','2022-01-02 17:10:38','USER'),(2,'Hieu123','e9fb3875bd395d2e47a75c41a2b596f6','1954052027hieu@ou.edu.vn','https://res.cloudinary.com/dwgjmgf6o/image/upload/v1641054396/user_image/default_xojj6r.png','2022-01-09 11:02:07','USER');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-01-12 11:09:07
