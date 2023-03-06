# ### Ejercicio 3
# **Meses y días.** Crea un programa que pida un número de mes (por ejemplo, el 4) 
# y diga cuántos días tiene (por ejemplo, 30) 
# y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

mes = int(input("Ingrese el numero de mes: "));
mes = mes - 1;
meses =  ["Enero, 31 días", "Febrero, 28 días", "Marzo, 31 días", "Abril, 30 días", "Mayo, 31 días", "Junio, 30 días", 
          "Julio, 31 días", "Agosto, 31 días", "Septiembre, 30 días", "Octubre, 31 días", "Noviembre, 30 días", "Diciembre, 31 días"];
print(f"Mes {mes + 1} es: {meses[mes]}");