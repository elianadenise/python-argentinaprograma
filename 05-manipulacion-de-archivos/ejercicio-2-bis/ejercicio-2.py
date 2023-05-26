# (*)  Este archivo está en formato CVS y corresponde a una base de datos sobre árboles en parques de la Ciudad de Buenos Aires. 
# El mismo lo pueden obtener directamente  de [la página del gobierno de CABA](https://data.buenosaires.gob.ar/dataset/arbolado-espacios-verdes) 

# Realizar:
import os;
import csv;
os.chdir('./05-manipulacion-de-archivos/ejercicio-2-bis');

# **a**. Leer el archivo y explorarlo
arboles = []
with open('arbolado.csv', errors="ignore") as f:
    filas = csv.reader(f)
    encabezado = next(filas)
    for fila in filas:
        arboles.append(fila)

# print(arboles)

# **b**. Hacer un código que cree una lista con las alturas de los arboles (columna `'altura_tot'`) de una determinada especie 
# (por ejemplo, probar con `'Jacarandá'` de la columna `'nombre_com'` ).
altura_de_especie = [];
especie = "Ulmaceas"
with open('arbolado.csv', errors="ignore") as f:
    filas = csv.reader(f)
    for fila in filas:
        if fila[12].__eq__(fila):
            altura_de_especie.append(fila[3] + "m")
# print(altura_de_especie) # esto esta mal. no funciona. tira mal las alturas

# **c**. ¿Cuál es el arbol más alto que podemos encontrar en CABA? ¿En qué espacio verde queda?
arbol_mas_alto = 0;
for arbol in arboles:
    arbol_mas_alto = (max(arbol[3]))
print(arbol_mas_alto)
    
# **d**. ¿Cuántos especios verdes diferentes podemos encontrar en CABA?

# **e**. Crear un archivo, llamado 'palmeras.txt' que contenga todas las informaciones de los árboles de este tipo. 

# alturas = []
# especie_altura = 'Jacarandá'
# max_altura = 0
# max_altura_espacio = ''
# espacios_verdes = set()

# with open('palmeras.txt', 'w', errors="ignore") as o:

#     for arbol in arboles:

#         # Crea lista con las alturas
#         if arbol[7] == especie_altura:
#             alturas.append(arbol[3])

#         # Obtiene la mayor altura y en que espacio se encuentra
#         if int(arbol[3]) > max_altura:
#             max_altura = int(arbol[3])
#             max_altura_espacio = arbol[10]
        
#         # Genera un conjunto con los espacios verdes
#         espacios_verdes.add(arbol[10])

#         #se agrega info al archivo palmeras.txt
#         if arbol[9]  == 'Palmera':
#             o.write(','.join(arbol) + '\n')

# print('Lista alturas')
# print(alturas)
# print()
# print(f'El arbol mas alto mide {max_altura} mts y se encuentra en el espacio' \
#       f'verde {max_altura_espacio}')
# print()
# print(f'En CABA hay un total de {len(espacios_verdes)} espacios verdes')
# print()
# print('Se creó el archivo palmeras.txt')