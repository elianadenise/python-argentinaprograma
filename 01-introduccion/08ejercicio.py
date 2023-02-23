# ## Ejercicio 8:
# Escriba un programa que se utilizará para decidir si un alumno ha aprobado o no. 
# Para ser aprobado, todos los promedios del alumno deben ser superiores a 7. 
# Considere que el alumno cursa sólo tres asignaturas, y que la calificación 
# de cada una de ellas se almacena en las siguientes variables: materia1, materia2 y materia3.

materia1 = int(input("Ingrese la nota de la primera materia: "));
materia2 = int(input("Ingrese la nota de la segunda materia: "));
materia3 = int(input("Ingrese la nota de la tercera materia: "));

if materia1 >= 7 and materia2 >= 7 and materia3 >= 7 and materia1 <= 10 and materia2 <= 10 and materia3 <= 10:
    print("Aprobado")
else:
    print("Desaprobado")