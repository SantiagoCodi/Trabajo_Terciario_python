x=1
while x==1:
    edad=int(input('Ingrese la edad del personal: '))
    gen=input('Ingrese el genero del personal: ')
    if edad>=1 and edad<=120:
        x==0
    else:
        break
    if gen=="m":
        break
    elif gen=="f":
        break
    else:
        print('Error al ingresar datos, vuelva a intentarlo')
if gen=="f" and edad>=60:
    print("El personal puede jubilarse")
elif edad >=65:
    print("El personal puede jubilarse")
else:
    print("El personal no puede jubilarse")


