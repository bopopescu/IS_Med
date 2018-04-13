-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema maquinaB
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema maquinaB
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `maquinaB` DEFAULT CHARACTER SET utf8 ;
USE `maquinaB` ;

-- -----------------------------------------------------
-- Table `maquinaB`.`Exame`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `maquinaB`.`Exame` (
  `idExame` INT NOT NULL,
  `idCilenteCC` INT NOT NULL,
  `tipo` VARCHAR(45) NOT NULL,
  `data` DATETIME(45) NOT NULL,
  `realizou` TINYINT(1) NOT NULL,
  `relatorio` VARCHAR(450) NULL,
  PRIMARY KEY (`idExame`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
