# Natali - Salomón

## Recomendaciones.
### Usar entorno virtual. En una carpeta usar el comando " py -m venv {nombre_del_entorno} " par iniciarlo. 
### Ya depues seleccionar desde VisualCode el interprete a utilizar, para esto oprimir CtrilIzq + Shit + P, despues colocar " >python: Select Interpreter " y seleccionar el interprete parecido a la siguiente iamgen:

![image](https://github.com/SalomonRN/API-DJANGO/assets/109772788/636144cd-d0e5-421b-bcb7-be6dbef1230a)

## Instalar las dependencias
### Para instalar las dependencias necesarias usamos " pip install -r requirements.txt "

## Pasos
### Inicar server con " py manage.py runserver 0.0.0.0:8000 "


### Usar " http://localhost:8000/api/Estudiante/ " para las peticiones, solo combiar parametros.
### Si se agregar un numero al final en una peticion GET buscará por ID en la DB " http://localhost:8000/api/Estudiante/1/ " (Retorna el dato con valor 1)
### Para eliminar solo cambiar el metodo a DELETE es: " http://localhost:8000/api/Estudiante/1/ " (Elimina el dato con valor 1)



### Notas: 
## Note that the default IP address, 127.0.0.1, is not accessible from other machines on your network. To make your development server viewable to other machines on the network, use its own IP address (e.g. 192.168.2.1), 0 (shortcut for 0.0.0.0), 0.0.0.0, or :: (with IPv6 enabled) 
