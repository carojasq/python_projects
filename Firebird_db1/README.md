<h1> Agenda </h1>

Práctica acedémica, implementación de una agenda usando modelo relacional y firebird.

<h2> Instrucciones: </h2>
	````bash
	# Instalar dependencias
        pip install -r requirements.pip
	#Restaurar bases de datos (DUMP Incluido):
	gbak -c -v -user SYSDBA -password masterkey c:\location\1\database_backup.fbk dbserver:/db/agenda.fdb	
        ````
	Configurar usuario y contraseña en la segunda linea del archivo server.py

	Ejecutar:
         ````bash
	python2 server.py
        ````

	Ingresar a:
		localhost:8080 desde su navegador favorito


<h2> Licencia de la implementación: </h2>
	Creative commons.

<h2> Recursos: </h2>
	The Firebird Book: A Reference for Database Developers.

