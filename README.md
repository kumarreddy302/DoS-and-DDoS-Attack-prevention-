## Dos and DDos attack prevention

This project aims to protect servers from Denial-of-Service (DoS) and Distributed Denial-of-Service (DDoS) attacks in real time. The code monitors log files and detects suspicious activity, such as excessive requests from a single IP address or continuous requests from multiple IPs. Upon identifying suspicious activity, the code blocks the corresponding IP addresses, preventing them from further disrupting the server's operations.

### Installation

To install the required dependencies, follow these steps:

1. Install the `re` module using pip:
- ```pip install re```
- ```python Main.py```

### Usage

Before running the script, ensure you have replaced the log file path at line 19 in the `main.py` file with the actual path to your log file. Once the script is executed, it will continuously monitor the log file for suspicious activity and take appropriate actions to block malicious IPs.

### Contributions

Contributions to this project are not currently accepted.

Contact:
    Email: kovvurisai750@gmail.com
    WhatsApp: +91 9550763666
