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
-- Table `pedido`.`utente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pedido`.`utente` (
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
-- Table `pedido`.`pedido`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pedido`.`pedido` (
  `idPedido` INT(11) NOT NULL AUTO_INCREMENT,
  `data` INT(10) NOT NULL,
  `idDoente` INT(11) NOT NULL,
  `tipo` VARCHAR(2) NOT NULL,
  `descricao` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idPedido`),
  INDEX `fk_pedido_utente_idx` (`idDoente` ASC),
  CONSTRAINT `fk_pedido_utente`
    FOREIGN KEY (`idDoente`)
    REFERENCES `pedido`.`utente` (`idUtenteCC`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 19
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pedido`.`worklist`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pedido`.`worklist` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `msg` VARCHAR(400) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 30
DEFAULT CHARACTER SET = utf8;

USE `pedido`;

DELIMITER $$
USE `pedido`$$
CREATE
DEFINER=`root`@`localhost`
TRIGGER `pedido`.`trigg_up`
AFTER INSERT ON `pedido`.`pedido`
FOR EACH ROW
BEGIN
	INSERT INTO worklist(estado, idPedido)
    VALUES (0, NEW.idPedido);
END$$


DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
