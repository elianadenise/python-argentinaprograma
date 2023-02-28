# ### Ejercicio 7 - (opcional)

# Supongamos que tenemos una lista de números enteros, y queremos encontrar todas las subsecuencias
# de la lista que sumen un número objetivo dado. Para hacerlo, vamos a crear una función que tome
# como argumentos la lista de números y el número objetivo, y devuelva una lista con todas
# las subsecuencias que suman el número objetivo. 

# *Ayuda:* Por ejemplo, si le damos a tu programa la lista de números [1, 2, 3, 4, 5] 
# y queremos encontrar todas las subsecuencias que suman `7` (número objetivo dado), 
# la función debería devolver las siguientes listas [2, 5], [3, 4], [1, 2, 4].

enteros = [1, 2, 3, 4, 5];
numero = int(input("Ingrese numero"))
cadena = "";
indice = 0;
for entero in enteros:
    for entero in enteros:
        if entero + enteros[indice] == numero:
            cadena += f"[ {entero}, {enteros[indice]} ],";
            # print(entero, enteros[indice])
            break;
        
    indice += 1;
    
print(cadena);