# simple_client_task3.py
import socket

def start_client():
    host = input("Enter server IP Address: ")
    port = int(input("Enter server Port: "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print("[Server]:", client_socket.recv(1024).decode())

    choice = input("[Client]: ")
    client_socket.send(choice.encode())

    while True:
        response = client_socket.recv(1024).decode()
        print("[Server]:", response)

        if "successfully" in response or "Welcome" in response or "incorrect" in response or "unknown" in response:
            break

        message = input("[Client]: ")
        client_socket.send(message.encode())

    client_socket.close()


if __name__ == "__main__":
    start_client()
