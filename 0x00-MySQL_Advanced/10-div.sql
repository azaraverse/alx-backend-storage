-- A SQL script that creates a function SafeDiv that divides the first by the second number

-- Create function
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT DETERMINISTIC
BEGIN
    -- Declare return variable
    DECLARE result FLOAT;

    -- check if the denominator equals 0
    IF b = 0 THEN
        RETURN 0;
    -- Perform division if denominator passes
    ELSE SET result = a / b;
    END IF;

    RETURN result;

END $$
DELIMITER ;
