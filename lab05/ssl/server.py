import socket
import ssl
import threading

HOST = 'localhost'
PORT = 12345
clients = []

def handle_client(client_socket):
    clients.append(client_socket)
    print("✅ Đã kết nối với:", client_socket.getpeername())

    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("📨 Nhận:", data.decode('utf-8'))

            # Gửi lại đến tất cả client khác
            for client in clients:
                if client != client_socket:
                    try:
                        client.send(data)
                    except:
                        clients.remove(client)
    finally:
        client_socket.close()

def main():
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='certificates/server-cert.crt',
                            keyfile='certificates/server-key.key')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"🔐 Server SSL đang chạy tại {HOST}:{PORT}")

        with context.wrap_socket(server, server_side=True) as ssock:
            while True:
                client_socket, addr = ssock.accept()
                thread = threading.Thread(target=handle_client, args=(client_socket,))
                thread.start()

if __name__ == '__main__':
    main()
