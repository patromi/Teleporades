-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 35.189.109.28    Database: teleporada
-- ------------------------------------------------------
-- Server version	5.7.25-google-log

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '3ec1b2c2-138a-11eb-90ed-42010a9a0006:1-77782';

--
-- Table structure for table `lekarz`
--

DROP TABLE IF EXISTS `lekarz`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lekarz` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `imie` text COLLATE utf8mb4_polish_ci NOT NULL,
  `nazwisko` text COLLATE utf8mb4_polish_ci NOT NULL,
  `specjalizacja` text COLLATE utf8mb4_polish_ci NOT NULL,
  `klinika` text COLLATE utf8mb4_polish_ci NOT NULL,
  `idkliniki` int(11) NOT NULL,
  `login` text COLLATE utf8mb4_polish_ci NOT NULL,
  `haslo` text COLLATE utf8mb4_polish_ci NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lekarz`
--

LOCK TABLES `lekarz` WRITE;
/*!40000 ALTER TABLE `lekarz` DISABLE KEYS */;
INSERT INTO `lekarz` VALUES (38,'Patryk','Migaj','logopeeda','klinika',1,'',''),(39,'Patryk','Migaj','logopeeda','ewwe\r\n',2,'',''),(40,'Patryk','Migaj','logopeda','klinika',1,'',''),(41,'Patryk','Migaj','logopeda','klinika',1,'',''),(42,'Patryk','Migaj','logopeda','klinika',1,'',''),(43,'Paa','Miogg','logo','kli',2,'',''),(48,'Patryk','migaj','logopeda','Klinika imienia tadeusza kosciószki',2,'lekarz','pass'),(49,'Patryk','migaj','logopeda','Klinika imienia tadeusza kosciószki',2,'lekarz','pass'),(50,'Patryk','migaj','logopeda','Klinika imienia tadeusza kosciószki',2,'lekarz','pass'),(51,'Patryk','migaj','logopeda','Klinika imienia tadeusza kosciószki',2,'lekarz','pass'),(52,'Patryk','migaj','logopeda','Klinika imienia tadeusza kosciószki',2,'leewwewewez','pass'),(53,'Patryk','migaj','logopeda','Klinika imienia tadeusza kosciószki',2,'leewwewewez','pass'),(54,'Patryk','migaj','logopeda','Klinika imienia tadeusza kosci˘szki',2,'leewwewewez','pass'),(55,'Patryk','migaj','logopeda','Klinika imienia tadeusza kosciószki',2,'leewwewewez','pass'),(56,'kamilek','kamilek','kamilek','Klinika',1,'kamilek','kamilek'),(57,'kamilek','kamilek','kamilek','Klinika',1,'kamilek','kamilek'),(58,'radek2','radek2','radek2','Klinika',1,'radek2','radek2'),(59,'Patryk','migaj','logopeda','Klinika imienia tadeusza kosciószki',2,'leewwewewez','pass'),(60,'Patryk','migaj','logopeda','Klinika imienia tadeusza kosciószki',2,'leewwewewez','pass'),(61,'Patryk','migaj','logopeda','Klinika imienia tadeusza kosciószki',2,'leewwewewez','pass'),(62,'Patryk','migaj','logopeda','Klinika imienia tadeusza kosciószki',2,'leewwewewez','pass'),(63,'kamilek','kamilek','kamilek','Klinika',1,'kamilek','kamilek');
/*!40000 ALTER TABLE `lekarz` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `recepcja`
--

DROP TABLE IF EXISTS `recepcja`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `recepcja` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `login` text COLLATE utf8mb4_polish_ci NOT NULL,
  `haslo` text COLLATE utf8mb4_polish_ci NOT NULL,
  `nazwa` text COLLATE utf8mb4_polish_ci NOT NULL,
  `ulica` text COLLATE utf8mb4_polish_ci NOT NULL,
  `miasto` text COLLATE utf8mb4_polish_ci NOT NULL,
  `telefon` text COLLATE utf8mb4_polish_ci NOT NULL,
  `email` text COLLATE utf8mb4_polish_ci NOT NULL,
  `nrlokalu` text COLLATE utf8mb4_polish_ci NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `recepcja`
--

LOCK TABLES `recepcja` WRITE;
/*!40000 ALTER TABLE `recepcja` DISABLE KEYS */;
INSERT INTO `recepcja` VALUES (1,'admin','root','Klinika','ul.se','ostrow','043934','',''),(2,'w','w','w','w','w','w','',''),(11,'admin1','root12','klinika','asd','Ostrow','123456789','root12@','asd'),(12,'admin12','root12','Szpital','Groma','Ostrow','123456789','root123@op.pl','2'),(13,'admin2','root12','Jana Pawła 2','Groma','Ostrow','123456789','mikolaj@','1'),(14,'longlive','haslo','nazwa','lecznicza','ostów','+48 222 333 444','kontakt@kliniczki1h com','17'),(15,'longlive','haslo','nazwa','lecznicza','ost˘w','+48 222 333 444','kontakt@kliniczki1h com','17');
/*!40000 ALTER TABLE `recepcja` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `login` text COLLATE utf8mb4_polish_ci NOT NULL,
  `haslo` text COLLATE utf8mb4_polish_ci NOT NULL,
  `imie` text COLLATE utf8mb4_polish_ci NOT NULL,
  `nazwisko` text COLLATE utf8mb4_polish_ci NOT NULL,
  `leki` text COLLATE utf8mb4_polish_ci NOT NULL,
  `email` text COLLATE utf8mb4_polish_ci NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_polish_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (9,'user','root','Patryk','Migaj','',''),(13,'l','h','i','n','l',''),(18,'patromi','123','patr','qwe','brak','ewqqwe@wp.pl'),(19,'patromi','123','patr','qwe','brak','ewqqwe@wp.pl');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-10-25 23:47:09
