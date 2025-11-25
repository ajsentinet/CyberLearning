# Port Scanner – Python (Three Versions)

This folder contains three versions of a Python-based port scanner, going from a simple scan to a faster and more complete implementation using multithreading. These scripts help me practice basic network scanning concepts and understand how ports and common services work.

## Project structure

- basic-version
  Contains a simple port scanner that checks ports from 20 to 1024 and reports which ones are open.

- advanced-version
  Extends the basic version by identifying the service commonly associated with each open port.

- threaded-version
  Uses multithreading to scan many ports at the same time, resulting in much faster performance.

## Purpose

These scripts demonstrate progressive improvements in port scanning, starting from a basic approach and moving toward a more efficient and informative implementation. Port scanning is a fundamental task in cybersecurity and helps understand system exposure and network behaviour.

## What each version demonstrates

### Basic version
- Simple TCP port checks
- Use of sockets in Python
- Basic timeout handling

### Advanced version
- Detection of open ports
- Identification of services using getservbyport
- More complete and structured output

### Threaded version
- Faster port scanning using threads
- Parallel execution of socket checks
- Improved efficiency and responsiveness

## How to run

Each version includes its own README.md with detailed instructions.
In general, run the desired script using:

python3 script-name.py

Then enter the target IP address or domain when prompted.

## Skills practiced

- Network scanning concepts
- Use of sockets in Python
- Basic service identification
- Multithreading for performance
- Script organization and documentation
- Introductory cybersecurity analysis

## Author

Javier Avila
