#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Escáner de puertos con multithreading
Autor: Javier Ávila Andrade
Fecha: Junio 2025

Este script realiza un escaneo rápido de puertos en un host utilizando hilos (threads),
lo que permite ejecutar múltiples escaneos al mismo tiempo y acelerar el proceso.
"""

import socket          # Para crear conexiones TCP
import threading       # Para usar múltiples hilos (procesamiento paralelo)
from datetime import datetime  # Para medir el tiempo total del escaneo

# Solicita al usuario el objetivo del escaneo
target = input("Ingresa la IP o dominio a escanear: ")

# Rango de puertos a escanear 
start_port = 20
end_port = 1024

print(f"\nEscaneando {target} del puerto {start_port} al {end_port} con hilos...\n")

# Inicio del escaneo
start_time = datetime.now()

# Función que escanea un solo puerto
def scan_port(port):
    try:
        # Crea un socket para intentar conectarse al puerto
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # Tiempo máximo de espera por puerto

        result = sock.connect_ex((target, port))  # Devuelve 0 si se conecta exitosamente

        if result == 0:
            try:
                # Identifica el servicio que usa ese puerto
                service = socket.getservbyport(port)
            except:
                service = "Servicio desconocido"
            print(f"[✓] Puerto {port} abierto - {service.upper()}")
        
        sock.close()

    except:
        pass

# Lista para guardar todos los hilos que se van a crear
threads = []

# Crea un hilo por cada puerto y lo lanza
for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

# Espera a que todos los hilos terminen antes de continuar
for thread in threads:
    thread.join()

# Final del escaneo
end_time = datetime.now()
duration = end_time - start_time

# Imprime cuánto tiempo tomó el escaneo
print(f"\nEscaneo completado en {duration}")
