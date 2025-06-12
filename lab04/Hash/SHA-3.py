import hashlib

def calculate_sha3_hash(data):
    sha3_hash = hashlib.sha3_256()
    sha3_hash.update(data.encode('utf-8'))  # Chuyển đổi dữ liệu thành bytes
    return sha3_hash.hexdigest()  # Trả về giá trị hex của chuỗi hash

data_to_hash = input("Nhập dữ liệu để hash bằng SHA-3: ")
hash_value = calculate_sha3_hash(data_to_hash)
print("Giá trị hash SHA-3:", hash_value)
