import socket

def main():
    host = "127.1.1.1"  # Server IP (localhost for testing)
    port = 6111         # Same as server port

    client_name = "Client of STK"

    # Take integer input
    while True:
        try:
            num = int(input("Enter an integer (1–100): "))
            if 1 <= num <= 100:
                break
            else:
                print("Number must be between 1 and 100.")
        except ValueError:
            print("Please enter a valid integer.")

    # Create TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))  # connect

    # Send data: name + integer
    message = f"{client_name},{num}"
    client_socket.send(message.encode())

    # Receive server reply
    data = client_socket.recv(1024).decode()
    server_name, server_num_str = data.split(",")
    server_num = int(server_num_str.strip())

    # Compute sum
    total = num + server_num

    # Display details
    print("\n--- Client Side ---")
    print(f"Client Name: {client_name}")
    print(f"Server Name: {server_name}")
    print(f"Client Integer: {num}")
    print(f"Server Integer: {server_num}")
    print(f"Sum: {total}")

    client_socket.close()

if __name__ == "__main__":
    main()
