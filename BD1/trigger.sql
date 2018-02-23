DELIMITER $$ 
CREATE TRIGGER trigg_up AFTER INSERT ON pedido FOR EACH ROW
BEGIN
	INSERT INTO worklist(idPedido,estado) 
    VALUES (NEW.idPedido,new.estado);
END;

