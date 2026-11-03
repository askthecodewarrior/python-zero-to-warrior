# Practice 2: check one port on your own computer
# Only scan what you own or have written permission to test.
import socket


def is_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex(("127.0.0.1", port)) == 0


port = int(input("Port to check on this computer: "))
if is_open(port):
    print(f"Port {port} is open")
else:
    print(f"Port {port} is closed")
