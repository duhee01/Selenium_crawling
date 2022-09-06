CREATE SCHEMA IF NOT EXISTS `news_db` DEFAULT CHARACTER SET utf8;
USE `news_db` ;

CREATE TABLE `news_db`.`T_news` (
  `news_no` INT NOT NULL PRIMARY KEY,
  `title` VARCHAR(100) ,
  `date` DATETIME,
  `content` LONGTEXT
);

CREATE TABLE `news_db`.`T_keyword` (
  `keyword_no` INT NOT NULL PRIMARY KEY,
  `main_keyword` VARCHAR(10),
  `keyword_count` INT
);

CREATE TABLE `news_db`.`News_Keyword`(
	`News_Kmain` VARCHAR(10),
    `News_Kcount` INT,
    `News_Content`LONGTEXT,
	PRIMARY KEY(`News_Kmain`, `News_Kcount`)
);
