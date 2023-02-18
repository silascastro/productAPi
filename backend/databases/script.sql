-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema test
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema test
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `test` DEFAULT CHARACTER SET utf8 ;
USE `test` ;

-- -----------------------------------------------------
-- Table `test`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`category` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(128) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test`.`product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`product` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(60) NULL,
  `price` DOUBLE NULL,
  `serie` INT NULL,
  `image` VARCHAR(250) NULL,
  `category_id` INT NOT NULL,
  PRIMARY KEY (`id`, `category_id`),
  INDEX `fk_product_category_idx` (`category_id` ASC) VISIBLE,
  CONSTRAINT `fk_product_category`
    FOREIGN KEY (`category_id`)
    REFERENCES `test`.`category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `test`.`review`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `test`.`review` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(40) NULL,
  `comentary` VARCHAR(128) NULL,
  `rate` INT NULL,
  `product_id` INT NOT NULL,
  `product_category_id` INT NOT NULL,
  PRIMARY KEY (`id`, `product_id`, `product_category_id`),
  INDEX `fk_review_product1_idx` (`product_id` ASC, `product_category_id` ASC) VISIBLE,
  CONSTRAINT `fk_review_product1`
    FOREIGN KEY (`product_id` , `product_category_id`)
    REFERENCES `test`.`product` (`id` , `category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
