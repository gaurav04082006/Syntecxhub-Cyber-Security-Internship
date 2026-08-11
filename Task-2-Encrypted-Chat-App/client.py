import socket
import threading

from crypto_utils import encrypt_message, decrypt_message


HOST = "127.0.0.1"
PORT = 5555


def receive_messages(client):
    buffer = ""

    while True:
        try:
            data = client.recv(4096)

            if not data:
                print("\n[DISCONNECTED] Server connection closed.")
                break

            buffer += data.decode("utf-8")

            while "\n" in buffer:
                encrypted_message, buffer = buffer.split("\n", 1)

                if not encrypted_message:
                    continue

                try:
                    message = decrypt_message(encrypted_message)

                    print(f"\n{message}")
                    print("You: ", end="", flush=True)

                except Exception:
                    print("\n[ERROR] Could not decrypt message.")

        except Exception:
            print("\n[ERROR] Connection lost.")
            break


def start_client():
    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    try:
        client.connect((HOST, PORT))

        print("=" * 50)
        print("          ENCRYPTED CHAT CLIENT")
        print("=" * 50)

        username = input("Enter your name: ").strip()

        if not username:
            username = "Anonymous"

        print("\n[CONNECTED] Connected to encrypted chat server.")
        print("Type /exit to leave the chat.\n")

        receive_thread = threading.Thread(
            target=receive_messages,
            args=(client,),
            daemon=True
        )

        receive_thread.start()

        while True:
            message = input("You: ")

            if message.lower() == "/exit":
                print("[DISCONNECTED] You left the chat.")
                break

            if not message.strip():
                continue

            full_message = f"{username}: {message}"

            encrypted_message = encrypt_message(full_message)

            client.sendall(
                (encrypted_message + "\n").encode("utf-8")
            )

    except ConnectionRefusedError:
        print("[ERROR] Server is not running.")

    except KeyboardInterrupt:
        print("\n[DISCONNECTED]")

    finally:
        client.close()


if __name__ == "__main__":
    start_client()