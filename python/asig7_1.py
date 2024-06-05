#Consigna,
#Realizar la carga del precio de un producto y la cantidad a llevar. Mostrar cuanto se debe pagar (se ingresa un valor entero en el precio del producto)
precio=int(input('Ingrese el precio del producto: '))
#precio del prducto, con int porque son precios enteros
cantidad=int(input('Ingrese la cantidad del producto: '))
#cantidad
pagar=precio*cantidad
#funcion para determinar el total a pagar
print('Se debe pagar un total de', pagar)
#mostrar el resultado de la funcion