-- a script that creates a trigger that resets the attribute valid_email only when email has been changed

DELIMITER $$
CREATE TRIGGER reset_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET New.valid_email = 0
    END IF;
END $$
DELIMITER ;
