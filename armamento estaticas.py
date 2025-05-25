class Armamento:
  __daño = "200"
  __calidad = "Legendario"
  __tipo = "Melee"

Rango = Armamento()
print(Rango.__daño)
Rango.__daño = 100
print(Rango.__daño)

print(Rango.__calidad)
Rango.__calidad = Estropeado
print(Rango.__calidad)

print(Rango.__tipo)
Rango.__tipo = Mago
print(Rango.__tipo)
