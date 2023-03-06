# ### Ejercicio 6

# # 1.   Crea una lista con los números del 1 al 10.
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
# 2.   Imprime los elementos en las posiciones 3, 4 y 5 utilizando slices.
print(lista[2:4])
# 3.   Imprime los elementos en las posiciones 2, 4, 6 y 8 utilizando slices.
# nueva = lista[1:8];
for numero in lista[1:8]:
    while numero%2==0:
        print(numero);
        break;
# 4.   Crea una nueva lista que contenga los elementos de la lista original en orden inverso utilizando slices.
nueva_lista = lista[::-1];
print(nueva_lista);
# 5.   Reemplaza los elementos en las posiciones 2, 3 y 4 con los números 20, 30 y 40 utilizando slices.
lista[1:2] = [20, 30, 40];
print(lista);

