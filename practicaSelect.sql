CREATE DATABASE vacunaciones;
USE vacunaciones;
 -- crear una tabla llamada vacunas en la cual tengamos las sgts columnas:
	-- el id sera numerico y sera auto incrementable y primary key
	-- nombre de la vacuna que sera hasta 100 caracteres
    -- procedencia 20 caracteres
	-- lote 6 caracteres
CREATE TABLE vacunas(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)UNIQUE NOT NULL,
    procedencia VARCHAR(20)NOT NULL,
    lote char(6)
);

INSERT INTO vacunas (id, nombre, procedencia, lote) VALUES 
										(DEFAULT, 'PFIZER', 'EEUU', '123abc'),
										(DEFAULT, 'SPUTNIK', 'RUSA', '3d3afg'),
										(DEFAULT, 'ASTRAZENECA', 'CHINA', '5d8jh5'),
										(DEFAULT, 'CHINOPHARM', 'CHINA', 'n8gg84'),
										(DEFAULT, 'JHONSON & JHONSON', 'CHINA', 'b55b47');

-- devolver todas las vacunas que tengan el id 3
SELECT * FROM vacunas WHERE id = '3';
SELECT * FROM vacunas WHERE procedencia LIKE 'CHINA';
SELECT * FROM vacunas WHERE nombre LIKE '% %';
SELECT * FROM vacunas WHERE nombre LIKE '__I_O%';

SELECT * FROM vacunas;
SET SQL_SAFE_UPDATES = false;
DELETE FROM vacunas WHERE procedencia = 'RUSIA';
-- PK entero
-- direccion 100 caracteres
-- numero numeral no puede ser entero
-- atencion preferencial boolean no puede ser nulo
-- latitud y longitud de 2 enteros y 2 flotantes
CREATE TABLE vacunatorios(
	-- columnas propias de la tabla
		id INT PRIMARY KEY,
		direccion VARCHAR(100),
		numero INT NOT NULL,
		atencion_preferencial BOOLEAN DEFAULT TRUE NOT NULL, -- tambien puede ser 1 0 FALSE
		latitud FLOAT(4,2),
		longitud FLOAT(4,2),
        
	-- Columnas que van a cumplir como relaciones
		-- es buena practica usar el sigt formato:
			-- nombre_de_la_tabla_columna
		vacuna_id INT,
        
        -- RELACIONES
		FOREIGN KEY (vacuna_id) REFERENCES vacunas(id)
);