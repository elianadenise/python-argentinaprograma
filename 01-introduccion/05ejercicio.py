# ## Ejercicio 5:

# Crea un código que tome como parámetro una frase y sea capaz 
# de contar el número de palabras que contiene. Haga un test con la frase: 
# "Me gusta estudiar python en la UNSAM". 

# Y si queremos contar los caracteres incluyendo los espacios. ¿Cómo seria?

# Prueba con otras frases, para eso podes usar la funcion de 
# ingreso de valores por teclado. 

frase = "Me gusta estudiar python en la UNSAM";
frase_a_array = frase.split();
contar_caracteres = len(frase);

contador_de_palabras = 0;
for palabras in frase_a_array:
    contador_de_palabras += 1;

print(contador_de_palabras)
print(contar_caracteres);
