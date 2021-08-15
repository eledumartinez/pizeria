#la entrada cuesta
# $20 si tiene hasta 10años
# $50 si tiene entre 10 y 18 años
# $100 si tiene 18 o mas años
#preguntar edad e imprimir cuanto cuesta
#la entrada


edad = int(input("ingrese edad: "))

if (edad <= 10):
	print("precio de la entrada: $20")
else:
	if (edad > 10 and edad <18):
		print("precio de la entrada: $50")
	else:
		print("precio de la entrada: $100")

