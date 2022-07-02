CREATE DATABASE vacunaciones02;
USE vacunaciones02;
CREATE TABLE vacunas02(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100)UNIQUE NOT NULL,
    procedencia VARCHAR(20) NOT NULL,
    lote CHAR(6)
);
INSERT INTO vacunas02 (id, nombre, procedencia, lote) VALUES 
										(DEFAULT, 'PFIZER', 'EEUU', '123abc'),
										(DEFAULT, 'SPUTNIK', 'RUSA', '3d3afg'),
										(DEFAULT, 'ASTRAZENECA', 'CHINA', '5d8jh5'),
										(DEFAULT, 'CHINOPHARM', 'CHINA', 'n8gg84'),
										(DEFAULT, 'JHONSON & JHONSON', 'EEUU', 'b55b47');
-- id=3, de china, nombre con espacio, tercer caracter letter "I" y quinta "O"
SELECT * FROM vacunas02 WHERE id=3;
SELECT * FROM vacunas02 WHERE nombre="CHINA";
SELECT * FROM vacunas02 WHERE nombre LIKE '% %';
SELECT * FROM vacunas02 WHERE nombre LIKE '__I_O%';

CREATE TABLE vacunatorios02(
	id INT AUTO_INCREMENT PRIMARY KEY,
    direccion VARCHAR(100),
    numero INT NOT NULL,
    atencion_preferencial BOOL NOT NULL DEFAULT TRUE,
    latitud FLOAT(4,2),
    longitud DECIMAL(4,2),
    
    vacuna_id INT,
    -- creacion de relaciones
    FOREIGN KEY (vacuna_id) REFERENCES vacunas02(id)
);

INSERT INTO vacunatorios02(id, direccion,numero,atencion_preferencial,latitud,longitud,vacuna_id)VALUES
	(DEFAULT,'CALLE LOS PALITOS',123,TRUE,10.53,14.80,1),
    (DEFAULT,'AV GIRASOL',1213,FALSE,12.53,19.80,1),
    (DEFAULT,'HOSP. GENERAL',111,DEFAULT,12.49,80.15,2),
    (DEFAULT,'POSTA CERRO 7 COLORES',1485,DEFAULT,10.53,14.80,3),
    (DEFAULT,'ESTADIO LOS AGUATEROS',1489,FALSE,20.52,18.10,4),
    (DEFAULT,'PLAZA DE ARMAS',1256,FALSE,12.54,17.26,4)
;

-- Eliminacion de columna
ALTER TABLE vacunatorios02 DROP COLUMN id;

-- agreagr una columna, en este caso la id con sus propiedades y que sea la primera
	-- primera --> FIRST
	-- ultima --> esta por default pero a veces para asegurarse se pone LEFT
    -- despues de --> AFTER columnName
ALTER TABLE vacunatorios02 ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY FIRST;

-- return the directions que tengan atencion preferencial
-- return the directions que se encuentren entre lat>20 y long<20
-- return directions que sean pfizer(1) y que tengan atencion preferencial
-- return directions cuya vacuna no sea pfizer(1) (diferente !=0) o tengan atencion preferencial
SELECT direccion, numero FROM vacunatorios02 WHERE atencion_preferencial=TRUE;
SELECT direccion FROM vacunatorios02 WHERE latitud>20.00 AND longitud<20.00;
SELECT direccion FROM vacunatorios02 WHERE vacuna_id=1 AND atencion_preferencial=TRUE;
SELECT direccion FROM vacunatorios02 WHERE vacuna_id!=1 OR atencion_preferencial=TRUE;

-- JOINS
	-- todas las columnas de la tabla vacunas cuya interseccion con la tabla vacunatorios 
		-- y tenga 
SELECT * FROM vacunas02 INNER JOIN vacunatorios02 ON vacunas02.id=vacunatorios02.vacuna_id;

-- left join
	-- traera todo lo de la izquierda y si es que hay alguna coincidencia con lo de la derecha
SELECT * FROM vacunas02 LEFT JOIN vacunatorios02 ON vacunas02.id=vacunatorios02.vacuna_id;

--
INSERT INTO vacunatorios02 (id, direccion, numero, atencion_preferencial, latitud, longitud, vacuna_id) VALUES
						 (default, 'CALLE SIN NUMERO', 123, False, 10.00, 10.00, null);
                         
-- RIGHT JOIN
SELECT * FROM vacunas02 RIGHT JOIN vacunatorios02 ON vacunas02.id=vacunatorios02.vacuna_id;

-- --
SELECT vacunas02.id, vacunatorios02.id FROM vacunas02 INNER JOIN vacunatorios02 ON vacunas02.id=vacunatorios02.vacuna_id;

--
SELECT A.id, B.id FROM vacunas02 AS A INNER JOIN vacunatorios02 AS B ON A.id=B.vacuna_id;
--
SELECT A.id as 'Id de las vacunas', B.id AS 'Id de los vacunatorios'
FROM vacunas02 AS A INNER JOIN vacunatorios02 AS B ON A.id=B.vacuna_id;

--

CREATE TABLE campanias(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    fecha DATE,
    descripcion TEXT -- es como el varchar (dependiendo de cuantos caracteres guardemos, seperaremos el espacio de memoria pero no tiene limite)
);

-- Eliminando la tabla que estaba mal creada
DROP TABLE vacunaciones02.vacunatorios_campanias;
--
CREATE TABLE vacunatorios_campanias(
	id INT PRIMARY KEY AUTO_INCREMENT,
	vacunatorio_id INT NOT NULL,
	campania_id INT NOT NULL,

	-- CREACION DE RELACIONES
	FOREIGN KEY (vacunatorio_id) REFERENCES vacunatorios02(id),
    FOREIGN KEY (campania_id)    REFERENCES campanias(id)
);
--
INSERT INTO campanias (id, nombre, fecha, descripcion) VALUES 
	  (DEFAULT, 'PONGO EL HOMBRO', '2022-01-01', 'Campaña de vacunacion para personas adultas'),
	  (DEFAULT, 'VACUNA WARMA', '2022-03-10', 'Campaña de vacunacion para niños menores de 18 años'),
	  (DEFAULT, 'MAYORCITOS', '2021-11-04', 'Campaña de vacunacion para personas mayores a 65 años');

INSERT INTO vacunatorios_campanias (id, vacunatorio_id, campania_id) VALUES
									(DEFAULT, 1, 1),
                                    (DEFAULT, 2, 1),
                                    (DEFAULT, 3, 1),
                                    (DEFAULT, 2, 2),
                                    (DEFAULT, 1, 2),
                                    (DEFAULT, 3, 3),
                                    (DEFAULT, 4, 3),
                                    (DEFAULT, 5, 3)
                                    ;

-- Desde la campaña hacia el vacunatorio_campana
SELECT * FROM campanias as C INNER JOIN vacunatorios_campanias as VC ON C.id = VC.campania_id;