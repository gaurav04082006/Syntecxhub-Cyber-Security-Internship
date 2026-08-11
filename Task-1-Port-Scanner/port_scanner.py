import socket
import threading
import time
from datetime import datetime

def scan_port(host, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    try:
        result = scanner.connect_ex((host, port))
        return result == 0

    except socket.timeout:
        print(f"[TIMEOUT] Port {port}")
        return False

    except Exception as e:
        print(f"[ERROR] Port {port}: {e}")
        return False

    finally:
        scanner.close()

def threaded_scan(host, port, open_ports, lock):
    if scan_port(host, port):
        print(f"[OPEN]   Port {port}")

        with lock:
            open_ports.append(port)
    else:
        print(f"[CLOSED] Port {port}")

print("=" * 50)
print("        TCP PORT SCANNER")
print("=" * 50)

host = input("Enter Host/IP: ")

try:
    target_ip = socket.gethostbyname(host)
    print(f"Target IP: {target_ip}")
except socket.gaierror:
    print("Invalid Host or IP Address")
    exit()

try:
    start_port = int(input("Enter Start Port: "))
    end_port = int(input("Enter End Port: "))
except ValueError:
    print("Please enter valid port numbers.")
    exit()

start_time = time.time()

open_ports = []
threads = []
lock = threading.Lock()

for port in range(start_port, end_port + 1):
    thread = threading.Thread(
        target=threaded_scan,
        args=(target_ip, port, open_ports, lock)
    )

    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

    end_time = time.time()

print("\n" + "=" * 50)

if open_ports:
    print("Open Ports Found:")
    for port in open_ports:
        print(f"Port {port}")
else:
    print("No Open Ports Found.")

print("=" * 50)

print(f"\nTotal Open Ports : {len(open_ports)}")

with open("scan_results.txt", "w") as file:

    file.write("TCP PORT SCANNER REPORT\n")
    file.write("=" * 40 + "\n")

    file.write(f"Host : {host}\n")
    file.write(f"IP : {target_ip}\n")
    file.write(f"Port Range : {start_port}-{end_port}\n\n")

    file.write("Open Ports:\n")

    if open_ports:
        for port in open_ports:
            file.write(f"{port}\n")
    else:
        file.write("No Open Ports Found\n")

    file.write("\n")
    file.write(f"Total Open Ports : {len(open_ports)}\n")
    file.write(f"Scan Time : {end_time-start_time:.2f} Seconds\n")

    print("\nResults saved in scan_results.txt")

    print(f"Scan Time        : {end_time - start_time:.2f} Seconds")