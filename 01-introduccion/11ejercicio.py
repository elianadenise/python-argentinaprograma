# ## Ejercicio 11:

# El alquiler de un auto cuesta `$3000` por día y `$220` por cada kilometro recorrido. 
# Escriba un programa que calcule el valor a pagar dependiendo del número de días alquilado y de km total recorridos. 

# Verifique su programa calculando el importe a pagar por un alquiler de 10 días y 400 kilometros recorridos en esos 10 días. Pruebe otros ejemplos. 

alquiler_por_dia = 3000;
precio_por_km = 220;

dias_alquilados = int(input("Cantidad de dias de alquiler: "));
kilometros_recorridos = float(input("Cantidad de kilometros recorridos totales: "))

importe_total = alquiler_por_dia * dias_alquilados + precio_por_km * kilometros_recorridos;
print(f"${importe_total}");