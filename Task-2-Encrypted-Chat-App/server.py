import socket
import threading
import logging

from crypto_utils import decrypt_message


HOST = "127.0.0.1"
PORT = 5555

clients = []


# Server logging
logging.basicConfig(
    filename="server.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall((message + "\n").encode("utf-8"))
            except Exception:
                remove_client(client)


def remove_client(client):
    if client in clients:
        clients.remove(client)

    try:
        client.close()
    except Exception:
        pass


def handle_client(client_socket, address):
    print(f"[CONNECTED] {address}")

    logging.info(f"Client connected: {address}")

    buffer = ""

    try:
        while True:
            data = client_socket.recv(4096)

            if not data:
                break

            buffer += data.decode("utf-8")

            while "\n" in buffer:
                encrypted_message, buffer = buffer.split("\n", 1)

                if not encrypted_message:
                    continue

                try:
                    decrypted_message = decrypt_message(encrypted_message)

                    print(f"[MESSAGE] {address}: {decrypted_message}")

                    logging.info(
                        f"Message received from {address}"
                    )

                    broadcast(
                        encrypted_message,
                        client_socket
                    )

                except Exception as error:
                    print(
                        f"[DECRYPTION ERROR] {address}: {error}"
                    )

                    logging.warning(
                        f"Invalid encrypted message from {address}"
                    )

    except ConnectionResetError:
        pass

    finally:
        print(f"[DISCONNECTED] {address}")

        logging.info(f"Client disconnected: {address}")

        remove_client(client_socket)


def start_server():
    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind((HOST, PORT))

    server.listen()

    print("=" * 50)
    print("        ENCRYPTED CHAT SERVER")
    print("=" * 50)

    print(f"[LISTENING] Server running on {HOST}:{PORT}")
    print("[WAITING] Waiting for clients...")

    logging.info(
        f"Server started on {HOST}:{PORT}"
    )

    try:
        while True:
            client_socket, address = server.accept()

            clients.append(client_socket)

            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address),
                daemon=True
            )

            thread.start()

            print(
                f"[ACTIVE CONNECTIONS] {len(clients)}"
            )

    except KeyboardInterrupt:
        print("\n[SERVER STOPPED]")

    finally:
        for client in clients.copy():
            remove_client(client)

        server.close()


if __name__ == "__main__":
    start_server()