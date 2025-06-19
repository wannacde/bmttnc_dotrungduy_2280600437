from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_data = ''
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            for i in range(3):
                binary_data += format(pixel[i], '08b')[-1]

    # Tách từng 8 bit một để tạo ký tự
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ''
    for c in chars:
        if c == '11111110':  # đánh dấu kết thúc
            break
        message += chr(int(c, 2))
    return message

if __name__ == '__main__':
    path = input("📁 Nhập đường dẫn ảnh cần giải mã (ví dụ: encoded_image.png): ")
    secret = decode_image(path)
    print("🔍 Thông điệp đã giấu:", secret)
