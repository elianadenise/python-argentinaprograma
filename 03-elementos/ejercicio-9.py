# ## Ejercicio 9:
# En base a las listas ficticias de alumnos, con datos como nombre, apellido, y nota (calificación).

# Escribir un programa que:
# *NOTA: el orden de las listas es el mismo, vale decir, la nota de Laura Pérez es 7, y asi sucesivamente.*

nombres = ['Laura', 'Juan', 'Tomás', 'Ana', 'Diego', 'Carla', 'Kim', 'Sofía'];
apellidos = ['Pérez', 'Isla', 'Gómez', 'Castro', 'Roca', 'Romero', 'Díaz', 'López'];
notas = [7, 4, 9, 5, 7, 10, 8, 6];

# * Imprima la nombre y apellido de los alumnos de manera ordenada alfabéticamente por el apellido
indice = 0;
for nombre in nombres:
    print(f"Nombre: {nombre:<10s} Apellido: {apellidos[indice]:<10s} Nota: {notas[indice]}");
    indice += 1;

# * Calcule el promedio de notas de la cursada, e informe la nota máxima y la mínima.
acumulador = 0;
promedio = 0;
menor = 0;
for nota in notas:
    acumulador += nota;
    menor = min(notas);
    mayor = max(notas);
promedio = acumulador / len(notas);
print(f"Promedio de la notas de la cursada: {promedio}");
print(f"Menor: {menor}");
print(f"Mayor: {mayor}");


# indice_dos = 0;
# indice_tres = 0;
# mayor = 0;
# for nota in notas:
#     if notas[indice_dos-1] < nota:
#         mayor = nota;
#     indice_dos += 1;
# print(f"Mayor: {mayor}");

# este no funciona
# menor = 0;
# auxiliar = 0;
# for nota in notas:
#     if nota < notas[indice_tres-1]: // porque no tiene que tomar el anterior, tiene que tomar el anterior numero menor, osea va con un aux
#         menor = nota;
#     indice_tres += 1;
# print(f"Menor: {menor}");

# * Genere una variable llamada "aprobados" con un a lista de alumnos aprobados (se aprueba con 7)
aprobados = "";
indice_dos = 0;
for nota in notas:
    if nota >= 7:
        aprobados += f"Nombre: {nombres[indice_dos]:<10s} Apellido: {apellidos[indice_dos]:<10s} Nota: {nota} \n";
    indice_dos += 1;
print(f"Aprobados: \n{aprobados}");

# * Genere una variable (lista) conteniendo valores booleanos (True/False), que corresponda a los alummnos aprobados (`True`) o desaprobados (`False`)
promocionados = [];
desaprobados = [];
cadena = ""
indice_tres = 0;
for nota in notas:
    if nota >= 7:
        cadena = f"Nombre: {nombres[indice_tres]:<10s} Apellido: {apellidos[indice_tres]:<10s} Nota: {nota}"
        promocionados.append(cadena);
    elif nota < 7:
        cadena = f"Nombre: {nombres[indice_tres]:<10s} Apellido: {apellidos[indice_tres]:<10s} Nota: {nota}"
        desaprobados.append(cadena);
    indice_tres += 1;
print(f"Aprobados: \n{promocionados}")
print(f"Desaprobados: \n{desaprobados}") 