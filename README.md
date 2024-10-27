# port-scanner

This script is designed to check an IP address or URL, retrieve detailed information about it using the Shodan InternetDB API, and display it in a user-friendly format. Below is a breakdown of the script's features:

### Features:

1. **IP Address Retrieval**:
   - The script starts by displaying a custom banner using ASCII art, enhancing user interaction.
   - It fetches and displays your public IP address by making a request to `ipinfo.io`.

2. **User Input**:
   - The user is prompted to enter an IP address or a URL.
   - The script checks if the entered value is a valid IP address. If not, it attempts to resolve the hostname (URL) into an IP address using Python's `socket` module.

3. **Shodan InternetDB API Integration**:
   - Once a valid IP address is obtained, the script queries the [Shodan InternetDB API](https://internetdb.shodan.io/) to gather information about that IP.
   - The data returned includes details like:
     - **CPES** (Common Platform Enumeration): Information about identified platforms and software.
     - **Hostnames**: Associated domain names for the IP address.
     - **IP Address**: Confirms the IP address.
     - **Open Ports**: Lists the open ports found for the IP.
     - **Tags**: Labels or identifiers Shodan has associated with the IP.
     - **Vulnerabilities**: Known vulnerabilities affecting the IP.

4. **Error Handling**:
   - If the user provides an invalid input (either a bad IP or an unresolvable URL), the script displays an error message and exits gracefully.
   - If no information is available for the IP in the Shodan database, it prints "IP Down".

5. **Formatted Output**:
   - The data retrieved from Shodan is printed in a clean, readable format.
   - Empty lists or missing information are handled, ensuring the output is well-structured, even if some fields are unavailable.

### Key Modules Used:
- `os`: Used for clearing the terminal screen depending on the operating system.
- `requests`: Used to make HTTP requests to external APIs (ipinfo.io and Shodan).
- `json`: Used to parse the JSON responses from the API calls.
- `socket`: Used to validate and resolve IP addresses and hostnames.

### Use Cases:
- **Network Security**: It can be used to perform lightweight reconnaissance by checking if a given IP address has open ports, associated vulnerabilities, or specific software platforms.
- **Troubleshooting**: Helps in diagnosing whether an IP or domain is reachable and if there are any potential vulnerabilities.

This script is highly useful for users wanting quick access to basic network information about any IP address or URL without needing more advanced tools.

## Requirements
- Python 3.x
- `requests` module

## Installation

1. Clone or download this repository to your local machine.
2. Install the required Python package by running:
   ```bash
   pip install requests
   
   ```

## Usage


1. Run the script:
   ```bash
   python scanner.py
   ```

2. When prompted, enter the ip or URL.

3. The script will scan ports and output them in terminal.



