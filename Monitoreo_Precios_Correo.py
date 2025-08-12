
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import smtplib, os, csv, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from email.mime.text import MIMEText


def mandarEmail(precios_umbral,precios_pagina,productos):
    i = 0
    try:
        mensaje = """"""
        for precio_pagina in precios_pagina:     
            #Comprobacion del umbral del precio
            if precio_pagina < precios_umbral[i]:
                porcentaje = 100 - ((precio_pagina*100)/precios_umbral[i])
                mensaje += f"\n\n +El producto : {productos[i]} que te interesa ahora esta a {porcentaje} % menos de tu precio deseado de {precios_umbral[i]} con un valor de : {precios_pagina[i]}"     
            i+=1
        i=0
         
        #Cargar variables del archivo .env
        load_dotenv()
        #Email que envia el mensaje
        emisor = os.getenv("EMAIL_EMISOR")
        #Contraseña de ese email
        password = os.getenv("PASSWORD")
        #Email que recibe el mensaje
        receptor = os.getenv("EMAIL_RECEPTOR")
        #Crear el objeto de conexion y especifica el puerto
        conexionEmail = smtplib.SMTP("smtp.gmail.com", 587)
        conexionEmail.ehlo()
        conexionEmail.starttls()
        #Creacion de la estructura del mensaje
        msg = MIMEText(mensaje,"plain","utf-8")
        msg["Subject"] = "Precio bajo del Umbral"
        msg["From"] = emisor
        msg["To"] = receptor
        #logearse
        conexionEmail.login(emisor,password)
        #Enviar email
        #Mandar el mail
        conexionEmail.send_message(msg)
        #Cerrar la conexion
        conexionEmail.quit()
        print("\nCorreo Enviado...")
    except:
        print ("\nError al enviar el email")           

def lectorCsv()  :
   try:
        #Declaracion del diccionario para trabajar
        productos = {}
        #Abrir el csv con la info de  las urls y precios
        with open('productos.csv', newline='',encoding='utf-8') as csvfile:
            #Lectura de la info en memoria
            Lector = csv.DictReader(csvfile)
            for fila in Lector:
                #Introducir los valores en el diccionario
                productos[fila["url"]] = float(fila["precio_umbral"])
        #Retornar el diccionario
        return productos
   except:
       print("\n Ocurrio un error en la lectura del archivo .csv")     

def busquedaPrecios(productos_dict,driver):
    try:
        precios = []
        productos = []
        precios_umbral = []
        
        for url in productos_dict.keys():
            #Busca la url que se le pasa
            driver.get(url) 
            #Obtener la informacion de pagina, pero con selenium - HTML
            pagina = driver.page_source
            #Parsear el HTML
            soup = BeautifulSoup(pagina, "html.parser")
            #Encontrar el nombre del producto
            elemento = soup.find('h1', class_ = "ui-pdp-title")
            producto = elemento.get_text(strip=True)
            productos.append(producto)
            #Encontramos el precio del producto, con la construccion de la pagina
            elemento = soup.find('span', class_ = "andes-money-amount__fraction")
            #Convertir el dato para la manipulacion
            precio = float(elemento.get_text(strip=True))
            precios.append(precio)
            #Dejar el programa en pause ese tiempo para evitar, bloqueos de la pagina
            time.sleep(5)    
      
        for precio in productos_dict.values():
           precios_umbral.append(precio)

        mandarEmail(precios_umbral,precios,productos)
    except:
        print("Ocurrio un problema con la busqueda de precios")


#Mercado libre usa JS, asi que tuve que usar selenium y el uso de proyecto es solamente de APRENDIZAJE y estoy usando Mercado libre para practicar

#Leer el csv con las Urls y los precios
productos = {}
#Invocar la funccion de lectura del csv y obtener esa informacion
productos = lectorCsv()

#Seleccionando navegador
driver =  webdriver.Chrome()
busquedaPrecios(productos,driver)
#Cerrar navegadorS
driver.quit()
print("\nPrograma Finalizado...\n")
