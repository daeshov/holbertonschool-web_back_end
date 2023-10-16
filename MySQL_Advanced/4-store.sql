-- Decrease the item quantity for the item associated with the new order
CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE items
  SET quantity = quantity - 1
  WHERE item_id = NEW.item_id;
END;
$$
DELIMITER ;
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE items.name = NEW.item_name;