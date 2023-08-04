# Offensive-Python-HTTPReverseShell

## Description

This repository contains a Python script that demonstrates a reverse shell using the HTTP protocol. The script is designed to show the potential risks of insecure configurations but should never be used for malicious purposes. It serves as an educational resource to understand the importance of securing network configurations.

## Reason for HTTP

The HTTP protocol is often allowed on outbound firewall rules because it is used for web surfing. Additionally, a significant amount of HTTP traffic is present on most networks, making it harder to monitor and increasing the chances of evading security measures.

## Features

- Initiates a reverse HTTP session back to the attacker's server using the GET method.
- Accepts commands from the attacker's server through raw input and sends them back to the target machine.
- Executes the received command on the target machine using a subprocess (cmd.exe subprocess).
- Posts the result of the command execution back to the attacker's server using the POST method.
- Implements a 3-second sleep to ensure continuity during the command execution process.
- Repeats the entire process in an infinite loop using the `while True:` loop.

## Prerequisites

Before running the script, make sure you have Python installed on both the attacker (server) and target (client) machines.

## Usage

1. Set up the attacker machine as an HTTP server to receive the reverse shell connections.
2. Run the script on the attacker machine.
3. Set up the target machine as an HTTP client to connect back to the attacker.
4. Run the script on the target machine.

**Attention: Never use this script for malicious purposes or without proper authorization. Unauthorized access to computer systems is illegal and unethical. Only use this script on systems you have permission to access.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This script is provided for educational purposes only. The author and contributors are not responsible for any misuse or illegal activities performed with this code.

## Author

- Name: Brian Baraka Kasamba
- Date: 13/04/2022

