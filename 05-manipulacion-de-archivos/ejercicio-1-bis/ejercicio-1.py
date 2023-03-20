# ## Ejercicio 1:

# Hacer un código que calcule la raiz cuadrada de todos los números del 1 al 100 y
# los guarde en un archivo "raices.csv" con el siguiente formato:

# > numero1, raíz de número1 \\
# > numero2, raíz de número2 \\
# > ...
# 

from math import sqrt as raiz_cuadrada;
import os;
import csv;

os.chdir('./05-manipulacion-de-archivos/ejercicio-1-bis');

resultado = 0;

with open("raices.csv", "w") as file:
    for i in range (1, 100):
        resultado = raiz_cuadrada(i);
        file.write(f"{round(resultado,2)} raiz de {i}\n")

with open("raices.csv") as f:
    filas = csv.reader(f);
    lineas = []
    for fila in filas:
        lineas.append(fila);
        print(fila)