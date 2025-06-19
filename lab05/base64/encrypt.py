
import base64

def encrypt_and_save():
    user_input = input("Nhập dữ liệu cần mã hóa: ")
    encoded_data = base64.b64encode(user_input.encode('utf-8'))

    with open("data.txt", "wb") as f:
        f.write(encoded_data)

    print("✅ Đã mã hóa và lưu vào data.txt")

if __name__ == '__main__':
    encrypt_and_save()
