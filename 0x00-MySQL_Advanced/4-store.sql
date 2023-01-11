-- Decreases the quantity of an item afer adding a new order
CREATE TRIGGER decrease AFTER INSERT ON orders
FOR EACH ROW
	UPDATE items SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
