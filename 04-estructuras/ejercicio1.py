#  # Ejercicio 1

# Escribe un programa que pida al usuario ingresar una lista de números separados por comas.
# Luego, crea una tupla con esos números y muestra por pantalla la tupla creada y la suma de sus elementos. 
# Si la lista que ingresa el usuario tiene elementos erroneos, que el programa se frene y le avise al usario.

# *Pista: Para que sum() funcione todos los elementos del contenedor tiene que ser int o float.*

numeros_input = input("Ingrese numeros separados por \",\": ");
numeros_lista = numeros_input.split(",");
print(numeros_lista)
tupla = zip(numeros_lista);
print(tupla)
sumatoria = sum(tupla)


# ---------- ejemplo con try y map ----------
numeros = (input("Ingrese numeros separados por coma: ")).split(",")
convertir_a_numeros = []

try:
   #convertir_a_numeros = [float(x) for x in numeros]  #convertir lista string a lista numerica
   convertir_a_numeros = map(float,numeros) #el map es mas conveniente que el for anterior - MAP ITERA TODO. (ACCION, VARIABLE-A-APLICAR-ACCION)
   numeros_tupla = tuple(convertir_a_numeros)
   print(f"Tupla de numeros: \n{numeros_tupla} \nSuma de elementos: \n{sum(numeros_tupla)}")
except ValueError:
  print("La lista solo debe contener valores numericos")


# ---------- ejemplo con enumerate ----------
numeros = (input("Ingrese numeros separados por coma: ")).split(",")
lista = numeros.split(",");
print(lista);

for i, v in enumerate(lista):
   num = 0;
   if v.isdigit():
      num = int(v);
   else: 
      print(f"ERROR: solo se puede ingresar numeros enteros, {v} no es un caracter permitido")
   lista[i] = (num);

tupla = tuple(lista);
print(tupla);
print(sum(tupla));


# ---------- ejemplo con try e if ----------
numeros = (input("Ingrese numeros separados por coma: ")).split(",")
lista = numeros.split(",");
lista_a_llenar = [];

try:
   for numero in lista:
      if '.' in numero:
         numero_a_agregar = float(numero);
         lista_a_llenar.append(numero_a_agregar);
      else:
         numero_a_agregar = int(numero);
         lista_a_llenar.append(numero_a_agregar);
   tupla = tuple(lista_a_llenar);
   print("Tupla: ", tupla, "; Sumatoria: ", sum(tupla));
except ValueError:
   print("Ingresaste un valor no numerico");



# ---------- ejemplo con while y for ----------
condicion = False
while condicion == False:
  lista = input("Ingrese una lista de números  separados por comas: ")
  lista=lista.split(",")     
  for n in lista:
    if not n.isdigit():
      if '-' in n or '.' in n:
        continue
      else:
        print("Error: La lista ingresada contiene elementos no numéricos. Vuelva a intentarlo")
    else:
      condicion=True
lista = [float(num) for num in lista]
tupla_num = tuple(lista)
print("Tupla creada:", tupla_num)

suma = sum(tupla_num)
print("Suma de los elementos:", suma)