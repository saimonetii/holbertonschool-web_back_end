-- Script que crea un trigger para resetear valid_email si el email cambia
CREATE TRIGGER reset_valid_email BEFORE UPDATE ON users
FOR EACH ROW
SET NEW.valid_email = IF(OLD.email != NEW.email, 0, NEW.valid_email);
