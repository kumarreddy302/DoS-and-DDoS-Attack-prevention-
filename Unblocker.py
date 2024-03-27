import subprocess

def unblock_ip():
    try:
        # Remove the previously added rule named "BlockIP"
        subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule', 'name="BlockIP"'], check=True)
        print('Blocked rule has been removed.')
    except Exception as e:
        print(f'Error: {e}')

# Run the function to unblock the IP
unblock_ip()