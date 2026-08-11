# 🔐 Encrypted Chat Application

A secure multi-client chat application built using Python.

The application uses TCP socket communication and AES-256-GCM
authenticated encryption to protect messages before they are
transmitted over the network.

## Features

- TCP client-server communication
- AES-256-GCM message encryption
- Random nonce for every message
- Pre-shared secret key handling
- Multiple client support using threading
- Real-time encrypted messaging
- Connection and activity logging
- Message authentication using AES-GCM

## Technologies Used

- Python
- Socket Programming
- Threading
- Cryptography Library
- AES-256-GCM
- SHA-256

## Project Structure

Encrypted-Chat-App/
├── server.py
├── client.py
├── crypto_utils.py
├── requirements.txt
├── README.md
└── .gitignore

## Installation

Install the required dependency:

pip install -r requirements.txt

## Run the Server

python server.py

## Run a Client

Open another terminal:

python client.py

Run multiple clients in separate terminals to test multi-user chat.

## Security

Messages are encrypted before transmission using AES-256-GCM.

A fresh 12-byte random nonce is generated for every encrypted
message. AES-GCM also provides authentication, allowing modified
or corrupted ciphertext to be detected.

The shared secret can be supplied using the CHAT_SECRET_KEY
environment variable.

## Example

Client 1:

Enter your name: Gaurav
You: Hello Rahul

Client 2:

Enter your name: Rahul
Gaurav: Hello Rahul

## Author

Developed by Gaurav Singh
