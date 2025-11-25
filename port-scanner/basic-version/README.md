# Basic Port Scanner – Python

This project contains a simple Python port scanner designed to detect which ports are open on a target IP address or domain. It scans ports in the range 20 to 1024 and serves as an introductory exercise to understand how ports and network services work.

## Purpose

Port scanners are commonly used in cybersecurity for both defensive and assessment tasks. They help:

- Identify services that are open without need or by mistake
- Understand the exposure level of a system
- Prepare for more advanced analysis in real environments

## How to use

1. Run the script named port_scanner.py
2. Enter an IP address or domain when prompted
   Example targets: google.com, scanme.nmap.org
3. The program will display which ports respond as open

![port-scanner](evidence/port-scan.png)

## What I learned

- A clearer understanding of ports and how services like SSH, HTTP, and FTP communicate through them
- How to use Python’s socket library to test TCP connections and detect open ports
- The importance of using a timeout to avoid a frozen scan
- How to automate basic scanning tasks without relying on external tools like Nmap
- How to write and document small security scripts in a more structured way

## Author

Javier Avila
