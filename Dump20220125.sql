CREATE DATABASE  IF NOT EXISTS `moviedb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `moviedb`;
-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: localhost    Database: moviedb
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
-- Table structure for table `actor`
--

DROP TABLE IF EXISTS `actor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actor` (
  `Act_id` varchar(45) NOT NULL,
  `Act_name` varchar(45) DEFAULT NULL,
  `Act_gender` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`Act_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actor`
--

LOCK TABLES `actor` WRITE;
/*!40000 ALTER TABLE `actor` DISABLE KEYS */;
INSERT INTO `actor` VALUES ('20230','N. T. Rama Rao Jr.','Male'),('26264','Vijay Devarakonda','Male'),('39397','Naveen Kumar Gowda(Yash)','Male'),('55068','Anushka Shetty','Female'),('55129','Rana Daggubati','Male'),('66063','Samantha Ruth Prabhu','Female'),('74132','Tamannaah Bhatia','Female'),('99848','Prabhas Raju','Male');
/*!40000 ALTER TABLE `actor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `casting`
--

DROP TABLE IF EXISTS `casting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `casting` (
  `movie_id` varchar(45) NOT NULL,
  `Act_id` varchar(45) NOT NULL,
  `role` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`movie_id`,`Act_id`),
  KEY `Act_id_idx` (`Act_id`),
  CONSTRAINT `Act_id` FOREIGN KEY (`Act_id`) REFERENCES `actor` (`Act_id`) ON DELETE CASCADE,
  CONSTRAINT `movie_id` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`mov_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `casting`
--

LOCK TABLES `casting` WRITE;
/*!40000 ALTER TABLE `casting` DISABLE KEYS */;
INSERT INTO `casting` VALUES ('4224','20230','Hero'),('4224','66063','Heroine'),('7887','55068','Heroine'),('7887','55129','Villain'),('7887','99848','Hero'),('8646','39397','Hero');
/*!40000 ALTER TABLE `casting` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `director`
--

DROP TABLE IF EXISTS `director`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `director` (
  `director_id` int NOT NULL,
  `director_name` varchar(45) DEFAULT NULL,
  `director_phone` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`director_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `director`
--

LOCK TABLES `director` WRITE;
/*!40000 ALTER TABLE `director` DISABLE KEYS */;
INSERT INTO `director` VALUES (224,'SS Rajamouli','1234567890'),(466,'Boyapati Srinivas','1432567'),(827,'PrashanthNeel','53522614');
/*!40000 ALTER TABLE `director` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `mov_id` varchar(45) NOT NULL,
  `title` varchar(45) DEFAULT NULL,
  `release_year` int DEFAULT NULL,
  `language` varchar(45) DEFAULT NULL,
  `director_id` int DEFAULT NULL,
  `budget` int DEFAULT NULL,
  `genre` varchar(20) DEFAULT NULL,
  `prodn_id` int NOT NULL,
  PRIMARY KEY (`mov_id`),
  KEY `dir_id_idx` (`director_id`),
  CONSTRAINT `director_id` FOREIGN KEY (`director_id`) REFERENCES `director` (`director_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES ('3533','Magadheera',2016,'Telugu',224,10000000,'Family',41),('4224','RRR',2022,'Telugu',224,20000000,'Drama',54),('7887','Baahubali 1',2019,'Telugu',224,15000000,'Family',54),('8646','KGF 1',2019,'Kannada',827,15000000,'Family',78);
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `prod_company`
--

DROP TABLE IF EXISTS `prod_company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prod_company` (
  `prodn_id` int NOT NULL,
  `prodn_name` varchar(45) DEFAULT NULL,
  `prodn_addr` varchar(45) DEFAULT NULL,
  `tot_investment` int DEFAULT NULL,
  PRIMARY KEY (`prodn_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prod_company`
--

LOCK TABLES `prod_company` WRITE;
/*!40000 ALTER TABLE `prod_company` DISABLE KEYS */;
INSERT INTO `prod_company` VALUES (41,'Dharma Productions','Mumbai',10000000),(54,'Arka Media Works','Hyderabad',35000000),(78,'Hombale Films','Bengaluru',15000000);
/*!40000 ALTER TABLE `prod_company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ratings`
--

DROP TABLE IF EXISTS `ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ratings` (
  `mov_id` varchar(45) NOT NULL,
  `title` varchar(45) DEFAULT NULL,
  `rating` char(3) DEFAULT NULL,
  PRIMARY KEY (`mov_id`),
  CONSTRAINT `mov_id` FOREIGN KEY (`mov_id`) REFERENCES `movies` (`mov_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ratings`
--

LOCK TABLES `ratings` WRITE;
/*!40000 ALTER TABLE `ratings` DISABLE KEYS */;
INSERT INTO `ratings` VALUES ('4224','RRR','5'),('8646','KGF 1','5');
/*!40000 ALTER TABLE `ratings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `username` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  `question` varchar(45) DEFAULT NULL,
  `answer` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`username`,`password`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('DIlip','1234','Who\'s your best friend','Shivesh'),('Ganesh','4321','What\'s your nickname','Chitriki'),('Priyanka','1542','What\'s your favourite teacher name','Biradar'),('Shivesh','1010','What\'s your favourite teacher name','Annapurna');
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

-- Dump completed on 2022-01-25 10:05:45
