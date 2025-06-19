
import base64

def decrypt_and_save():
    try:
        with open("data.txt", "rb") as f:
            encoded_data = f.read()

        decoded_data = base64.b64decode(encoded_data).decode('utf-8')

        with open("data.txt", "w", encoding="utf-8") as f:
            f.write(decoded_data)

        print("✅ Đã giải mã và lưu lại vào data.txt")
    except Exception as e:
        print("❌ Đã xảy ra lỗi khi giải mã:", e)

if __name__ == '__main__':
    decrypt_and_save()
