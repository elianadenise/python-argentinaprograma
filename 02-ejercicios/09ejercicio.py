# ## Ejercicio 9:

# Escriba un programa que lea input del usuario: cantidad de días, horas, minutos y segundos y que en base a esos datos, calcule el total en segundos.
dias = int(input('dias: '))
horas = int(input('horas: '))
minutos = int(input('minutos: '))
segundos = int(input('dias: '))

totalseg = (dias * 24 * 60 * 60) + (horas * 60 * 60) + minutos * 60 + segundos

print(f'el total en segundos es {totalseg}')