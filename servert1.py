# iterated_server_task3.py
import socket

users = {}  # store username: password


def start_server():
    host = "127.0.0.1"
    port = 9000

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(3)

    print("[*] Server started.")

    while True:
        print(f"Listening on {host}:{port}")
        conn, addr = server_socket.accept()
        print(f"[+] Connected by {addr}")

        conn.send("Welcome! Would you like to (1) Register or (2) Login?".encode())

        choice = conn.recv(1024).decode()

        if choice == "1":
            conn.send("Username:".encode())
            username = conn.recv(1024).decode()

            conn.send("Password:".encode())
            password = conn.recv(1024).decode()

            conn.send("Retype password:".encode())
            confirm = conn.recv(1024).decode()

            if password == confirm:
                users[username] = password
                conn.send(f"User '{username}' registered successfully!".encode())
            else:
                conn.send("Passwords do not match.".encode())

        elif choice == "2":
            conn.send("Username:".encode())
            username = conn.recv(1024).decode()

            if username not in users:
                conn.send("User unknown. Try again.".encode())
            else:
                conn.send("Password:".encode())
                password = conn.recv(1024).decode()

                if users[username] == password:
                    conn.send(f"Welcome {username}!".encode())
                else:
                    conn.send("Password incorrect.".encode())

        conn.close()
        print("[-] Client disconnected.")


if __name__ == "__main__":
    start_server()
