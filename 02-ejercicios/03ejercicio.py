# ## Ejercicio 3:

# *El índice de masa corporal (IMC) se puede calcular utilizando la siguiente fórmula:*

# > *IMC = P / A^2*

# > *donde P es el peso de la persona en kilogramos y A es la altura de la misma persona en metros. La fórmula resulta en un número que se utiliza para determinar si una persona está en un peso saludable o no.* 

# *Un IMC normal se encuentra entre 18.5 y 24.9 kg/m^2. Un IMC menor a 18.5 kg/m^2 se considera bajo peso, mientras que un IMC mayor a 25 kg/m^2 se considera sobrepeso. Un IMC mayor a 30 kg/m^2 se considera obesidad. Sin embargo, estos valores son solo una guía y no son válidos para todas las personas, especialmente aquellas con una gran cantidad de músculo o deportistas.*

# **Crea un programa que te pida (usando input()) las siguientes informaciones: nombre, edad, peso en kg y altura en m y que te devuelva el nombre, la edad y el índice de masa corporal de esa persona.**


# *PISTA: input() siempre devuelve siempre una cadena*

# input() promptea al usuario y guarda esa variable COMO UNA CADENA (str).
nombre = input('¿Nombre?: ')

edad_str = input('¿Edad?: ')
edad = int(edad_str)  # Como input guarda la variable como cadena, hay que 'castearla' (convertir su tipo) a entero, con la funcion int() (int=integer=entero)
# ¿Que pasa si el usuario introduce una palabra en vez de un numero?

altura_str = input('¿Altura en cm?: ')
altura = float(altura_str) 

peso_str = input('¿Peso en kilos?: ')
peso = int(peso_str) 

imc = peso / (altura * altura);
print(imc)

if imc >= 18.5 and imc <= 24.9:
    print("IMC normal");
elif imc < 18.5 and imc >= 0:
    print("IMC menor");
elif imc > 24.9:
    print("IMC mayor");