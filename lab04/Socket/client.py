import socket

# Khởi tạo socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối đến server
server_address = ('localhost', 65432)  # Địa chỉ server
client_socket.connect(server_address)

try:
    while True:
        # Nhập dữ liệu từ người dùng
        data_to_send = input("Nhập dữ liệu bạn muốn gửi đến server (nhập 'exit' để thoát): ")

        # Gửi dữ liệu đến server
        client_socket.sendall(data_to_send.encode('utf-8'))

        # Kiểm tra xem người dùng có nhập "exit" không
        if data_to_send.lower() == 'exit':
            print("Kết thúc kết nối.")
            break  # Thoát khỏi vòng lặp

        # Nhận dữ liệu từ server
        data_received = client_socket.recv(1024).decode('utf-8')
        print("Dữ liệu nhận được từ server:", data_received)

finally:
    # Đóng socket
    client_socket.close()
