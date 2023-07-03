-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: ma_base
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add emploi du temps',6,'add_emploidutemps'),(22,'Can change emploi du temps',6,'change_emploidutemps'),(23,'Can delete emploi du temps',6,'delete_emploidutemps'),(24,'Can view emploi du temps',6,'view_emploidutemps'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add account_request',8,'add_account_request'),(30,'Can change account_request',8,'change_account_request'),(31,'Can delete account_request',8,'delete_account_request'),(32,'Can view account_request',8,'view_account_request');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authentification_account_request`
--

DROP TABLE IF EXISTS `authentification_account_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authentification_account_request` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(63) NOT NULL,
  `email` varchar(63) NOT NULL,
  `num_id` int NOT NULL,
  `is_approved` tinyint(1) NOT NULL,
  `password` varchar(63) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentification_account_request`
--

LOCK TABLES `authentification_account_request` WRITE;
/*!40000 ALTER TABLE `authentification_account_request` DISABLE KEYS */;
INSERT INTO `authentification_account_request` VALUES (3,'mariama','jules.agassoussi2005@gmail.com',170,1,'3333aaaa'),(7,'leo','agassoussisalwane2@gmail.com',1245,1,'0000aaaa');
/*!40000 ALTER TABLE `authentification_account_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authentification_user`
--

DROP TABLE IF EXISTS `authentification_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authentification_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `num_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentification_user`
--

LOCK TABLES `authentification_user` WRITE;
/*!40000 ALTER TABLE `authentification_user` DISABLE KEYS */;
INSERT INTO `authentification_user` VALUES (1,'pbkdf2_sha256$260000$vLJiaCWSPLkvjKxAS1yt2Q$I/DtdBByIHjeNBEdJa8jDNrWvmGpVgXTukbbiM0cpNY=','2023-07-02 02:25:04.855036',0,'toto','','','',0,1,'2023-07-02 00:31:04.894143',1234),(2,'pbkdf2_sha256$260000$0OFiXYr8mCBWRK80I0ESHH$ZDSGfyVEJoexiYjF/+YnKhH9ri/SCnufw2JmIlfcwVY=','2023-07-03 12:47:29.644775',1,'jules','','','',1,1,'2023-07-02 02:34:56.095105',1234),(3,'pbkdf2_sha256$260000$fz0ihi9Nzv3LJCd5xJHGLp$0+++ikQ6SKAhmoBhSTFLjNeWH8qvCbNmhqlrdo+AM44=','2023-07-02 07:53:58.635213',0,'salboss','','','jules@gmail.com',0,1,'2023-07-02 07:53:57.977786',17),(4,'pbkdf2_sha256$260000$k9FcpN2Jgvbhz5xsKurode$l/8HvoSxmcIpO5Bt2ErxYzj7IJv9n79edRmqRHhfPYw=','2023-07-03 17:39:34.076521',0,'jokair','','','jules.agassoussi2005@gmail.com',0,1,'2023-07-02 11:02:17.727764',170),(7,'pbkdf2_sha256$260000$VboANKN5Vk3B9AnmT6Puhl$t0A1zAaZW5M3974enRwXv6l/eEwhMy0LU8oeD4/59NU=','2023-07-03 06:44:56.378150',0,'mariama','','','jules.agassoussi2005@gmail.com',0,1,'2023-07-02 19:42:31.118406',170),(11,'pbkdf2_sha256$260000$1Nq4Nso4LDEfjzrumHNglH$kbWymKgDQohgJxY8OP7A0H30W3I6xcuFmoXk84jGB/c=','2023-07-02 22:57:32.489000',0,'leo','','','agassoussisalwane2@gmail.com',0,1,'2023-07-02 22:54:37.720566',1245),(12,'pbkdf2_sha256$260000$EbBceiAOUJHJPCZlnF91tN$wZhd6frwEqKyX7x/3mmobKhCf0rvK3E67+j3X7Npgrw=',NULL,1,'fat','','','agassoussisalwane2@gmail.com',0,1,'2023-07-02 23:17:34.366607',333312);
/*!40000 ALTER TABLE `authentification_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authentification_user_groups`
--

DROP TABLE IF EXISTS `authentification_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authentification_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `authentification_user_groups_user_id_group_id_8756f2ae_uniq` (`user_id`,`group_id`),
  KEY `authentification_user_groups_group_id_81eeee0f_fk_auth_group_id` (`group_id`),
  CONSTRAINT `authentification_use_user_id_43be5d3c_fk_authentif` FOREIGN KEY (`user_id`) REFERENCES `authentification_user` (`id`),
  CONSTRAINT `authentification_user_groups_group_id_81eeee0f_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentification_user_groups`
--

LOCK TABLES `authentification_user_groups` WRITE;
/*!40000 ALTER TABLE `authentification_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `authentification_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authentification_user_user_permissions`
--

DROP TABLE IF EXISTS `authentification_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authentification_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `authentification_user_us_user_id_permission_id_0505c2b8_uniq` (`user_id`,`permission_id`),
  KEY `authentification_use_permission_id_62750d9c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `authentification_use_permission_id_62750d9c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `authentification_use_user_id_576a50aa_fk_authentif` FOREIGN KEY (`user_id`) REFERENCES `authentification_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentification_user_user_permissions`
--

LOCK TABLES `authentification_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `authentification_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `authentification_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_authentification_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_authentification_user_id` FOREIGN KEY (`user_id`) REFERENCES `authentification_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(8,'authentification','account_request'),(7,'authentification','user'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(6,'timetable','emploidutemps');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'timetable','0001_initial','2023-07-01 18:51:12.374634'),(2,'contenttypes','0001_initial','2023-07-01 18:51:12.543530'),(3,'contenttypes','0002_remove_content_type_name','2023-07-01 19:09:31.089370'),(4,'auth','0001_initial','2023-07-01 19:09:31.651848'),(5,'auth','0002_alter_permission_name_max_length','2023-07-01 19:09:31.931245'),(6,'auth','0003_alter_user_email_max_length','2023-07-01 19:09:31.970861'),(7,'auth','0004_alter_user_username_opts','2023-07-01 19:09:32.009123'),(8,'auth','0005_alter_user_last_login_null','2023-07-01 19:09:32.043459'),(9,'auth','0006_require_contenttypes_0002','2023-07-01 19:09:32.053827'),(10,'auth','0007_alter_validators_add_error_messages','2023-07-01 19:09:32.076572'),(11,'auth','0008_alter_user_username_max_length','2023-07-01 19:09:32.094877'),(12,'auth','0009_alter_user_last_name_max_length','2023-07-01 19:09:32.120707'),(13,'auth','0010_alter_group_name_max_length','2023-07-01 19:09:32.170734'),(14,'auth','0011_update_proxy_permissions','2023-07-01 19:09:32.208468'),(15,'auth','0012_alter_user_first_name_max_length','2023-07-01 19:09:32.229262'),(16,'authentification','0001_initial','2023-07-01 19:09:32.991023'),(17,'admin','0001_initial','2023-07-01 19:09:33.401741'),(18,'admin','0002_logentry_remove_auto_add','2023-07-01 19:09:33.459209'),(19,'admin','0003_logentry_add_action_flag_choices','2023-07-01 19:09:33.512707'),(20,'sessions','0001_initial','2023-07-01 19:09:33.667573'),(21,'timetable','0002_auto_20230628_1452','2023-07-01 19:09:35.391625'),(22,'timetable','0003_rename_emploi_emploidutemps_emploi_data','2023-07-01 19:09:35.436993'),(23,'timetable','0004_emploidutemps_published_date','2023-07-01 19:09:35.475691'),(24,'timetable','0005_auto_20230630_1726','2023-07-01 19:09:37.728247'),(25,'timetable','0006_alter_adminuser_options','2023-07-01 19:09:37.790681'),(26,'timetable','0007_alter_adminuser_options','2023-07-01 19:09:37.830866'),(27,'timetable','0008_remove_adminuser_a_email','2023-07-01 19:09:37.963783'),(28,'timetable','0009_adminuser_a_email','2023-07-01 19:09:38.147003'),(29,'timetable','0010_alter_adminuser_a_email','2023-07-01 19:09:38.190419'),(30,'timetable','0011_alter_adminuser_a_email','2023-07-01 19:09:38.240612'),(31,'timetable','0012_remove_adminuser_a_email','2023-07-01 19:09:38.380306'),(32,'timetable','0013_adminuser_a_email','2023-07-01 19:09:38.567765'),(33,'timetable','0014_alter_adminuser_a_email','2023-07-01 19:09:38.714235'),(34,'timetable','0015_alter_adminuser_a_email','2023-07-01 19:09:38.833460'),(35,'timetable','0016_alter_adminuser_username','2023-07-01 19:09:38.947081'),(36,'timetable','0017_auto_20230701_1642','2023-07-01 19:09:39.316437'),(37,'timetable','0018_user','2023-07-01 19:09:40.333580'),(38,'timetable','0019_auto_20230701_1917','2023-07-01 19:09:41.270017'),(39,'timetable','0020_auto_20230701_1951','2023-07-01 19:09:42.315022'),(40,'timetable','0021_delete_user','2023-07-01 19:09:42.508061'),(41,'authentification','0002_account_request','2023-07-02 16:45:05.720323'),(42,'authentification','0003_account_request_password','2023-07-02 17:53:29.908589');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `timetable_emploidutemps`
--

DROP TABLE IF EXISTS `timetable_emploidutemps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `timetable_emploidutemps` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `emploi_data` json NOT NULL DEFAULT (_utf8mb3'{"valeur": "par_defaut"}'),
  `published_date` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `timetable_emploidutemps`
--

LOCK TABLES `timetable_emploidutemps` WRITE;
/*!40000 ALTER TABLE `timetable_emploidutemps` DISABLE KEYS */;
INSERT INTO `timetable_emploidutemps` VALUES (1,'{\"j_7_8\": \"\", \"j_8_9\": \"\", \"l_7_8\": \"\", \"l_8_9\": \"valide\", \"m_7_8\": \"\", \"m_8_9\": \"\", \"s_7_8\": \"\", \"s_8_9\": \"\", \"v_7_8\": \"\", \"v_8_9\": \"\", \"j_9_10\": \"\", \"l_9_10\": \"\", \"m_9_10\": \"\", \"me_7_8\": \"\", \"me_8_9\": \"\", \"s_9_10\": \"\", \"v_9_10\": \"\", \"filiere\": \"IA\", \"j_10_11\": \"\", \"j_11_12\": \"\", \"j_12_13\": \"\", \"j_13_14\": \"\", \"j_14_15\": \"\", \"j_15_16\": \"\", \"j_16_17\": \"\", \"j_17_18\": \"\", \"j_18_19\": \"\", \"l_10_11\": \"\", \"l_11_12\": \"\", \"l_12_13\": \"\", \"l_13_14\": \"\", \"l_14_15\": \"\", \"l_15_16\": \"\", \"l_16_17\": \"\", \"l_17_18\": \"\", \"l_18_19\": \"\", \"m_10_11\": \"\", \"m_11_12\": \"\", \"m_12_13\": \"\", \"m_13_14\": \"\", \"m_14_15\": \"\", \"m_15_16\": \"\", \"m_16_17\": \"\", \"m_17_18\": \"\", \"m_18_19\": \"\", \"me_9_10\": \"\", \"s_10_11\": \"\", \"s_11_12\": \"\", \"s_12_13\": \"\", \"s_13_14\": \"\", \"s_14_15\": \"\", \"s_15_16\": \"\", \"s_16_17\": \"\", \"s_17_18\": \"\", \"s_18_19\": \"\", \"v_10_11\": \"\", \"v_11_12\": \"\", \"v_12_13\": \"\", \"v_13_14\": \"\", \"v_14_15\": \"\", \"v_15_16\": \"\", \"v_16_17\": \"\", \"v_17_18\": \"\", \"v_18_19\": \"\", \"me_10_11\": \"\", \"me_11_12\": \"jacques est la\", \"me_12_13\": \"\", \"me_13_14\": \"\", \"me_14_15\": \"\", \"me_15_16\": \"\", \"me_16_17\": \"\", \"me_17_18\": \"\", \"me_18_19\": \"\", \"description\": \"  fff  \"}','2023-07-02 01:09:01.104192'),(2,'{\"j_7_8\": \"\", \"j_8_9\": \"\", \"l_7_8\": \"mathématiques\", \"l_8_9\": \"\", \"m_7_8\": \"\", \"m_8_9\": \"\", \"s_7_8\": \"\", \"s_8_9\": \"\", \"v_7_8\": \"\", \"v_8_9\": \"\", \"j_9_10\": \"\", \"l_9_10\": \"\", \"m_9_10\": \"\", \"me_7_8\": \"\", \"me_8_9\": \"\", \"s_9_10\": \"\", \"v_9_10\": \"\", \"filiere\": \"si\", \"j_10_11\": \"\", \"j_11_12\": \"\", \"j_12_13\": \"\", \"j_13_14\": \"\", \"j_14_15\": \"\", \"j_15_16\": \"\", \"j_16_17\": \"\", \"j_17_18\": \"\", \"j_18_19\": \"\", \"l_10_11\": \"\", \"l_11_12\": \"\", \"l_12_13\": \"\", \"l_13_14\": \"\", \"l_14_15\": \"\", \"l_15_16\": \"\", \"l_16_17\": \"\", \"l_17_18\": \"\", \"l_18_19\": \"\", \"m_10_11\": \"\", \"m_11_12\": \"\", \"m_12_13\": \"\", \"m_13_14\": \"\", \"m_14_15\": \"\", \"m_15_16\": \"\", \"m_16_17\": \"\", \"m_17_18\": \"\", \"m_18_19\": \"\", \"me_9_10\": \"\", \"s_10_11\": \"\", \"s_11_12\": \"\", \"s_12_13\": \"\", \"s_13_14\": \"\", \"s_14_15\": \"\", \"s_15_16\": \"\", \"s_16_17\": \"\", \"s_17_18\": \"\", \"s_18_19\": \"\", \"v_10_11\": \"\", \"v_11_12\": \"\", \"v_12_13\": \"\", \"v_13_14\": \"\", \"v_14_15\": \"\", \"v_15_16\": \"physique\", \"v_16_17\": \"\", \"v_17_18\": \"\", \"v_18_19\": \"\", \"me_10_11\": \"\", \"me_11_12\": \"\", \"me_12_13\": \"\", \"me_13_14\": \"\", \"me_14_15\": \"\", \"me_15_16\": \"\", \"me_16_17\": \"\", \"me_17_18\": \"economie\", \"me_18_19\": \"\", \"description\": \"  devoir dans la semaine du lundi 15  \"}','2023-07-02 02:20:02.395506'),(3,'{\"j_7_8\": \"\", \"j_8_9\": \"\", \"l_7_8\": \"\", \"l_8_9\": \"DEV WEB\", \"m_7_8\": \"\", \"m_8_9\": \"\", \"s_7_8\": \"\", \"s_8_9\": \"\", \"v_7_8\": \"\", \"v_8_9\": \"\", \"j_9_10\": \"\", \"l_9_10\": \"\", \"m_9_10\": \"\", \"me_7_8\": \"\", \"me_8_9\": \"\", \"s_9_10\": \"\", \"v_9_10\": \"\", \"filiere\": \"GL\", \"j_10_11\": \"\", \"j_11_12\": \"\", \"j_12_13\": \"\", \"j_13_14\": \"\", \"j_14_15\": \"\", \"j_15_16\": \"\", \"j_16_17\": \"\", \"j_17_18\": \"\", \"j_18_19\": \"\", \"l_10_11\": \"\", \"l_11_12\": \"\", \"l_12_13\": \"\", \"l_13_14\": \"\", \"l_14_15\": \"\", \"l_15_16\": \"\", \"l_16_17\": \"\", \"l_17_18\": \"\", \"l_18_19\": \"\", \"m_10_11\": \"\", \"m_11_12\": \"\", \"m_12_13\": \"\", \"m_13_14\": \"\", \"m_14_15\": \"\", \"m_15_16\": \"\", \"m_16_17\": \"\", \"m_17_18\": \"\", \"m_18_19\": \"\", \"me_9_10\": \"\", \"s_10_11\": \"\", \"s_11_12\": \"\", \"s_12_13\": \"\", \"s_13_14\": \"\", \"s_14_15\": \"\", \"s_15_16\": \"\", \"s_16_17\": \"\", \"s_17_18\": \"\", \"s_18_19\": \"\", \"v_10_11\": \"\", \"v_11_12\": \"\", \"v_12_13\": \"\", \"v_13_14\": \"infographie\", \"v_14_15\": \"\", \"v_15_16\": \"\", \"v_16_17\": \"\", \"v_17_18\": \"\", \"v_18_19\": \"\", \"me_10_11\": \"\", \"me_11_12\": \"\", \"me_12_13\": \"\", \"me_13_14\": \"\", \"me_14_15\": \"\", \"me_15_16\": \"\", \"me_16_17\": \"\", \"me_17_18\": \"\", \"me_18_19\": \"\", \"description\": \"Iran2 est  occuper pour cette semaine vous travaillerez a padtice.\\r\\nCordialement,\\r\\nle SG\"}','2023-07-03 09:20:46.170448'),(4,'{\"j_7_8\": \"\", \"j_8_9\": \"\", \"l_7_8\": \"math igénieur\", \"l_8_9\": \"\", \"m_7_8\": \"\", \"m_8_9\": \"\", \"s_7_8\": \"\", \"s_8_9\": \"\", \"v_7_8\": \"\", \"v_8_9\": \"\", \"j_9_10\": \"\", \"l_9_10\": \"\", \"m_9_10\": \"\", \"me_7_8\": \"\", \"me_8_9\": \"\", \"s_9_10\": \"\", \"v_9_10\": \"\", \"filiere\": \"IA\", \"j_10_11\": \"mathématiques\", \"j_11_12\": \"\", \"j_12_13\": \"\", \"j_13_14\": \"\", \"j_14_15\": \"\", \"j_15_16\": \"\", \"j_16_17\": \"\", \"j_17_18\": \"\", \"j_18_19\": \"\", \"l_10_11\": \"\", \"l_11_12\": \"\", \"l_12_13\": \"\", \"l_13_14\": \"\", \"l_14_15\": \"\", \"l_15_16\": \"\", \"l_16_17\": \"\", \"l_17_18\": \"\", \"l_18_19\": \"\", \"m_10_11\": \"\", \"m_11_12\": \"\", \"m_12_13\": \"\", \"m_13_14\": \"electromagnétisme\", \"m_14_15\": \"\", \"m_15_16\": \"\", \"m_16_17\": \"\", \"m_17_18\": \"\", \"m_18_19\": \"\", \"me_9_10\": \"\", \"s_10_11\": \"\", \"s_11_12\": \"\", \"s_12_13\": \"\", \"s_13_14\": \"\", \"s_14_15\": \"\", \"s_15_16\": \"\", \"s_16_17\": \"\", \"s_17_18\": \"\", \"s_18_19\": \"\", \"v_10_11\": \"\", \"v_11_12\": \"\", \"v_12_13\": \"\", \"v_13_14\": \"\", \"v_14_15\": \"\", \"v_15_16\": \"\", \"v_16_17\": \"\", \"v_17_18\": \"\", \"v_18_19\": \"\", \"me_10_11\": \"\", \"me_11_12\": \"\", \"me_12_13\": \"\", \"me_13_14\": \"\", \"me_14_15\": \"\", \"me_15_16\": \"\", \"me_16_17\": \"\", \"me_17_18\": \"\", \"me_18_19\": \"\", \"description\": \" On compte sur vous pour le concours ,  ramener nous le trophée a la maison , enfin a l\'école ....\"}','2023-07-03 09:49:38.895370');
/*!40000 ALTER TABLE `timetable_emploidutemps` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-03 19:01:47
