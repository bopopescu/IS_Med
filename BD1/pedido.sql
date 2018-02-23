-- MySQL Workbench Forward Engineering
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema pedido
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema pedido
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pedido` DEFAULT CHARACTER SET utf8 ;
USE `pedido` ;

-- -----------------------------------------------------
-- Table `pedido`.`Pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pedido`.`Pedido` (
  `idPedido` INT NOT NULL,
  `data` DATETIME(0) NOT NULL,
  `idDoente` INT NOT NULL,
  `nprocesso` INT NOT NULL,
  `morada` VARCHAR(45) NOT NULL,
  `telefone` INT NOT NULL,
  `estado` INT NOT NULL,
  PRIMARY KEY (`idPedido`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pedido`.`worklist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pedido`.`worklist` (
  `idworklist` INT NOT NULL,
  `idPedido` INT NOT NULL,
  `estado` INT NULL,
  PRIMARY KEY (`idworklist`),
  INDEX `fk_worklist_Pedido_idx` (`idPedido` ASC),
  CONSTRAINT `fk_worklist_Pedido`
    FOREIGN KEY (`idPedido`)
    REFERENCES `pedido`.`Pedido` (`idPedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
