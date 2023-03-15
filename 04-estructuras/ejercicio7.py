# Ejercicio 7

# Escribe un programa que lea una lista de palabras separadas por espacios 
# y cree una tupla con ellas. Luego, muestra por pantalla la tupla creada 
# y la cantidad de veces que aparece la letra más repetida en todas las palabras.
palabras = "hola arbol cartuchera lapicera murcielago developer testing"
lista_de_palabras = palabras.split(" ");

tupla_de_palabras = tuple(lista_de_palabras)
print(tupla_de_palabras);

# y la cantidad de veces que aparece la letra más repetida en todas las palabras.
palabras = palabras.replace(" ", "");
dic = {};
for i in palabras:
    if i not in dic:
        dic[i] = 1;
    else:
        dic[i] += 1;

print(tupla_de_palabras, "\nLetra que se repite más veces: ", [key for key, value in dic.items() if value == max(dic.values())]);