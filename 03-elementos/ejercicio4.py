# ### Ejercicio 4

# Supongamos que la población del país A es del orden de 75000 habitantes con una tasa de crecimiento anual del 4% 
# y la población del país B es de 230000 habitantes con una tasa de crecimiento del 1,2%. 
# Haz un programa que calcule y escriba el número de años necesarios para que la población del país A supere o iguale a la población del país B, 
# tasas de crecimiento mantenidas.

poblacion_pais_a = 75000;
poblacion_pais_b = 230000;
tasa_crecimiento_a = 4;
tasa_crecimiento_b = 1.2;
anios_necesarios = 0;

while poblacion_pais_a <= poblacion_pais_b:
    poblacion_pais_a += (poblacion_pais_a / 100) * tasa_crecimiento_a;
    poblacion_pais_b += (poblacion_pais_b / 100) * tasa_crecimiento_b;
    anios_necesarios += 1;

poblacion_pais_a = int(poblacion_pais_a);
poblacion_pais_b = int(poblacion_pais_b);

print(f"los anios necesarios son: {anios_necesarios}");
print(f"poblacion pais a: {poblacion_pais_a}");
print(f"poblacion pais b: {poblacion_pais_b}");