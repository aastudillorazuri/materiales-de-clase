						/*========================================
							SESIÓN Nº02: GESTIÓN DE BASES DE DATOS
						===========================================*/
/*==============================
	I.- CREACIÓN DE BD
================================*/
/*-----------------------
		CASO Nº01
-------------------------*/
--Crear la base de datos VENTAS de forma predeterminada
--1) Activamos la base de datos maestra
	USE master
	GO

--2) Validando la existencia de la base de datos
	IF DB_ID('VENTAS')IS NOT NULL
		DROP DATABASE VENTAS
	GO

--3) Crear la BD
	CREATE DATABASE VENTAS
	GO

--4) Visualizar la base de datos en un listado
	SELECT*FROM SYS.sysdatabases S
	WHERE S.name='VENTAS'
	GO

/*-------------------
	CASO Nº02
---------------------*/
--Crear la base de datos VENTAS en una carpeta específica. Considerar un tamaño inicial de 50 MB
--máximo de 150 MB y una tasa de crecimiento del 20%
DROP DATABASE VENTAS
GO

CREATE DATABASE VENTAS
ON PRIMARY(
	NAME='VENTAS',
	FILENAME='C:\BaseVentas\VENTAS.MDF',
	SIZE=50MB,
	MAXSIZE=150MB,
	FILEGROWTH=20%
)
GO

/*----------------
	CASO Nº03
----------------*/
--Crear la base de datos VENTAS en una carpeta específica. Considerar un taño inicial de 50 MB
--máximo de 150 MB y una tasa de crecimiento del 20%. Además, un archivo de transacciones con
--tamaño inicial de 5MB, máximo de 50 MB y una tasa de crecimiento del 10%
DROP DATABASE VENTAS
GO

CREATE DATABASE VENTAS
ON PRIMARY(
	NAME='VENTAS',
	FILENAME='C:\BaseVentas\VENTAS.MDF',
	SIZE=50MB,
	MAXSIZE=150MB,
	FILEGROWTH=20%
)
LOG ON(
	NAME='VENTAS_LOG',
	FILENAME='C:\BaseVentas\VENTAS.LDF',
	SIZE=5MB,
	MAXSIZE=50MB,
	FILEGROWTH=10%
)
GO

/*---------------------------
		TIPOS DE DATOS
-----------------------------*/
--Verificar los tipos de datos en la base
	SELECT*FROM SYS.systypes
	GO

--Agregando un tipo de dato para documento de identidad
	SP_ADDTYPE DNI,'CHAR(8)','NOT NULL'
	GO

--Eliminar el tipo de dato
	SP_DROPTYPE 'DNI'
	GO

/*============================
	II.- GESTIÓN DE TABLAS
==============================*/
/*----------------------
	CREACIÓN DE TABLAS
------------------------*/
--1.- Creación de la tabla CLIENTE
--Activar la base
USE VENTAS
GO

--Verificación de la tabla
IF OBJECT_ID('CLIENTE')IS NOT NULL
	DROP TABLE CLIENTE
GO

--Creación de la tabla
CREATE TABLE CLIENTE(
	CODIGO CHAR(5),
	DIRECCION VARCHAR(100),
	TELEFONO CHAR(13),
	RUC CHAR(11),
	TIPO VARCHAR(10),
	CONTACTO VARCHAR(30)
)
GO

--Selección de la tabla
SELECT*FROM CLIENTE
GO

--Lista de tablas en la BD
	SP_TABLES
	GO

--Visualizar las columnas
	SP_COLUMNS CLIENTE
	GO

/*------------------------
	MODIFICAR LA TABLA
--------------------------*/
--Modificar la extensión del campo TELEFONO de la tabla cliente
ALTER TABLE CLIENTE
	ALTER COLUMN TELEFONO CHAR(15)
GO

--Agregar el campo FECHA DE NACIMIENTO
ALTER TABLE CLIENTE
	ADD FNA DATE
GO

SELECT*FROM CLIENTE
GO

--Eliminar el campo CONTACTO
ALTER TABLE CLIENTE
	DROP COLUMN CONTACTO
GO

--Eliminar la tabla
DROP TABLE CLIENTE
GO

/*-------------------------------
	RESTRICCIÓN DE DATOS NULOS
-------------------------------*/
--Crear la tabla CLIENTE
CREATE TABLE CLIENTE(
	CODIGO CHAR(5) NOT NULL,
	DIRECCION VARCHAR(100) NOT NULL,
	TELEFONO CHAR(13) NULL,
	RUC CHAR(11) NOT NULL,
	TIPO VARCHAR(10) NULL,
	CONTACTO VARCHAR(30) NULL
)
GO

--Añadir ESTADO DEL CLIENTE con asignación de valor nulo
ALTER TABLE CLIENTE
	ADD ESTADO CHAR(1) NULL
GO

/*--------------------
	LLAVE PRIMARIA
----------------------*/
--Implementar la tabla DISTRITO asignando COD_DIS como el campo clave
--Primera forma
CREATE TABLE DISTRITO(
	COD_DIS CHAR(5) NOT NULL PRIMARY KEY,
	NOM_DIS VARCHAR(50) NOT NULL
)
GO

--Segunda forma
DROP TABLE DISTRITO
GO

CREATE TABLE DISTRITO(
	COD_DIS CHAR(5) NOT NULL,
	NOM_DIS VARCHAR(50) NOT NULL
)
GO

ALTER TABLE DISTRITO
	ADD PRIMARY KEY (COD_DIS)
GO

--Tercera forma
DROP TABLE DISTRITO
GO

CREATE TABLE DISTRITO(
	COD_DIS CHAR(5) NOT NULL,
	NOM_DIS VARCHAR(50) NOT NULL,
	PRIMARY KEY (COD_DIS)
)
GO

--Implementar la tabla DETALLE_COMPRA asignando llaves compuestas a NUM_DOC y COD_PRO
--Primera forma
CREATE TABLE DETALLE_COMPRA(
	NUM_DOC CHAR(5) NOT NULL,
	COD_PRO CHAR(5) NOT NULL,
	CANTIDAD INT NOT NULL,
	PRIMARY KEY (NUM_DOC,COD_PRO)
)
GO

--Segunda forma
DROP TABLE DETALLE_COMPRA
GO

CREATE TABLE DETALLE_COMPRA(
	NUM_DOC CHAR(5) NOT NULL,
	COD_PRO CHAR(5) NOT NULL,
	CANTIDAD INT NOT NULL,
)
GO

ALTER TABLE DETALLE_COMPRA
	ADD PRIMARY KEY(NUM_DOC,COD_PRO)
GO

/*--------------------
	LLAVE SECUNDARIA
----------------------*/
--Implementar la tabla distrito asignando COD_DIS como campo clave
DROP TABLE CLIENTE
DROP TABLE DISTRITO
GO

--Primera forma
	CREATE TABLE DISTRITO(
		CODIGO CHAR(5) NOT NULL PRIMARY KEY,
		NOMBRE VARCHAR(50) NOT NULL,
		GOBERNADOR VARCHAR(50) NOT NULL
	)
	GO

	CREATE TABLE CLIENTE(
		COD_CLIENTE CHAR(5) NOT NULL PRIMARY KEY,
		DIRECCION VARCHAR(100) NOT NULL,
		RUC CHAR(11) NOT NULL,
		COD_DIS CHAR(5) NOT NULL REFERENCES DISTRITO
	)
	GO

