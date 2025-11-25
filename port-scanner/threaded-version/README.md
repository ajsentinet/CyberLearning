# Threaded Port Scanner – Python

This project is the third version of a port scanner that I improved step by step.
In this version, the performance is optimized using multithreading, allowing many ports to be scanned at the same time. This makes the scan significantly faster than the previous versions.

## What this script does

- Scans ports from 20 to 1024 on a target IP address or domain
- Shows which ports are open
- Attempts to identify the service commonly associated with each port (HTTP, FTP, SSH, etc.)
- Performs all tasks in parallel using threads

## What I learned

- How multithreading works in Python using the threading module
- How to make port scanning much more efficient
- How to detect and identify common services behind open portss
- The importance of adjusting timeouts to avoid delays or stalled scans
- How to document a script clearly so it can be reused or improved later

## How to use

1. Open your terminal
2. Run the script: threaded-port-scanner.py
3. Enter the target IP address or domain when prompted (for example: scanme.nmap.org)
4. The script will display open ports and the service associated with each one in real time

![threaded-port-scanner](evidence/threaded-port-scanner)

## Author

Javier Avila
