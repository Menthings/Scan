#coding:utf-8

import sys
import socket

try:
    adressIP = sys.argv[1]
    ports = [21, 22, 23, 24, 25, 80, 135, 443, 3306, 8080]

    adressIP = int(adressIP)
    ports = int(ports)

    for port in ports:
        client = sockets.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.05)
        code = client.connect_ex((adressIP, port))

    if code == 0:
        print("Scan : " + str(port) + "ports ouverts")
    else:
        print("Scan : " + str(port) + "ports fermés")

except ValueError:
    print("Port invalide")

except OSError:
    sys.exit()
