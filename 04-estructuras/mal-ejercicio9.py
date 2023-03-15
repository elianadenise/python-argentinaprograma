# # Ejercicio 9

# Escribe un programa que le permita al usuario registrar información sobre 
# estudiantes en una escuela. Cada estudiante tendrá un nombre y apellido, 
# una edad y una lista de materias en las que está inscrito.
# El programa deberá guardar toda la información guardada, y además deberá 
# indicar cuantas y cuales son las materias a las que hay por lo menos un estudiante inscrito. 

# Probá para las siguientes informaciones

# - Nombre: Juan Perez,
#   Edad: 18,
#   Materias: Matemáticas, Física, Química
# - Nombre: Ana Suarez, 
#   Edad: 17,
#   Materias: Lengua, Historia, Geografía
# - Nombre: Pedro Martinez,
#   Edad: 16,
#   Materias: Inglés, Música
# - Nombre: María Barbosa,
#   Edad: 18,
#   Materias: Matemáticas, Física, Dibujo
# - Nombre: Luis Sanchez, 
#   Edad: 17,
#   Materias: Biología, Historia, Geografía

# con un while como en java hasta que dice s

info = input("Ingrese una lista de los alumnos separados por '-' (guiones medios). De la siguiente manera:\n Nombre Apellido/ Edad/ Materias: \n")
info=info.split("-")
alumnos=[]
for tupla in info:
  tupla=tupla.split("/")
  aux={'Nombre':tupla[0] , 'Edad':tupla[1], 'Materias':tupla[2]}
  alumnos.append(aux)
materias = []
for alumno in alumnos:
  aux=alumno['Materias'].split(', ')
  for mat in aux:
    materias.append(mat)
print(f'\nLas materias que tienen por lo menos un inscripto son: {set(materias)}\n')
print(f'Toda la infotmación ingresada quedó guardada en la siguiente lista de alumnos: \n{alumnos}')