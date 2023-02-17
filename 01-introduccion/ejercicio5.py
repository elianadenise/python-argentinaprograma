# ### Ejercicio 5
# **La hipoteca de David**. David solicitó un crédito a 30 años 
# para comprar una vivienda, con una tasa fija nominal anual del 5%. 
# Pidió \$500000 al banco y acordó un pago mensual fijo de \$2684,11.

# El siguiente es un programa que calcula el monto total que pagará David 
# a lo largo de los años:

# hipoteca

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1 + tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado:', round(total_pagado, 2))

# Supongamos que David adelanta pagos extra de \$1000 por mes durante 
# los primeros 12 meses de la hipoteca. Modificá abajo el programa 
# para incorporar estos pagos extra y que imprima el monto total pagado
# junto con la cantidad de meses requeridos. Debería dar un pago total 
# de 929965.62 en 342 meses.

# Pregunta adicional: investigar que hace la función `round`. 
# Qué hace el parámetro **2** en esta función?

# *(Ayuda: este ejercicio requiere que agregues una variable mes 
# y que prestes bastante atención a cuándo la incrementás, con 
# qué valor entra al ciclo y con qué valor sale del ciclo. Una 
# posiblidad es inicializar mes en 0 y otra es inicializarla en 1. 
# En el primer caso es problable que la variable salga del ciclo 
# contando la cantidad de pagos que se hicieron, en el segundo, 
# ¡es probable que salga contando la cantidad de pagos más uno!)*

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
pago_mensual_extra = 1000
meses = 0

while saldo > 0:
    if meses < 12:
        saldo = saldo * (1 + tasa/12) - pago_mensual - pago_mensual_extra
        total_pagado = total_pagado + pago_mensual + pago_mensual_extra
    else:        
        saldo = saldo * (1 + tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        
    meses = meses + 1

print('Total pagado:', round(total_pagado, 2))
print('Meses:', meses)


# **(Opcional)**. ¿Cuánto pagaría David si agrega $1000 por mes durante 
# cuatro años, comenzando en el sexto año de la hipoteca (es decir, 
# luego de 5 años)? Modificá tu programa de forma que la información
# sobre pagos extras sea incorporada de manera versátil. 
# Agregá las siguientes variables antes del ciclo, 
# para definir el comienzo, fin y monto de los pagos extras:

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
meses = 0

while saldo > 0:
    if meses >= pago_extra_mes_comienzo and meses <= pago_extra_mes_fin:
        saldo = (saldo * (1 + tasa/12) - pago_mensual) - pago_extra
        total_pagado = total_pagado + pago_mensual + pago_extra
    else:        
        saldo = saldo * (1 + tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        
    meses += 1

print('Total pagado:', round(total_pagado, 2))
print('Meses:', meses)
