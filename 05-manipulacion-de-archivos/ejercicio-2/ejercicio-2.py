# ### Ejercicio 2:
# Escribir un programa que pida un número entero entre 1 y 10 y guarde en 
# un fichero con el nombre `tabla-n.txt` la tabla de multiplicar de ese número, 
# donde `n` es el número introducido.

import os;
import csv;
print(os.getcwd());
print(os.listdir());
os.chdir('./05-manipulacion-de-archivos/ejercicio-2'); # Recordar poner un ./ 
print(os.getcwd()) ;

numero = int(input("Ingrese un numero para generar la tabla: "));
resultado = 0;
texto = "";
# with open("tabla-n.txt", "w") as tabla:
#     data = tabla.read()
#     indice = 0;
#     lineas = []; #tendria que llenar el array antes de recorrer

#     while indice <= 10:
#         resultado = numero * indice;
#         texto = tabla.write(f"{numero} x {indice} = {resultado}");
#         # lineas.append(texto);
#         indice += 1;
#     print(data);
#     print(lineas)

nombre_fichero = 'tabla-' + str(numero) + '.txt'
with open(nombre_fichero, 'w') as f:
    for i in range(1, 11):
        f.write(str(numero) + ' x ' + str(i) + ' = ' + str(numero * i) + '\n')
        

with open(nombre_fichero) as f:
    filas = csv.reader(f);
    lineas = []
    for fila in filas:
        lineas.append(fila);
        print(fila)