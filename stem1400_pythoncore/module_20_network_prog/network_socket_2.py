"""
socket
http
"""

import socket
import ssl


def fetch_homepage_ssl(url):
    host = "www.athensoft.com"
    context = ssl.create_default_context()

    with socket.create_connection((host, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
            ssock.send(request.encode())
            response = ssock.recv(4096)
            print(response.decode())


fetch_homepage_ssl("https://www.athensoft.com")

