# # ## Ejercicio 3:

# Juan es un joven inversor que hace unos años decidió probar suerte en
# la bolsa argentina para cubrirse de la inflación.
# El [archivo](https://drive.google.com/file/d/1UtYNDSZDwFJwNrAAxCeQBpoZt53Zyf4H/view?usp=share_link) `portafolio_juan.csv`
# contiene la información de las acciones que fue agregando a su pequeño portafolio de inversión. El mismo contiene los siguientes datos:

# **a.** Hacé un código que lea un csv como el mencionado anteriormente
# y devuelva una **lista de diccionarios** conteniendo los datos de cada fila,
# donde cada encabezado es la clave del valor correspondiente.
# Por ejemplo, el primer elemento de la lista debería ser
# `{'ticker': 'LOMA', 'fecha': '2021-04-26', 'cantidad': '28', 'precio_compra': '184.3', 'precio_actual': '507'}`.
# *Ayuda: la función zip puede facilitar la creación de los diccionarios.*

import os
import csv
os.chdir('./05-manipulacion-de-archivos/ejercicio-3')
print(os.getcwd())

with open('portafolio_juan.csv') as portafolio:
    lineas = csv.reader(portafolio)
    encabezado = next(lineas)

    lista_dic = []
    for linea in lineas:
        lista_dic.append(dict(zip(encabezado, linea)))
    print(lista_dic)

# CON COMPRENSION
# with open('/content/drive/MyDrive/Colab Notebooks/Data/portafolio_juan.csv') as portafolio:
#     lineas = csv.reader(portafolio)
#     encabezado = next(lineas)
#     lista_dic = [dict(zip(encabezado, linea)) for linea in lineas]


# **b.** A partir de la lista de diccionarios que creaste en el inciso anterior, calculá el valor actual
# del portafolio de acciones (es decir, la suma del precio actual de las acciones mutiplicado por la 
# cantidad de acciones que posee) y el costo de compra del mismo (la suma del precio de compra de 
# las acciones mutiplicado por la cantidad de acciones que compró ese día). ¿Juan ganó o perdió dinero?

    # for i in lista_dic.values():
    #     if lista_dic.key() == 'cantidad' and lista_dic.key() == 'precio_actual':
    #         multiplicacion += i