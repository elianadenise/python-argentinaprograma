# **Usando comprensión.** Volvé a rehacer los dos ejercicios anteriores, 
# pero esta vez usando comprensión.
alumnos = [
    ('Carlos Gómez', 41008418, 5),
    ('Gabriela Torres', 45790918, 8),
    ('Juan Pérez', 48327044, 9),
    ('Éric Guay', 35360531, 7),
    ('Juana Monte', 31583398, 10),
    ('Carla Díaz', 43772387, 6)]

# diccionario notas:
dic_notas = {alumno[0] : alumno[2] for alumno in alumnos};
print(dic_notas);

# lista diccionarios:
lista_de_dic = [{"nombre" : alumno[0], "dni" : alumno[1], "nota" : alumno[2]} for alumno in alumnos];
print(lista_de_dic);