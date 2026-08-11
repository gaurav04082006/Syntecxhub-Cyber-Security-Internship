# TCP Port Scanner

## 📌 Project Overview

This project is a Multithreaded TCP Port Scanner developed using Python as part of the Syntecxhub Cyber Security Internship.

The scanner checks whether TCP ports on a target host are open or closed. It supports custom port ranges, multithreading for faster scanning, exception handling, and saves scan results to a text file.

---

## 🚀 Features

- Scan any Host/IP Address
- Scan a custom range of TCP ports
- Multithreaded scanning for improved performance
- Detect open and closed ports
- Exception handling for invalid hosts and timeouts
- Saves results to `scan_results.txt`
- Displays total open ports and scan time

---

## 🛠 Technologies Used

- Python 3
- Socket Programming
- Threading
- Time Module
- Datetime Module

---

## 📂 Project Structure

```
Syntecxhub_Port_Scanner/
│
├── port_scanner.py
├── scan_results.txt
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/gaurav04082006/Syntecxhub_Port_Scanner.git
```

Go to the project folder:

```bash
cd Syntecxhub_Port_Scanner
```

Run the project:

```bash
python port_scanner.py
```

---

## 💻 Sample Output

```
==================================================
        TCP PORT SCANNER
==================================================

Enter Host/IP: scanme.nmap.org
Target IP: 45.33.32.156

Open Ports Found:
Port 22
Port 80

Total Open Ports : 2
Scan Time : 0.25 Seconds
```

---

## 🎯 Learning Outcomes

- Socket Programming
- TCP Port Scanning
- Multithreading in Python
- Exception Handling
- File Handling
- Basic Cyber Security Concepts

---

## 📜 Internship

Developed for the **Syntecxhub Cyber Security Internship**.

---

## 👨‍💻 Author

**Gaurav Singh**

GitHub: https://github.com/gaurav04082006
