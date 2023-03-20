# Ejercicio 5

# Dadas las listas de nombres y edades:
nombre = ["Juan", "Ana", "Marcela", "Claudio", "Nicolás", "Cecilia", "Tomás", "Pedro"];
edades = [25, 15, 13, 21, 45, 32, 17, 33];
# 1. Crear una lista de tuplas que contenga los nombres y las edades de las 
# personas mayores de 18 años. Atención, usar la función `zip()`.
tupla = tuple(zip(nombre, edades));
print(tupla);

lista_tuplas =  list(zip(nombre, edades))
mayores_de_edad = []
for nombre, edad in lista_tuplas:
  if edad >= 18:
    mayores_de_edad.append((nombre, edad))

# 2. Ordenar la lista resultante de forma alfabética por el nombre de las personas.
tupla_ordenada = sorted(mayores_de_edad);
print(tupla_ordenada);
# tupla_ordenada_dos = tupla.sort(); esto no funciona porque la tuplas no tienen este metodo.

