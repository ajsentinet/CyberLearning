#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ----------------------------------------
# HONEYPOT SIMPLE EN PYTHON

# Autor: Javier Ávila Andrade
# Junio 2025

# Descripción: Este script simula un servidor falso (honeypot) que escucha conexiones,
#              registra quién intenta conectarse y guarda los datos en un archivo .csv.
# ----------------------------------------


import socket
import datetime
import os


# Configuro el puerto donde va a "escuchar" el honeypot.
PUERTO = 2222  # Puedes cambiarlo por 21 (FTP), 22 (SSH), 80 (HTTP), etc.

# Le doy un nombre llamativo al "servicio falso" que estoy simulando.
NOMBRE_SERVICIO = "Servidor tarjetas_clientes_2025"

# Archivo donde se guardarán los registros
ARCHIVO_LOG = "registros_honeypot.csv"

# Si el archivo de logs no existe, lo creo con encabezados
if not os.path.exists(ARCHIVO_LOG):
    with open(ARCHIVO_LOG, "w") as archivo:
        archivo.write("fecha_hora,ip,puerto,dato_recibido\n")

# Creo un socket que escuchará conexiones TCP
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(("0.0.0.0", PUERTO))  # Escucha en todas las interfaces de red
servidor.listen(5)  # Permite hasta 5 conexiones en cola

print(f"[+] {NOMBRE_SERVICIO} activo en el puerto {PUERTO}")
print("[*] Esperando conexiones...\n")

# Ciclo infinito para aceptar conexiones
while True:
    cliente, direccion = servidor.accept()
    ip, puerto = direccion
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"[!] Conexión detectada de {ip}:{puerto} a las {fecha_hora}")

    try:
        datos = cliente.recv(1024).decode(errors='ignore').strip()
        if not datos:
            datos = "[Sin datos enviados]"
    except:
        datos = "[Error al recibir datos]"

    print(f"    ↳ Datos recibidos: {datos}\n")

    # Guardar los datos en el archivo de log
    with open(ARCHIVO_LOG, "a") as archivo:
        archivo.write(f"{fecha_hora},{ip},{puerto},{datos}\n")

    # Enviar una respuesta falsa (como si fuera un servicio real)
    mensaje_falso = "Bienvenido al servidor de datos bancarios. Acceso restringido.\n"
    cliente.send(mensaje_falso.encode())

    cliente.close()
