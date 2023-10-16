--Write a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number
DELIMITER $$

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 2)
BEGIN
    IF b = 0 THEN
        RETURN 0.00;
    ELSE
        RETURN a / b;
    END IF;
END $$

DELIMITER ;
