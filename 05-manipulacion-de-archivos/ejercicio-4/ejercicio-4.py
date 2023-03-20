# **a**. Escribí código que te permita leer este archivo y explorarlo
import os;
import csv;
os.chdir('./05-manipulacion-de-archivos/ejercicio-4');

with open("estimaciones-agricolas-PBA-1969-2022.csv") as estimaciones:
    filas = csv.reader(estimaciones);
    lineas = [];
    for fila in filas:
        lineas.append(fila);
    print(lineas)
    
# **b**. Escribí código que te permita leer todos los datos (filas) de la planilla, 
# almacenando los valores (columnas) en alguna estructura de datos de Python (dict, lista, tupla, set) 
# que te parezca la más apropiada para responder las consultas que vienen a continuación. Explicá y fundamentá tu elección.

# Si no encontrás ninguna que sea perfecta o que no se ajuste en forma ideal a lo que necesitás, 
# discutilo y sugerí que cambios harias (en los datos) para poder operar más facilmente con la estructura 
# de Python que elegiste. 

# Consultas:

# **i**. Cuántos tipos de cultivos diferentes hay registrados en la Provincia de Buenos Aires? 

# **ii**. Cuál es el principal municipio productor de Ajo en la Provincia? y cuál fue el año de mayor superficie sembrada? 
# Y el año de mayor rendimiento? 

# **iii**. Repetí el punto **ii** para todos los cultivos. Cuáles son los mejores años en la Provincia?
# Coinciden para todos los cultivos?
