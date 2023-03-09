# # Ejercicio 4

# Escribe un programa que pida al usuario que ingrese dos listas de números 
# enteros separados por espacios. 
# Luego, crea dos conjuntos con los elementos de cada lista y muestra por 
# pantalla los siguientes conjuntos:

#     1. La unión de los dos conjuntos
#     2. La intersección de los dos conjuntos
#     3. Los elementos que están en el primer conjunto pero no en el segundo
#     4. Los elementos que están en el segundo conjunto pero no en el primero

numeros_input = input("Ingrese dos numeros de más de 10 cifras, separadas por un " ": ");
lista = numeros_input.split(" ");
set_uno = set(list(lista[0]));
set_dos = set(list(lista[1]));
print(set_uno);
print(set_dos);
union = set_uno | set_dos;
print(union);

interseccion = set_uno & set_dos;
print(interseccion);

primer = set_uno - set_dos;
print(primer);

segundo = set_dos - set_uno;
print(segundo);