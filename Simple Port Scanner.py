import socket

def port_scanner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open on {host}")
        sock.close()
    except socket.error:
        print("Couldn't connect to server")
        return

def main():
    target = input("Enter the host to be scanned: ")
    for port in range(1, 1025):
        port_scanner(target, port)

if __name__ == "__main__":
    main()
