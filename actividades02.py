# Programa que solicite base y altura de un rectágulo,
# y se muestre area y perímetro del mismo.

base=float(input("Ingrese la base del rectangulo"))
altura=float(input("Ingrese la altura del rectangulo"))
area=base*altura
print("El area del rectangulo es= ",area)
print("El perimetro del rectangulo es= ",2*area)

# Escribir un programa que solicite una cantidad de segundos
# y devuelva cuantas horas, minutos y segundos son
# en el formato "hh:mm:ss"
    #ejemplo 
    # 3661 segundos
    # 1:1:1
    # 60 segundos
    # 0:1:0
    # 3606
    # 1:0:6
segundos=float(input("ingrese la cantidad de segundos"))
hora=segundos//3600
minutos=(segundos-hora*3600)//60
segundos1=segundos-((hora*3600)+(minutos))


# Escriba un programa que permita el ingreso de 5 productos.
# De cada producto se ingresa el precio y la cantidad adquirida.
# mostrar el total de la compra, y detalle del subtotal de cada producto.

precio1=float(input("ingrese el precio del producto 2"))
cant_pre_1=int(input("ingrese la cantidad del producto"))
precio2=float(input("ingrese el precio del producto 2"))
cant_pre_2=int(input("ingrese la cantidad del producto"))
precio3=float(input("ingrese el precio del producto 3"))
cant_pre_3=int(input("ingrese la cantidad del producto"))
precio4=float(input("ingrese el precio del producto 4"))
cant_pre_4=int(input("ingrese la cantidad del producto"))
precio5=float(input("ingrese el precio del producto 5"))
cant_pre_5=int(input("ingrese la cantidad del producto"))

subtotal_1=precio1*cant_pre_1
subtotal_2=precio2*cant_pre_2
subtotal_3=precio3*cant_pre_3
subtotal_4=precio4*cant_pre_4
subtotal_5=precio5*cant_pre_5
total_compra=subtotal_1+subtotal_2+subtotal_3+subtotal_4+subtotal_5
print("El subtotal del producto 1= ", subtotal_1)
print("El subtotal del producto 2= ", subtotal_2)
print("El subtotal del producto 3= ", subtotal_3)
print("El subtotal del producto 4= ", subtotal_4)
print("El subtotal del producto 5= ", subtotal_5)
print("El total de la compra es igual a= ", total_compra)

# Escribe un programa que solicite el nombre del r
# emitente de un mensaje y
# su destinatario.
# y muestre la siguiente plantilla de mensaje remplazando
# [dest] por el destinatario, y [re] por el remitente.
plantilla = """Hola [dest],
Gracias por elegirnos para viajar, que disfrute y aprecie su destino.
Atentamente [re]
"""
remitente=input("Ingrese remitente; ")
destinatario=input("Ingrese destinatario: ")
plantilla="""Hola [dest],
Gracias pro elegirnos para viajar, que disfrute y aprecie su destino.
Atentamente [re]
"""
print(plantilla.replace("[dest]",destinatario).replace("[re]",remitente))


    # ejemplo
    # destinatario = "axel"
    # remitente = "pedro"
    #salida: 
    # Hola axel,
    # Gracias por elegirnos para viajar, que disfrute y aprecie su destino.
    # Atentamente pedro


# Escribir programa que solicite al usuario peso y estatura del paciente
# y muestre el índice de masa corporal.
peso=float(input("Ingrese el peso del paciente"))
estatura=float(input("Ingrese la estatura del paciente"))
ind_ma_cor=peso/estatura**2
print("El indice de masa corporal del paciente es= ",ind_ma_cor)


# Realizar una calculadora de plazo fijos.
# que solicite al usuario cantidad a invertir, cantidad de dias
# y TNA.
can_inv=float(input("Ingrese la cantidad que desea invertir"))
can_dias=int(input("Ingrese la cantidad de dias"))
tna=float(input("Ingrese el TNA"))
plazo_fijo=can_inv*(tna*can_dias/365)


# escriba un programa que solicite dos numeros enteros positivos a y b.
# luego concatenar el resultado de la suma de a+b con el resultado del
    # producto de a*b.
# luego al numero formado de la concatenación dividir por el resto de 
    # la división de a por b.

    #ejemplo
    # a=10 y b=4
    # a+b = 14 y a*b=40
    # concatenacion = "1440"
    # resto división a por b = 2
    # 1440/2 = 720
    # el programa debería mostrar por pantalla 720