import math

cateto_oposto = float(input("digite o cateto oposto: "))
cateto_adjacente = float(input("digite o cateto adjacente: "))

hipotenusa = math.hypot(cateto_oposto,cateto_adjacente)

print("Sua Hipotenusa é {:.2f}!!!".format(hipotenusa))
