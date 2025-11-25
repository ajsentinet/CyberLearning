#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# ----------------------------------------
# ANALIZADOR DE REGISTROS EN PYTHON

# Autor: Javier Ávila Andrade
# Junio 2025

# Descripción: Script para analizar los registros del honeypot con Pandas.
#              Muestra cantidad de conexiones por IP, puertos usados y si se enviaron datos.
# ----------------------------------------
import pandas as pd

archivo = "registros_honeypot.csv"

# Cargamos el archivo CSV y lo guardamos como un "DataFrame"
df = pd.read_csv(archivo)

# Mostramos filas del archivo para confirmar que se leyó correctamente
print(" Primeros registros encontrados en el archivo:")
print(df, "\n")

# Mostramos cuántas veces se conectó cada dirección IP
print(" Cantidad de intentos por dirección IP:")
conteo_por_ip = df["ip"].value_counts()
print(conteo_por_ip, "\n")

# Mostramos desed qué puertos remotos se intentaron más conexiones
print(" Puertos remotos más usados por los clientes:")
puertos_mas_usados = df["puerto"].value_counts()
print(puertos_mas_usados, "\n")

# Filtramos las conexiones que sí enviaron datos
print(" Conexiones que sí enviaron algún dato:")
con_datos = df[df["dato_recibido"] != "[Sin datos enviados]"]
print(con_datos[["ip", "dato_recibido"]], "\n")

# Mostramos un resumen final de todo el análisis
print(" Resumen general del análisis: \n")
print(f" Total de conexiones registradas: {len(df)}")
print(f" Conexiones con datos enviados: {len(con_datos)}")
print(f" Conexiones sin datos enviados: {len(df) - len(con_datos)}")
print(f" Total de IPs diferentes que se conectaron: {df['ip'].nunique()}")
