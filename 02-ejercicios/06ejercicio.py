# ## Ejercicio 6:

# Escriba un programa que reciba dos números y los compare dando 
# como resultado verdadero o falso ante la frase: 
# El primer número es menor que el segundo. 

numero_uno = int(input("Ingrese un numero: "));
numero_dos = int(input("Ingrese otro numero: "));

print(f'¿{numero_uno} es menor que {numero_dos}?')
if numero_uno < numero_dos:
    print("El primer número es menor que el segundo");
else:
    print("no.")