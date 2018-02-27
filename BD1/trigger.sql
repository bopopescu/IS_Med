DELIMITER $$ 
CREATE TRIGGER trigg_up AFTER INSERT ON Pedido FOR EACH ROW
BEGIN
	INSERT INTO Worklist(idPedido,estado) 
    VALUES (NEW.idPedido,new.estado);
END;

