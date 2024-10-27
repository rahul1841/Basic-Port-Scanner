import os
import requests
import json
import socket

# clear the screen
os.system('cls' if os.name == 'nt' else 'clear')


print('\u001b[36m' +
'''

 ██████   █████          █████      ███     ███████████      
░░██████ ░░███          ░░███      ░░░     ░█░░░███░░░█      
 ░███░███ ░███   ██████  ░███████  ████    ░   ░███  ░       
 ░███░░███░███  ███░░███ ░███░░███░░███        ░███          
 ░███ ░░██████ ░███ ░███ ░███ ░███ ░███        ░███          
 ░███ ░░██████ ░███ ░███ ░███ ░███ ░███        ░███          
 █████  ░░█████░░██████  ████████  █████       █████    ██ ██
░░░░░    ░░░░░  ░░░░░░  ░░░░░░░░  ░░░░░       ░░░░░    ░░ ░░ 

'''
)
#your ip
response = requests.get("https://ipinfo.io/ip")

# print the output of the API to the console
print('Your Ip = ' + response.text)
# prompt the user for input
user_input = input('\u001b[32m'+"Enter an IP address or a URL: ")

# check if the user input is an IP address
try:
    socket.inet_aton(user_input)
    ip_address = user_input
except socket.error:
    # if the user input is not an IP address, try to convert it to an IP address using the socket module
    try:
        ip_address = socket.gethostbyname(user_input)
    except socket.gaierror:
        # if the user input cannot be converted to an IP address, print an error message and exit
        print('\u001b[31m'+"Invalid input: please enter a valid IP address or URL")
        exit()

# build the URL for the Shodan API request
url = f"https://internetdb.shodan.io/{ip_address}"

# make the API request and parse the response JSON
response = requests.get(url)
data = json.loads(response.text)

# check if the response contains the message 'No information available'
if data.get("detail", "") == "No information available":
    print('\u001b[31m'+"IP Down")
else:
    # extract the desired information categories
    cpes = data.get("cpes", "")
    hostnames = data.get("hostnames", "")
    ip = data.get("ip", "")
    ports = data.get("ports", "")
    tags = data.get("tags", "")
    vulns = data.get("vulns", "")

    # remove the brackets from empty lists and convert non-empty lists to strings
    cpes = ", ".join(cpes) if cpes else ""
    hostnames = ", ".join(hostnames) if hostnames else ""
    ports = ", ".join(map(str, ports)) if ports else ""
    tags = ", ".join(tags) if tags else ""
    vulns = ", ".join(vulns) if vulns else ""

    # print the information categories in a readable format
    print("CPES: ", cpes)
    print("Hostnames: ", hostnames)
    print("IP Address: ", ip)
    print("Ports: ", ports)
    print("Tags: ", tags)
    print("Vulnerabilities: ", vulns)
