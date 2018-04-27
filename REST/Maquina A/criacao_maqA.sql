-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema maquinaA
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema maquinaA
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `maquinaA` DEFAULT CHARACTER SET utf8 ;
USE `maquinaA` ;

-- -----------------------------------------------------
-- Table `maquinaA`.`Cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `maquinaA`.`Cliente` (
  `idClienteCC` INT NOT NULL,
  `nome` VARCHAR(90) NOT NULL,
  `dataNasc` VARCHAR(45) NOT NULL,
  `morada` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`idClienteCC`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `maquinaA`.`Exame`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `maquinaA`.`Exame` (
  `idExame` INT NOT NULL,
  `tipo` VARCHAR(90) NOT NULL,
  `data` DATETIME(45) NOT NULL,
  `relatorio` VARCHAR(450) NULL,
  `idClienteCC` INT NOT NULL,
  PRIMARY KEY (`idExame`),
  INDEX `fk_Exame_Cliente_idx` (`idClienteCC` ASC),
  CONSTRAINT `fk_Exame_Cliente`
    FOREIGN KEY (`idClienteCC`)
    REFERENCES `maquinaA`.`Cliente` (`idClienteCC`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;