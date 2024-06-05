x=1
may=0
men=0
while x<=10:
    nota=float(input('ingrese la nota del alumno: '))
    if nota >=7:
        may=may+1
    else:
            men=men+1
    x=x+1
print('Hay un total de',men, ' notas menores a 7 y ',may, ' notas iguales o mayores a 7')
