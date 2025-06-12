import hashlib

def calculate_blake2_hash(data):
    blake2_hash = hashlib.blake2b()  # Sử dụng BLAKE2b (có thể dùng BLAKE2s cho các input nhỏ hơn)
    blake2_hash.update(data.encode('utf-8'))  # Chuyển đổi dữ liệu thành bytes
    return blake2_hash.hexdigest()  # Trả về giá trị hex của chuỗi hash

data_to_hash = input("Nhập dữ liệu để hash bằng Blake2: ")
hash_value = calculate_blake2_hash(data_to_hash)
print("Giá trị hash Blake2:", hash_value)
