-- <- commentary syntax
-- Registro > conjunto de datos
-- Dato > un valor que por si solo no da una buena referencia
-- DB estan compuestas por una 
-- ; <- indica que la instruccion a culminado
CREATE DATABASE prueba;

-- sirve para indicar que DB se va a usar
USE prueba;

CREATE TaBLE productos(
	-- obligatoriamente pafra crear una tabla debemos crear un  columna
    -- Solamente se puede usar una vez el auto_increment por tabla
    -- primary key > indicamos que esta columna se comportara como la identificadora
    -- de todo este registro
    -- Nombre | Tipo de dato | [Configuraciones adicionales]
	id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    fecha_vencimiento DATE
);

-- DML <- Lenguaje de manipulacion de datyos|Data Manipulation Language 
	-- extraccion insercion actualiza elimina la info del DB
-- DDL <- Data definition language|Lenguaje de definicion de datos
	-- definir la estructura qe vamos a manejar en la DB
		-- (crear,modificar,elminar TABLAS Y db)
        
INSERT INTO productos(id,nombre,fecha_vencimiento)VALUES(DEFAULT,'Aguaymanto','2022-07-01');
INSERT INTO productos(id,nombre,fecha_vencimiento)VALUES(DEFAULT,'Cebolla','2022-07-10'),
														(DEFAULT,'Limon','2022-06-30');
-- hhh
-- Al momento de ingresar registros y si estamos manejando el autoincerementador y al momeneot de 
	-- realizar ... un registro este fallase el incrementador igual incrementa
SELECT nombre AS 'Nombre',fecha_vencimiento AS 'Fecha de Vencimiento',id AS 'ID' FROM productos;

-- traer todas las columnas
SELECT * FROM productos;
SELECT fecha_vencimiento AS 'Fecha de Vencimiento' FROM productos;
SELECT * FROM productos WHERE nombre='Cebolla';
SELECT * FROM productos WHERE nombre LIKE '%ll%';