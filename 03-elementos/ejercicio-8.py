numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30];
fizz = "fizz";
buzz = "buzz";
fizzbuzz = "fizzbuzz";
indice = 0;

# realiza el cambio definitivo en el array
for numero in numeros:
    if numero % 3 == 0 and numero % 5 == 0:
        numeros[indice] = fizzbuzz;
    elif numero % 3 == 0:
        numeros[indice] = fizz;
    elif numero % 5 == 0:
        numeros[indice] = buzz;
    else:
        numeros[indice] = numero;
    indice += 1;
    print(numero)

print(numeros);
print(numeros[14]);


# asigna el nuevo valor solo en el bucle, no cambia la lista

# for numero in numeros:
#     if numero % 3 == 0 and numero % 5 == 0:
#         numeros = fizzbuzz;
#     elif numero % 3 == 0:
#         numero = fizz;
#     elif numero % 5 == 0:
#         numero = buzz;
#     else:
#         numero = numero;
#     indice += 1;
#     print(numero)

# print(numeros);
# print(numeros[14]);