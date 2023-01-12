-- Resets the attribute valid_email only when the email has been changed
delimiter ##
CREATE TRIGGER reset BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email NOT LIKE OLD.email THEN
		SET NEW.valid_email = '0';
	END IF;
END; ##
