# ## Ejercicio 6

# Usando la herramienta de compresión de listas y diccionarios aprendidas en clases crear:

# 1. Crea una lista de los cuadrados de los números del 1 al 10 utilizando una comprensión de listas.
lista_de_numeros = [x for x in range(1, 11)];
print(lista_de_numeros)
lista_de_cuadrados = [x**2 for x in lista_de_numeros];
print(lista_de_cuadrados);

# 2. Crea una lista de los números pares del 1 al 20 utilizando una comprensión de listas.
lista_de_numeros_dos = [x for x in range(1,21)];
lista_de_numeros_pares = [x for x in lista_de_numeros_dos if x % 2 == 0];
print(lista_de_numeros_pares);

# 3. Crea un diccionario que asocie ciudades con sus temperaturas actuales de las siguiente listas.
ciudades = ["Buenos Aires", "Madrid", "Roma", "París"]
temperaturas = [28, 16, 21, 19]

ciudades_y_temperaturas = dict(zip(ciudades, temperaturas))
print(ciudades_y_temperaturas)