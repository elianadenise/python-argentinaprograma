# ## Ejercicio 2

# Escribir un programa que pregunte al usuario su nombre, apellido, edad y teléfono, 
# y que lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje:  
# \<nombre apellido\> tiene \<edad\> años y su número de teléfono es \<telefono\>.

nombre = input("Ingrese su nombre: ");
apellido = input("Ingrese su apellido: ");
edad = int(input("Ingrese su edad: "));
telefono = int(input("Ingrese su telefono: "));

persona = {
    "nombre" : nombre,
    "apellido" : apellido,
    "edad" : edad,
    "telefono" : telefono
}
print(persona["nombre"]) # en este caso parece que no pasa nada
print(f"{persona['nombre']} {persona['apellido']} tiene {persona['edad']} años y su número de teléfono es {persona['telefono']}.");
# print con f y {} de valores de diccionario usar '' no ""