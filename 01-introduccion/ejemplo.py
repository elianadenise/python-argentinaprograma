# obelisco.py
grosor_billete = 0.11 * 0.001 # grosor de un billete en metros
altura_obelisco = 67.5 # altura en metros
num_billetes = 1
dia = 1

while num_billetes * grosor_billete <= altura_obelisco:
  print(dia, num_billetes, num_billetes * grosor_billete)
  dia = dia + 1
  num_billetes = num_billetes * 2
  # los bloques de codigo se define por la identacion

print('Cantidad de días', dia)
print('Cantidad de billetes', num_billetes)
print('Altura final:', num_billetes * grosor_billete)

# 1 1 0.00011
# 2 2 0.00022
# 3 4 0.00044
# 4 8 0.00088
# 5 16 0.00176
# 6 32 0.00352
# 7 64 0.00704
# 8 128 0.01408
# 9 256 0.02816
# 10 512 0.05632
# 11 1024 0.11264
# 12 2048 0.22528
# 13 4096 0.45056
# 14 8192 0.90112
# 15 16384 1.80224
# 16 32768 3.60448
# 17 65536 7.20896
# 18 131072 14.41792
# 19 262144 28.83584
# 20 524288 57.67168
# Cantidad de días 21
# Cantidad de billetes 1048576
# Altura final: 115.34336