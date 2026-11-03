# Your turn, solved: count the open ports
# Port scanner: for your own computer only.
# Only scan what you own or have written permission to test.
# Scanning without permission can be illegal.
import socket

ALLOWED = {"127.0.0.1", "localhost"}
PORTS = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    8000: "HTTP dev server",
    8080: "HTTP alternate",
}


def is_open(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        return s.connect_ex((host, port)) == 0


def scan(host):
    if host not in ALLOWED:
        print(f"Refusing to scan {host}: localhost only.")
        print("Scanning without permission can be illegal.")
        return
    print(f"Scanning {host}...")
    open_count = 0
    for port, name in PORTS.items():
        if is_open(host, port):
            print(f"Port {port} is open ({name})")
            open_count += 1
        else:
            print(f"Port {port} is closed ({name})")
    print(f"{open_count} of {len(PORTS)} ports are open")


def main():
    host = input("Host to scan: ").strip().lower()
    scan(host)


if __name__ == "__main__":
    main()
