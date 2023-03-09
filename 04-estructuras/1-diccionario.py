# **Armando un diccionario de notas.** A continuación damos una lista de tuplas, 
# donde cada tupla corresponde a un alumno de un curso, con `(nombre, dni, nota)`. 
# Armá a partir de la lista un diccionario `dic_notas` que tenga como clave el nombre y como valor la nota de cada alumno.

alumnos = [
    ('Carlos Gómez', 41008418, 5),
    ('Gabriela Torres', 45790918, 8),
    ('Juan Pérez', 48327044, 9),
    ('Éric Guay', 35360531, 7),
    ('Juana Monte', 31583398, 10),
    ('Carla Díaz', 43772387, 6)];

# diccionario notas:

dic_notas = {
    alumnos[0][0] : alumnos[0][2],
    alumnos[1][0] : alumnos[1][2],
    alumnos[2][0] : alumnos[2][2],
    alumnos[3][0] : alumnos[3][2],
    alumnos[4][0] : alumnos[4][2],
    alumnos[5][0] : alumnos[5][2]
}

print(dic_notas);