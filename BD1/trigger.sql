DELIMITER $$ 
CREATE TRIGGER trigg_up AFTER INSERT ON Pedido FOR EACH ROW
BEGIN
	INSERT INTO Worklist(idWorklist,idPedido,estado) 
    VALUES (NULL,NEW.idPedido,new.estado);
END;

