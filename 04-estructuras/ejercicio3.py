# # Ejercicio 3

# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y
# muestre por pantalla la misma fecha en formato dd de \<mes\> de aaaa
# donde \<mes \> es el nombre del mes. Para ello cree un diccionario que relacione 
# el valor de mm con el nombre del mes. 

meses = {
    "01" : "enero",
    "02" : "febrero",
    "03" : "marzo",
    "04" : "abril",
    "05" : "mayo",
    "06" : "junio",
    "07" : "julio",
    "08" : "agosto",
    "09" : "septiembre",
    "10" : "octubre",
    "11" : "noviembre",
    "12" : "diciembre"
}

entrada = input("Ingrese una fecha en formato dd/mm/aaaa: ");
dia = entrada[0:2];
mes = entrada[3:5];
anio = entrada[-4:];
print(f"{dia} de {meses[mes]} de {anio}")

# ver resolucion de los profes, lo hicieron con split. re lindo