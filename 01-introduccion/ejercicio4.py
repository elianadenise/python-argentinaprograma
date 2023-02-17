### Ejercicio 4

# **Intereses**. Suponé que tenes $100 dólares, que podés invertir con un
# 10% de retorno anual. Después de un año, esto es  100 x 1.1 = 110 
# dólares y luego de dos años es 100 x 1.1 x 1.1 = 121. 
# Escribí el código para calcular cuanto dinero vas a tener 
# al cabo de 7 años, e imprimí el resultado. 

inversion = 100;
interes = 1.1;
anios = 0;
calculo_interes = 0;
while anios < 7:
    calculo_interes = inversion * interes;
    inversion = calculo_interes;
    anios += 1;
    print("Saldo total al final del año: ", anios, " es de: $", calculo_interes);