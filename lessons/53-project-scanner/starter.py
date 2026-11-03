# Your turn: count the open ports
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
    # TODO: set open_count to 0 before the loop
    for port, name in PORTS.items():
        if is_open(host, port):
            print(f"Port {port} is open ({name})")
            # TODO: add 1 to open_count
        else:
            print(f"Port {port} is closed ({name})")
    # TODO: after the loop, print how many ports are open
    # (like "2 of 7 ports are open")


def main():
    host = input("Host to scan: ").strip().lower()
    scan(host)


if __name__ == "__main__":
    main()
