import socket
import ssl
import threading


HOST = 'localhost'
PORT = 12345

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            if data:
                print("📥 Từ server:", data)
        except:
            break

def main():
    context = ssl._create_unverified_context()

    with socket.create_connection((HOST, PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=HOST) as ssock:
            print("🔗 Đã kết nối tới server.")
            threading.Thread(target=receive_messages, args=(ssock,), daemon=True).start()

            while True:
                msg = input("💬 Nhập tin nhắn: ")
                if msg.lower() == 'exit':
                    break
                ssock.sendall(msg.encode('utf-8'))

if __name__ == '__main__':
    main()
