# ### Ejercicio 1:
# **Temperaturas máximas**
# En la página del servicio metereológico nacional es posible descargar algunos [datos históriocos]
# (https://www.smn.gob.ar/descarga-de-datos). A partir de los archivos: 
# * `estaciones_metereologicas.csv` que contiene la información de las estaciones metereologicas 
# en el país. 
# * `registro_temperatura365d_smn.csv`que tiene, para las diferentes estaciones metereologicas,
# los valores máximos y mínimos de temperatura registrados para diferentes días en el último año. 

import os;
import csv;
print(os.getcwd());
print(os.listdir());
os.chdir('./05-manipulacion-de-archivos/ejercicio-1'); # Recordar poner un ./ 
print(os.getcwd()) ;

# with open('estaciones_metereologicas.csv') as estaciones:
#     data = estaciones.read()
#     print(data)

# Determinar para la región del país en donde vive cuál fue la mínima y máxima temperatura 
# registrada en el último año y para que día fue.
with open('registro_temperatura365d_smn.csv') as temperaturas:
    filas = csv.reader(temperaturas);
    lineas = [];
    for fila in filas:
        lineas.append(fila);
    
    for linea in lineas:
        if linea[3] == "BUENOS AIRES OBSERVATORIO":
            print("El dia", linea[0], ", se registró una temperatura maxima de", linea[1], "y una temperatura menima de", linea[2], "en", linea[3])


# dias con temperatura maxima y minima.
lista_tmax = []
lista_tmin = []
lista_fecha = []

with open('registro_temperatura365d_smn.csv') as f:
  filas = csv.reader(f)
  encabezados = next(filas)
  for fila in filas:
    if "ROSARIO AERO" in fila:
      lista_fecha.append(fila[0])
      lista_tmax.append(float(fila[1]))
      lista_tmin.append(float(fila[2]))

tmin=min(lista_tmin)
tmax=max(lista_tmax)
fecha_tmin=lista_fecha[lista_tmin.index(tmin)]
fecha_tmax=lista_fecha[lista_tmax.index(tmax)]
print(f'Estacion ROSARIO AERO\r\n fecha: {fecha_tmin} tmin {tmin}\r\n fecha: {fecha_tmax} tmax {tmax}')