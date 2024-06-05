#día de temperatura max
dtm=1
#temperatura max
tm=0
#contador de pasar los 25°
c=0
#promedio temp
p=0
#variable acumuladora para el promedio
a=0
for i in range(1,31,1):
    temp= int(input(f'Temperatura del día N°{i}: '))
    a=temp+a
    #funciona pero no informa de dobles picos
    if temp > 25:
        c=c+1
    if temp > tm:
        tm=temp
        dtm=i
p=(a/30)
print(f'La temperatura máxima del mes fue {tm}° en el día {dtm}')
print(f'El promedio de la temperatura ese mes es de {p}°')
print(f'la cantidad de días que pasaron los 25° fue de {c}')
