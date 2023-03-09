#  # Ejercicio 1

# Escribe un programa que pida al usuario ingresar una lista de números separados por comas.
# Luego, crea una tupla con esos números y muestra por pantalla la tupla creada y la suma de sus elementos. 
# Si la lista que ingresa el usuario tiene elementos erroneos, que el programa se frene y le avise al usario.

# *Pista: Para que sum() funcione todos los elementos del contenedor tiene que ser int o float.*

# numeros_input = input("Ingrese numeros separados por \",\": ");
numeros = "4, 5, 6, 7, 32";
numeros_lista = numeros.split(",");
print(numeros_lista)
tupla = zip(numeros_lista);
print(tupla)
sumatoria = sum(tupla)