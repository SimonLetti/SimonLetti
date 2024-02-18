import socket
import threading
import queue

def port_scanner(host, port, result_queue):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open on {host}")
        sock.close()
    except socket.error:
        pass

def worker(host, queue, result_queue):
    while not queue.empty():
        port = queue.get()
        port_scanner(host, port, result.queue)
        queue.task_done()

def main():
    target = input("Enter the host to be scanned: ")
    port_queue = queue.Queue()
    result_queue = queue.Queue()
    threads = []

    
    for port in range(1, 1025):
        port_queue.put(port)

    for _ in range(10):
        thread = threading.Thread(target=worker, args=(target, port_queue, result_queue))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    while not result_queue.empty():
        print(result_queue.get())

if __name__ == "__main__":
    main()
