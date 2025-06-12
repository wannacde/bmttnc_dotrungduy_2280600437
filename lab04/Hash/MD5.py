import hashlib

def calculate_md5_hash(data):
    md5_hash = hashlib.md5()
    md5_hash.update(data.encode('utf-8'))  # Chuyển đổi dữ liệu thành bytes
    return md5_hash.hexdigest()  # Trả về giá trị hex của chuỗi hash

data_to_hash = input("Nhập dữ liệu để hash bằng MD5: ")
hash_value = calculate_md5_hash(data_to_hash)
print("Giá trị hash MD5:", hash_value)
