# PCAP Analysis – DNS Anomalies and Internal Reconnaissance   
**Tools:** Wireshark   
---

## 1. Overview

In this project, I analyzed a network capture file (`2022-03-21-traffic-analysis-exercise.pcap`) to identify suspicious activity related to DNS anomalies, internal reconnaissance, and possible post-exploitation behavior inside a Windows domain environment.


## 2. Objectives

- Detect unusual DNS activity  
- Identify suspicious domains or subdomains  
- Follow connections related to a specific host (10.0.19.9)  
- Detect internal reconnaissance techniques  
- Document the main findings in a clear and professional format  


## 3. Methodology

I used Wireshark to apply targeted filters and examine different parts of the capture:

- DNS analysis  
- Subdomain enumeration  
- DNS-to-internal IP pivot  
- LLMNR and NBNS traffic  
- SMB and LDAP communication  
- Protocol hierarchy breakdown  

All findings were supported with screenshots stored in the `evidence/` folder.


## 4. Findings

### **Finding 1 – High-volume DNS traffic toward suspicious domain**
I observed a large number of DNS queries to the domain `burnincandle.com` and several related subdomains.  
This is not normal behavior for a workstation and may indicate domain generation algorithms (DGA) or automated malware communication.

### **Finding 2 – Multiple suspicious subdomains**
The DNS queries included many unusual subdomains such as:
- `pad.burnincandle.com`  
- `burnincandle-dc.burnincandle.com`  
These names do not look legitimate and suggest automated or malicious activity.

### **Finding 3 – DNS response resolving to internal IP (10.0.19.9)**
Several DNS responses resolved the suspicious domain to the internal address `10.0.19.9`.  
This is unusual because external domains normally resolve to external IPs, not internal hosts.  
This behavior indicates redirection or command-and-control (C2) communication inside the environment.

### **Finding 4 – LLMNR and NBNS internal name resolution (reconnaissance)**
I identified active LLMNR and NBNS traffic, including queries for workstation names.  
This type of traffic is commonly abused by attackers to collect internal hostnames or perform poisoning attacks.

### **Finding 5 – SMB, LDAP and DCERPC traffic toward the same internal host**
After resolving the suspicious domain to 10.0.19.9, the workstation communicated with it using SMB, LDAP, and DCERPC.  
These protocols are typically used for authentication and domain controller interaction.  
This pattern suggests possible lateral movement or interaction with a compromised domain controller.


## 5. Screenshots

All evidence is stored in the `evidence/` directory:

Each screenshot supports one of the findings listed above.


## 6. Conclusion

This PCAP shows clear signs of suspicious behavior including DNS anomalies, internal reconnaissance, and communication with an internal IP using domain controller protocols.

If this activity happened in a real environment, I would recommend:

- Blocking the suspicious domain  
- Investigating the host 10.0.19.9  
- Reviewing authentication logs  
- Checking for lateral movement attempts  
- Running an endpoint investigation on the affected workstation  

---

## 7. Author
**Javier Ávila**  
Date: NOV/2025
