
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import smtplib,os
from selenium import webdriver
from selenium.webdriver.common.by import By


def mandarEmail(precio_umbral,precio_pagina,emisor,password,receptor,producto):
    if precio_pagina < precio_umbral:
       porcentaje = 100 - ((precio_pagina*100)/precio_Minimo)
       #print(porcentaje)
       try:
            #Crear el objeto de conexion y especifica el puerto
            conexionEmail = smtplib.SMTP("smtp.gmail.com", 587)
            conexionEmail.ehlo()
            conexionEmail.starttls()
            #logearse
            conexionEmail.login(emisor,password)
            #Enviar email
            conexionEmail.sendmail(emisor,receptor, "Subject: Precio bajo del Umbral" f"\n\n +El producto : {producto} que te interesa ahora esta a {porcentaje} % menos de tu precio deseado de {precio_Minimo}")
            #Cerrar la conexion
            conexionEmail.quit()
            print("\nCorreo Enviado...")
       except:
           print ("\nError al enviar el email")
           

#Mercado libre usa JS, asi que tuve que usar selenium y el uso de proyecto es solamente de APRENDIZAJE
#Cargar variables del archivo .env
load_dotenv()

#Url del producto
url_Producto = os.getenv("URL_PRODUCTO")
#Precio a comparar
precio_Minimo = float(os.getenv("PRECIO_MINIMO"))
#Email que envia el mensaje
email_Emisor = os.getenv("EMAIL_EMISOR")
#Contraseña de ese email
password = os.getenv("PASSWORD")
#Email que recibe el mensaje
email_Receptor = os.getenv("EMAIL_RECEPTOR")
#Seleccionando navegador
driver =  webdriver.Chrome()
driver.get(url_Producto)   #Busca la url que se le pasa

#Obtener la informacion de pagina, pero con selenium - HTML
pagina = driver.page_source
#Parsear el HTML
soup = BeautifulSoup(pagina, "html.parser")
#Encontrar el nombre del producto
elemento = soup.find('h1', class_ = "ui-pdp-title")
producto = elemento.get_text(strip=True)
#Encontramos el precio del producto, con la construccion de la pagina
elemento = soup.find('span', class_ = "andes-money-amount__fraction")
#Convertir el dato para la manipulacion
precio = float(elemento.get_text(strip=True))
#Cerrar navegador
driver.quit()

mandarEmail(precio_Minimo,precio,email_Emisor,password,email_Receptor,producto)
print("\nPrograma Finalizado...\n")

