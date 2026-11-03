# Practice 3: list only the open ports
# Port scanner: for your own computer only.
# Only scan what you own or have written permission to test.
# Scanning without permission can be illegal.
import socket

PORTS = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    8000: "HTTP dev server",
    8080: "HTTP alternate",
}


def is_open(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex(("127.0.0.1", port)) == 0


open_ports = [port for port in PORTS if is_open(port)]
if open_ports:
    for port in open_ports:
        print(f"{port} ({PORTS[port]})")
else:
    print("No open ports found")
