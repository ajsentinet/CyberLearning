#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escáner de puertos con identificación de servicios
Autor: Javier Ávila Andrade
Fecha: Junio 2025

Este script escanea los puertos del 20 al 1024 en un host (IP o dominio)
y muestra cuáles están abiertos, junto con el nombre del servicio asociado (si se conoce).
"""

import socket  # Para conexiones de red
from datetime import datetime  # Para calcular el tiempo de ejecución

# Solicita al usuario la dirección IP o dominio a escanear
target = input("Ingresa la IP o dominio a escanear: ")

# Define el rango de puertos a escanear
start_port = 20
end_port = 1024

print(f"\nEscaneando {target} del puerto {start_port} al {end_port}...\n")
start_time = datetime.now()  # Marca el tiempo de inicio

# Recorre cada puerto en el rango especificado
for port in range(start_port, end_port + 1):
    try:
        # Crea un socket para intentar conexión TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Limita el tiempo de espera por puerto

        # Intenta conectarse al puerto
        result = sock.connect_ex((target, port))

        # Si la conexión fue exitosa (0), el puerto está abierto
        if result == 0:
            try:
                # Obtener el nombre del servicio (como HTTP, SSH, etc.)
                service = socket.getservbyport(port)
            except:
                service = "Servicio desconocido"
            print(f"[✓] Puerto {port} abierto - {service.upper()}")
        
        sock.close()  # Cierra la conexión
    except KeyboardInterrupt:
        print("\nEscaneo interrumpido por el usuario.")
        break
    except Exception as e:
        print(f"Error al escanear el puerto {port}: {e}")

end_time = datetime.now()
duration = end_time - start_time

# Muestra cuánto tiempo duró el escaneo
print(f"\nEscaneo completado en {duration}")
