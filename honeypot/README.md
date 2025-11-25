# Simple Honeypot in Python and Connection Analyzer

This project contains a simple honeypot that simulates a fake server and logs connection attempts, as well as a Python script that analyzes those logs to extract useful information.

## What this project does

### simple_honeypot.py

- Listens for incoming connections on port 2222.
- Simulates a fake server named tarjetas_clientes_2025.
- Records the following information:
  - Visitor IP address
  - Remote port
  - Date and time
  - Data sent by the client
- Saves everything into the honeypot-logs.csv file.

### honeypot_log_analysis.py

- Reads the log file in CSV format.
- Displays:
  - Total number of recorded connections 
  - Connections where data was received 
  - Number of attempts per IP address 
  - Remote ports used by the clients 

## How to run

### 1. Run the honeypot

Command:
python3 simple_honeypot.py

From another terminal or a device on the same network, connect using:
nc 2222
Example:
nc 192.168.1.93 2222

![simple-honeypot](evidence/simple-honeypot.png)

### 2. Run the analyzer

Command:
python3 honeypot-log-analysis.py

## Example output (honeypot)

[+] Server tarjetas_clientes_2025 active on port 2222
[*] Waiting for connections...
[!] Connection detected from 192.168.1.75:54089 at 2025-06-10 18:22:37
    Data received: Soy un cliente  

## Example content of honeypot_logs.csv

fecha_hora,ip,puerto,dato_recibido
2025-06-10 18:22:37,192.168.1.75,54089,Preguntas frecuentes
2025-06-10 18:22:40,192.168.1.75,54090,[Sin datos enviados]

## Example output (analyzer)

Records loaded: 15 rows
Connections with data: 5

Attempts per IP address:
192.168.1.75    12
192.168.1.88     3

Remote ports used:
54089    4
54090    3
...

![honeypot-log-analysis](evidence/honeypot-log-analysis.png)

## What I learned

- Creating TCP servers using sockets.
- Structured logging of connections in CSV format.
- Event analysis using Python and pandas.
- First steps in monitoring network activity.

---
Javier Avila
