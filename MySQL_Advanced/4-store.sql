DELIMITER $$
CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  -- Decrease the item quantity for the item associated with the new order
  UPDATE items
  SET quantity = quantity - 1
  WHERE item_id = NEW.item_id;
END;
$$
DELIMITER ;