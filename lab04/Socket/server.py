import socket

# Khởi tạo socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Thiết lập địa chỉ server
server_address = ('localhost', 65432)
server_socket.bind(server_address)

# Lắng nghe kết nối
server_socket.listen()

print("Đang chờ kết nối từ client...")
while True:
    connection, client_address = server_socket.accept()
    try:
        print("Kết nối từ:", client_address)

        while True:
            # Nhận dữ liệu từ client
            data_received = connection.recv(1024).decode('utf-8')
            if not data_received:  # Kiểm tra nếu không còn dữ liệu
                print("Client đã ngắt kết nối.")
                break

            print("Dữ liệu nhận được từ client:", data_received)

            # Gửi lại dữ liệu cho client
            connection.sendall(data_received.encode('utf-8'))

    finally:
        # Đóng kết nối
        connection.close()
