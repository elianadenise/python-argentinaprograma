# ### Ejercicio 5

# **Notas**. Las notas obtenidas en por el alumno A durante su cursada fueron: 8, 7, 7, 6, 9, 10, 8, 9. El alumno B obtuvo las siguientes notas: 9, 8, 8, 9, 5, 8, 9, 7. 
# Realizar un programa que calcule la nota media y que muestre quien sacó la nota mayor y quien sacó la nota menor.  

estudiante_a = [8, 7, 7, 6, 9, 10, 8, 9];
estudiante_b = [9, 8, 8, 9, 5, 8, 9, 7];
promedio_a = 0;
promedio_b = 0;
acumulado_a = 0;
acumulado_b = 0;

for nota in estudiante_a:
    acumulado_a += nota;
    promedio_a = acumulado_a / len(estudiante_a);
    
for nota in estudiante_b:
    acumulado_b += nota;
    promedio_b = acumulado_b / len(estudiante_b);
    
if promedio_a > promedio_b:
    print(f"El estudiante a posee un promedio: {round(promedio_a, 2)}; y es mayor al promedio del estudiante b: {round(promedio_b, 2)}");
elif promedio_a == promedio_b:
    print(f"Los estudiantes tienen el mismo promedio.");
else:
    print(f"El estudiante b posee un promedio: {round(promedio_b, 2)}; y es mayor al promedio del estudiante a: {round(promedio_a, 2)}");