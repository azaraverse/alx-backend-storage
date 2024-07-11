-- A SQL script that creates a function SafeDiv that divides the first by the second number

-- Create function
DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS FLOAT DETERMINISTIC
BEGIN
    -- Declare variables
    DECLARE numerator INT;
    DECLARE denominator INT;
    DECLARE result;

    -- Set arguments to declared variables
    SET numerator = a;
    SET denominator = b;

    -- check if the denominator equals 0
    IF denominator = 0 THEN
        RETURN 0;
    -- Perform division if denominator passes
    ELSE SET result = numerator / denominator;
    END IF;

    RETURN result;

END $$
DELIMITER ;
