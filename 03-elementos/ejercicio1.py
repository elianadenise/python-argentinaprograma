# **Rebotes**. Una pelota de goma es arrojada desde una altura de 100 metros
# y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. 
# Escribí un programa/script que imprima una tabla mostrando las alturas 
# que alcanza en cada uno de sus primeros diez rebotes. 

# ejercicio con for

altura = 100;
salto = 3/5;
for i in range(10):
    altura = round(altura * salto, 2);
    print(f"Salto {i+1}: {altura}");


