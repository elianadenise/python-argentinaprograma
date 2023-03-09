# **Lista de diccionarios.** Usando la misma lista de antes, 
# armá ahora una nueva *lista* en la que a cada alumno le corresponde 
# un diccionario con las claves 'nombre', 'dni' y 'nota'. 
# Por ejemplo, el primer elemento es `{'Nombre':'Carlos Gómez', 'dni':41008418, 'nota':5}`.

alumnos = [
    ('Carlos Gómez', 41008418, 5),
    ('Gabriela Torres', 45790918, 8),
    ('Juan Pérez', 48327044, 9),
    ('Éric Guay', 35360531, 7),
    ('Juana Monte', 31583398, 10),
    ('Carla Díaz', 43772387, 6)]

# lista diccionario:

lista_dic_notas = [
    {
        "nombre" : alumnos[0][0],
        "dni" : alumnos[0][1],
        "nota" : alumnos[0][2]
    },
    {
        "nombre" : alumnos[1][0],
        "dni" : alumnos[1][1],
        "nota" : alumnos[1][2]
    },
    {
        "nombre" : alumnos[2][0],
        "dni" : alumnos[2][1],
        "nota" : alumnos[2][2]
    },
    {
        "nombre" : alumnos[3][0],
        "dni" : alumnos[3][1],
        "nota" : alumnos[3][2]
    },
    {
        "nombre" : alumnos[4][0],
        "dni" : alumnos[4][1],
        "nota" : alumnos[4][2]
    },
    {
        "nombre" : alumnos[5][0],
        "dni" : alumnos[5][1],
        "nota" : alumnos[5][2]
    }
];

print(lista_dic_notas);