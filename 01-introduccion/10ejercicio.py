# # Ejercicio 10:

# Haga un programa que pregunte por el precio de una mercaderia y el porcentaje de descuento de la misma y que calcule el importe del descuento y el precio a pagar.

precio = float(input("Ingrese el precio: "));
descuento = int(input("Ingrese el descuento: "));

importe = precio - ((precio * descuento) / 100);
print(f"$ {importe}");