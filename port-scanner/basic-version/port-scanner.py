#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Port Scanner en Python
----------------------

Este script realiza un escaneo de puertos TCP en un host determinado,
en un rango de puertos definido, e informa cuáles están abiertos.

Autor: Javier Ávila Andrade
Fecha: Junio 2025
"""

import socket
from datetime import datetime

# Solicita al usuario la dirección IP o dominio del objetivo
target = input("Ingresa la IP o dominio a escanear: ")

# Define el rango de puertos a escanear
start_port = 20
end_port = 1024

print(f"\nEscaneando {target} del puerto {start_port} al {end_port}...\n")

# Registra el tiempo de inicio del escaneo
start_time = datetime.now()

# Recorre el rango de puertos definidos
for port in range(start_port, end_port + 1):
    # Crea un socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # Define un tiempo máximo de espera por puerto

    # Intenta conectarse al puerto del objetivo
    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[✓] Puerto {port} abierto")

    sock.close()  # Cierra el socket después de cada intento

# Registra el tiempo de finalización del escaneo
end_time = datetime.now()
scan_duration = end_time - start_time

# Muestra duración total del escaneo
print(f"\nEscaneo completado en {scan_duration}")
