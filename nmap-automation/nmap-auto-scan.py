#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ----------------------------------------

# nmap_auto_scan.py

# Autor: Javier Ávila Andrade
# Junio 2025

# Descripción: Escaneo automatizado de red con Nmap y visualización de datos.



import nmap
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Crear el escáner Nmap
scanner = nmap.PortScanner()

# Definir la red que se va a escanear
red_objetivo = '192.168.1.0/24'

print(f"Iniciando escaneo de red en {red_objetivo}...\n")

# Ejecutar escaneo tipo ping para detectar dispositivos activos
scanner.scan(hosts=red_objetivo, arguments='-sn')

# Lista para almacenar resultados
resultados = []

# Procesar cada host encontrado
for host in scanner.all_hosts():
    if 'mac' in scanner[host]['addresses']:
        ip = scanner[host]['addresses'].get('ipv4', 'Desconocida')
        mac = scanner[host]['addresses'].get('mac', 'Desconocida')
        fabricante = scanner[host]['vendor'].get(mac, 'Desconocido')
        resultados.append({'ip': ip, 'mac': mac, 'fabricante': fabricante})

# Verificar si se encontraron dispositivos
if not resultados:
    print("No se detectaron dispositivos en la red.")
    exit()

# Crear un DataFrame con los resultados
df = pd.DataFrame(resultados)

# Generar nombre único para el archivo CSV según la fecha y hora actual
fecha_hora_actual = datetime.now().strftime('%Y%m%d_%H%M%S')
nombre_archivo_csv = f'logs_scan_{fecha_hora_actual}.csv'

# Guardar los resultados en el archivo CSV
df.to_csv(nombre_archivo_csv, index=False)
print(f"\nEscaneo finalizado. Resultados guardados en: {nombre_archivo_csv}")

# Mostrar tabla limpia en consola con los resultados
print("\nTabla de resultados del escaneo:\n")
print(df[['ip', 'mac', 'fabricante']].to_string(index=False))


# Estadísticas en texto

print("\nEstadísticas de fabricantes detectados:\n")
conteo_fabricantes = df['fabricante'].value_counts()
for fabricante, cantidad in conteo_fabricantes.items():
    print(f"  - {fabricante}: {cantidad} dispositivo(s)")


# Gráfica circular

plt.figure(figsize=(6, 6))
plt.pie(conteo_fabricantes, labels=conteo_fabricantes.index, autopct='%1.1f%%')
plt.title('Distribución de fabricantes detectados en la red')
plt.tight_layout()
plt.show()
