import sys
from PIL import Image

def encode_image(image_path, message):
    img = Image.open(image_path)
    width, height = img.size
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '11111110'  # đánh dấu kết thúc

    data_index = 0
    for row in range(height):
        for col in range(width):
            if data_index >= len(binary_message):
                break
            pixel = list(img.getpixel((col, row)))  # R, G, B
            for i in range(3):  # duyệt 3 kênh màu
                if data_index < len(binary_message):
                    pixel[i] = int(format(pixel[i], '08b')[:-1] + binary_message[data_index], 2)
                    data_index += 1
            img.putpixel((col, row), tuple(pixel))
        if data_index >= len(binary_message):
            break

    output_path = 'encoded_image.png'
    img.save(output_path)
    print("✅ Đã giấu thông điệp vào ảnh, lưu tại:", output_path)

def main():
    if len(sys.argv) != 3:
        print("📌 Dùng: python encrypt.py <tên_ảnh> <thông_điệp>")
        return
    image_path = sys.argv[1]
    message = sys.argv[2]
    encode_image(image_path, message)

if __name__ == '__main__':
    main()
