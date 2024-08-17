import socket
import threading
import argparse

# Banner corregido
BANNER = r"""
 █████╗ ███╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗███████╗██████╗  █████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗████╗  ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔════╝██╔══██╗██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
███████║██╔██╗ ██║██║  ██║██████╔╝██║   ██║██╔████╔██║█████╗  ██║  ██║███████║    ███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██╔══██║██║╚██╗██║██║  ██║██╔══██╗██║   ██║██║╚██╔╝██║██╔══╝  ██║  ██║██╔══██║    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██║  ██║██║ ╚████║██████╔╝██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗██████╔╝██║  ██║    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                                                                              
"""

# Función para escanear un solo puerto
def scan_single_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        print(f"Puerto {port} está abierto ({get_service_name(port)})")
    except socket.error as err:
        print(f"Puerto {port} está cerrado. Error: {err}")
    finally:
        s.close()

# Función para escanear un rango de puertos
def scan_multiple_ports(host, port_range):
    open_ports = []
    for port in port_range:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((host, port))
            open_ports.append(port)
        except socket.error:
            pass
        finally:
            s.close()
    return open_ports

# Función para escanear un rango de puertos utilizando hilos
def scan_with_threads(host, port_range):
    open_ports = []
    threads = []

    def scan_port(host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((host, port))
            open_ports.append(port)
        except socket.error:
            pass
        finally:
            s.close()

    for port in port_range:
        t = threading.Thread(target=scan_port, args=(host, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return open_ports

# Función para obtener el nombre del servicio asociado a un puerto
def get_service_name(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown Service"

# Función para manejar los argumentos de línea de comandos
def parse_arguments():
    parser = argparse.ArgumentParser(description="Escáner de Puertos en Python")
    parser.add_argument("host", help="La dirección IP o nombre de dominio del host a escanear")
    parser.add_argument("-p", "--ports", help="El rango de puertos a escanear, ejemplo: 1-1024", default="1-1024")
    parser.add_argument("-t", "--threads", help="Utilizar hilos para el escaneo", action="store_true")
    return parser.parse_args()

# Bloque principal para ejecutar las funciones
if __name__ == "__main__":
    print(BANNER)  # Mostrar el banner al inicio

    args = parse_arguments()  # Ahora se llama a la función después de que esté definida

    host = args.host
    port_range = range(int(args.ports.split('-')[0]), int(args.ports.split('-')[1]) + 1)

    if args.threads:
        print("\nEscaneando múltiples puertos con hilos...")
        open_ports = scan_with_threads(host, port_range)
    else:
        print("\nEscaneando múltiples puertos secuencialmente...")
        open_ports = scan_multiple_ports(host, port_range)

    if open_ports:
        print(f"Puertos abiertos en {host}:")
        for port in open_ports:
            print(f"Puerto {port} ({get_service_name(port)})")
    else:
        print("No se encontraron puertos abiertos.")