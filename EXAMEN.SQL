CREATE DATABASE EXAMEN

USE EXAMEN

CREATE TABLE FINAL(
ID_Alumno INT  NOT NULL,
NOMBRE NVARCHAR(20) NOT NULL,
APELLIDO VARCHAR(50) NOT NULL,
NOTA INT NOT NULL
PRIMARY KEY (ID_Alumno)

)

SELECT * FROM FINAL
INSERT INTO FINAL(
Id_Alumno,
NOMBRE,
APELLIDO,
NOTA
)
VALUES(
11, 'DIEGO','OBIN','60')
