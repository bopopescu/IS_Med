-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
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
  `idPedido` INT(11) NOT NULL AUTO_INCREMENT,
  `data` INT(1) NOT NULL,
  `idDoente` INT(11) NOT NULL,
  `tipo` VARCHAR(2) NOT NULL,
  `descricao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idPedido`))
ENGINE = InnoDB
AUTO_INCREMENT = 19
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pedido`.`Utente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pedido`.`Utente` (
  `idUtenteCC` INT(11) NOT NULL,
  `morada` VARCHAR(45) NOT NULL,
  `sexo` VARCHAR(1) NOT NULL,
  `telefone` INT(11) NOT NULL,
  `nome` VARCHAR(45) NOT NULL,
  `dataNasc` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idUtenteCC`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pedido`.`worklist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pedido`.`worklist` (
  `idworklist` INT(11) NOT NULL AUTO_INCREMENT,
  `estado` VARCHAR(2) NULL DEFAULT NULL,
  `idPedido` INT(11) NOT NULL,
  PRIMARY KEY (`idworklist`),
  INDEX `idPedido` (`idPedido` ASC),
  CONSTRAINT `worklist_ibfk_1`
    FOREIGN KEY (`idPedido`)
    REFERENCES `pedido`.`Pedido` (`idPedido`))
ENGINE = InnoDB
AUTO_INCREMENT = 12
DEFAULT CHARACTER SET = utf8;

USE `pedido`;

DELIMITER $$
USE `pedido`$$
CREATE
DEFINER=`root`@`localhost`
TRIGGER `pedido`.`trigg_up`
AFTER INSERT ON `pedido`.`Pedido`
FOR EACH ROW
BEGIN
	INSERT INTO worklist(estado, idPedido)
    VALUES (0, NEW.idPedido);
END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
