import os
import base64
import hashlib

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


# Pre-shared secret used by all chat clients.
# Later we can move this to an environment variable.
SECRET_KEY = os.getenv(
    "CHAT_SECRET_KEY",
    "EncryptedChatApp-2026"
).encode("utf-8")

# Convert our secret into a 256-bit AES key.
AES_KEY = hashlib.sha256(SECRET_KEY).digest()


def encrypt_message(message):
    aesgcm = AESGCM(AES_KEY)

    # AES-GCM recommends a fresh 12-byte nonce for every encryption.
    nonce = os.urandom(12)

    encrypted_data = aesgcm.encrypt(
        nonce,
        message.encode("utf-8"),
        None
    )

    # Send nonce + ciphertext together.
    encrypted_message = nonce + encrypted_data

    return base64.b64encode(encrypted_message).decode("utf-8")


def decrypt_message(encrypted_message):
    aesgcm = AESGCM(AES_KEY)

    encrypted_data = base64.b64decode(encrypted_message)

    nonce = encrypted_data[:12]
    ciphertext = encrypted_data[12:]

    decrypted_data = aesgcm.decrypt(
        nonce,
        ciphertext,
        None
    )

    return decrypted_data.decode("utf-8")

