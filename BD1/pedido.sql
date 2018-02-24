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
-- Table `pedido`.`Utente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pedido`.`Utente` (
  `idUtenteCC` INT NOT NULL,
  `morada` VARCHAR(45) NOT NULL,
  `sexo` VARCHAR(1) NOT NULL,
  `telefone` INT NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUtenteCC`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pedido`.`Pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pedido`.`Pedido` (
  `idPedido` INT NOT NULL,
  `data` VARCHAR(45) NOT NULL,
  `estado` VARCHAR(5) NOT NULL,
  `descricao` VARCHAR(120) NOT NULL,
  `idUtenteCC` INT NOT NULL,
  PRIMARY KEY (`idPedido`),
  INDEX `fk_Pedido_Utente_idx` (`idUtenteCC` ASC),
  CONSTRAINT `fk_Pedido_Utente`
    FOREIGN KEY (`idUtenteCC`)
    REFERENCES `pedido`.`Utente` (`idUtenteCC`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pedido`.`Worklist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pedido`.`Worklist` (
  `idWorklist` INT NOT NULL AUTO_INCREMENT,
  `estado` VARCHAR(5) NOT NULL,
  `idPedido` INT NOT NULL,
  PRIMARY KEY (`idWorklist`),
  INDEX `fk_Worklist_Pedido1_idx` (`idPedido` ASC),
  CONSTRAINT `fk_Worklist_Pedido1`
    FOREIGN KEY (`idPedido`)
    REFERENCES `pedido`.`Pedido` (`idPedido`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
