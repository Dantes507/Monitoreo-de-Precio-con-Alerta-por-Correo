#Monitoreo de Precio y Envío de Alerta por Correo


#Este script de Python verifica el precio de un producto especifico y compara si es menor al precio que se desea y de ser así, envía una alerta al email
que se introduzca como receptor del mensaje.


#Funcionamiento

1. Abre un ventana de navegador. 
2. Busca la pagina del producto.
3. Obtiene el Precio y el Nombre del Producto.
4. Verifica si se cumple la sentencia (que el precio de la pagina sea menor al mínimo aceptable)
5. Envía una alerta al email designado para avisar de esa baja de precio).


#Requisitos

- Python 3
- Librerías : os, dotenv, smtplib, selenium, BeautifulSoup  (vendrían incluidas con Python)
- Si las librerías no vienen instaladas seguir los siguientes pasos:

1. Abrir el CMD.
2. Introduce la ruta donde instalaste Python -> usando: cd + "Ruta especifica"
3. Ingresa pip + "Nombre de la librería" y se descargara e instalara.


#Guia de Uso

1. Crear un archivo .env con los datos requeridos y la siguiente estructura:
URL_PRODUCTO=	#Pagina del producto.
PRECIO_MINIMO=	#Precio mínimo que desea usar para activar la alerta.
EMAIL_EMISOR=	#Email que usara para enviar el mensaje.
PASSWORD= 	#Contraseña para el uso de aplicaciones del email que usara para enviar el mensaje.
EMAIL_RECEPTOR=	#Email al que desea que le llegue el mensaje.

2. Ejecutar el .exe y listo.
3. Proceso Terminado


#Actualizaciones Posibles

- Lograr que el script se ejecuta con una temporalidad especifica (cada día o cada cierto tiempo).
- Implementarlo con mas productos a la vez.


#Autor

Proyecto Realizado como Practica de Automatización para crecer como programador 

David Ortega

Versión 1.0.0
