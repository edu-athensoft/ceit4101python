"""
socket
http
"""

import socket


def fetch_homepage(url):
    print(f"fetching... {url}")

    # 分解URL获取主机名
    host = url.split("//")[-1]  # 去除"http://"或"https://"
    path = "/"

    # 创建一个socket对象
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(s)

    try:
        # 连接到主机
        print("connecting...")
        s.connect((host, 80))
        print("connected")

        # 发送GET请求
        request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
        s.send(request.encode())
        print("request sent.")

        # 接收响应数据
        response = b""
        while True:
            part = s.recv(1024)
            if part:
                response += part
            else:
                break

        # 关闭socket
        s.close()
    except Exception as e:
        print(e)
    finally:
        if s:
            s.close()

    # 解码响应数据
    return response.decode(errors='ignore')


# 调用函数读取网站首页
url = "https://www.athensoft.com"
homepage_content = fetch_homepage(url)
print(homepage_content)

