# Ejercicio 8

# Imagina que eres el gerente de una tienda en línea y estás revisando 
# tu base de datos de clientes. Descubres que algunos clientes se han registrado 
# varias veces con la misma información de contacto, pero diferentes nombres 
# de usuario. La lista con información de contacto que tenes es: 

clientes = [

  (1, "Ana", "García", "ana@example.com", "Calle Falsa 123"), 

  (2, "Pedro", "Martínez", "pedro@example.com", "Avenida Siempreviva 742"),

  (3, "Luisa", "Fernández", "luisa@example.com", "Calle Falsa 123"),

  (4, "Juan", "Pérez", "juan@example.com", "Calle Falsa 123"), 

  (5, "Ana", "García", "ana@example.com", "Calle Falsa 123")
  
  ]

# Donde el primer elemento de cada tupla es el numero de cliente, luego viene el nombre, 
# apellido, email y dirección.

# Para simplificar tu base de datos, decides eliminar los registros duplicados y ordenar 
# la lista de clientes alfabéticamente. Escribe un código que haga esto.

email_set = set()
clientes_unicos = []

for cliente in clientes:
    email = cliente[3]
    if email not in email_set:
        email_set.add(email)
        clientes_unicos.append(cliente)

ordenado = sorted(clientes_unicos, key=lambda x: x[1])

print(ordenado)