import socket
import random
import threading

def handle_client(conn, addr, server_name, server_number):
    print(f"Connected by {addr}")
    data = conn.recv(1024).decode()
    if not data:
        conn.close()
        return

    try:
        client_name, client_num_str = data.split(",")
        client_num = int(client_num_str.strip())
    except ValueError:
        print("Invalid message format. Closing connection.")
        conn.close()
        return

    if client_num < 1 or client_num > 100:
        print("Received number outside 1–100. Closing connection.")
        conn.close()
        return

    total = client_num + server_number

    print("\n--- Server Side ---")
    print(f"Client Name: {client_name}")
    print(f"Server Name: {server_name}")
    print(f"Client Integer: {client_num}")
    print(f"Server Integer: {server_number}")
    print(f"Sum: {total}")

    reply = f"{server_name},{server_number}"
    conn.send(reply.encode())
    conn.close()

def main():
    host = "0.0.0.0"   # Listen on all interfaces
    port = 6111

    server_name = "Server of STK"
    server_number = random.randint(1, 100)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server started on port {port}. Waiting for connections...")

    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, server_name, server_number))
        thread.start()

if __name__ == "__main__":
    main()
