import os
import msvcrt
import time
import sys

def ejecutar_comando(comando, mensaje, espera=5):
    print(f"Ejecutando {mensaje}...\n")
    os.system(comando)
    time.sleep(espera)
    print("Puede visualizar el informe en el directorio Resultados\n")

def mostrar_menu():
    print("***********************************************")
    print("SISTEMA DE DIAGNOSTICO DE FALLAS EN RED")
    print("***********************************************\n")
    print("*******************MENU*********************\n")
    print("1- Realizar un ping")
    print("2- Verificar Traceroute")
    print("3- Verificar hostname")
    print("4- Solicitar ipconfig")
    print("5- Verificar DNS")
    print("6- Verificar Gateway")
    print("7- Monitorear procesos activos")
    print("8- Información sobre el sistema operativo")
    print("9- Ver las redes a las que se conectó el dispositivo")
    print("10- Visualizar historial del DNS")
    print("11- Vaciar la caché de DNS")
    print("12- Escaneo de Puertos")
    print("13- Comprobación de Conectividad a un Servidor Web")
    print("14- Verificar la Velocidad de la Red")
    print("15- Mostrar la Tabla de Enrutamiento")
    print("16- Visualización de Interfaces de Red")
    print("17- Salir del programa\n")

def diagnosticos():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Ingrese una opción: "))##no continua gracias al try, que por la condicion no le permite seguir
        except ValueError:
            print("¡Opción incorrecta! Por favor, ingrese un número del 1 al 17.")
            continue
        
        if opcion == 1:
            ip = input("Ingrese un número de IP o nombre de dominio: ")
            ejecutar_comando(f"ping {ip} > Resultados/Ping.txt", f"ping a {ip}", 20)
        
        elif opcion == 2:
            trace = input("Ingrese un número de IP o nombre de dominio: ")
            ejecutar_comando(f"tracert {trace} > Resultados/Traceroute.txt", f"traceroute a {trace}", 10)
        
        elif opcion == 3:
            ejecutar_comando("hostname > Resultados/Hostname.txt", "hostname", 2)
        
        elif opcion == 4:
            ejecutar_comando("ipconfig /all > Resultados/Ipconfig.txt", "ipconfig completo", 20)
        
        elif opcion == 5:
            dns = input("Ingrese un número de IP o nombre de dominio para verificar DNS: ")
            ejecutar_comando(f"nslookup {dns} > Resultados/DNS.txt", f"verificación de DNS para {dns}", 5)
        
        elif opcion == 6:
            gateway = input("Ingrese un número de IP del Gateway: ")
            ejecutar_comando(f"ping {gateway} > Resultados/Gateway.txt", f"verificación del Gateway {gateway}", 10)
        
        elif opcion == 7:
            ejecutar_comando("netstat -anob > Resultados/Procesos_activos.txt", "Netstat", 5)
        
        elif opcion == 8:
            ejecutar_comando("systeminfo > Resultados/Informacion_del_sistema.txt", "información del sistema operativo", 5)
        
        elif opcion == 9:
            ejecutar_comando("netsh wlan show profile > Resultados/Historial_de_redes.txt", "historial de redes wifi", 10)
        
        elif opcion == 10:
            ejecutar_comando("ipconfig /displaydns > Resultados/Historial_DNS.txt", "historial de DNS", 20)
        
        elif opcion == 11:
            ejecutar_comando("ipconfig /flushdns", "vaciado de caché DNS", 2)
        
        elif opcion == 12:
            ip = input("Ingrese un número de IP para el escaneo de puertos: ")
            ejecutar_comando(f"nmap {ip} > Resultados/Escaneo_de_Puertos.txt", f"escaneo de puertos para {ip}", 20)
        
        elif opcion == 13:
            url = input("Ingrese la URL del servidor web: ")
            ejecutar_comando(f"curl -I {url} > Resultados/Comprobacion_Web.txt", f"comprobación de conectividad a {url}", 10)
        
        elif opcion == 14:
            ejecutar_comando("speedtest-cli > Resultados/Velocidad_de_Red.txt", "prueba de velocidad de red", 20)
        
        elif opcion == 15:
            ejecutar_comando("route print > Resultados/Tabla_de_Enrutamiento.txt", "tabla de enrutamiento", 5)
        
        elif opcion == 16:
            ejecutar_comando("ipconfig /all > Resultados/Interfaces_de_Red.txt", "interfaces de red", 5)
        
        elif opcion == 17:
            print("¡Adiós!")
            break
        
        else:
            print("¡Opción incorrecta! Por favor, ingrese un número del 1 al 17.")
        
        print("Presione cualquier tecla para continuar...")
        msvcrt.getch()

if __name__ == '__main__':
    if not os.path.exists("Resultados"):
        os.mkdir("Resultados")
    diagnosticos()
