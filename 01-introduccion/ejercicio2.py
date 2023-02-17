    ### Ejercicio 2
# **Rebotes**. Una pelota de goma es arrojada desde una altura de 100 metros
# y cada vez que toca el piso salta 3/5 de la altura desde la que cayó.
# Escribí un programa/script que imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.

# con el uso de while
altura = 100;
salto = 0.6;
rebotes = 0;
while rebotes < 10 and altura >= 0:
    pelota_salto = altura * salto;
    altura = pelota_salto;
    rebotes = rebotes + 1;
    print("ahora la altura del salto es de: ", altura);
    print("la cantidad de rebotes es: ", rebotes);
    
# altura = 100
# for i in range(10):
#     altura*=0.6
#     print(altura)

# con el uso de for
altura_pelota = 100;
altura_alcanzada = altura_pelota * 0.6;
piques = 10;

for pique in range(piques): 
    print(pique, (altura_alcanzada));
    altura_alcanzada = altura_alcanzada * 0.6;