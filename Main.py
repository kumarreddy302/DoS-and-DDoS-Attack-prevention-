import re
from collections import Counter
import time
import subprocess

blocked_ips = set()

def block_ip(ip):
    if ip not in blocked_ips:
        try:
            # Add a new inbound rule to block traffic from the specified IP
            subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name="BlockIP"', 'dir=in', f'protocol=any', f'action=block', f'remoteip={ip}'], check=True)
            print(f'Incoming connections from {ip} are now blocked.')
            blocked_ips.add(ip)
        except Exception as e:
            print(f'Error: {e}')


log_file_path = 'C:/xampp/apache/logs/access.log'

threshold = 100

ip_pattern = r'\d+\.\d+\.\d+\.\d+'

while True:

    ip_counter = Counter()

    with open(log_file_path, 'r') as log_file:
        for line in log_file:
           
            match = re.search(ip_pattern, line)
            if match:
                ip_address = match.group()
                ip_counter[ip_address] += 1

    suspicious_ips = [ip for ip, count in ip_counter.items() if count > threshold]

    if suspicious_ips:
        print("Potential DDOS attack detected. Suspicious IP addresses:")
        for ip in suspicious_ips:
            if ip not in blocked_ips:
                print(ip)
                block_ip(ip)

    else:
        print("No suspicious activity detected.")

    time.sleep(5)
