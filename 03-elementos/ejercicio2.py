# ### Ejercicio 2

# **Jeringoso simple**. Usá una iteración sobre el string `cadena` para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' 
# según corresponda luego de cada vocal. Podés probar tu código cambiando la cadena inicial por otra palabra, como 'apa' o 'boligoma'.

# jeringoso
# cadena = 'Geringoso'
# capadepenapa = ''

# for c in cadena:
  

# print(capadepenapa)

palabra=input("Escribí la palabra que quieras en geringoso: ")
palabraNueva=""

for letra in palabra:
    if letra=="a" or letra=="á":
        palabraNueva = palabraNueva + "apa"

    elif letra=="e" or letra=="é":
        palabraNueva = palabraNueva + "epe"

    elif letra=="i" or letra=="í":
        palabraNueva = palabraNueva + "ipi"

    elif letra=="o" or letra=="ó":
        palabraNueva = palabraNueva + "opo"

    elif letra=="u" or letra=="ú":
        palabraNueva = palabraNueva + "upu"

    else:
        palabraNueva=palabraNueva + letra

print("Palabra en geringoso:", palabraNueva)