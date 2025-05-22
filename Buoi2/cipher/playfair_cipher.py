import string

class PlayfairCipher:
    def __init__(self, key):
        self.key = key.upper()
        self.matrix = self._generate_matrix()

    def _generate_matrix(self):
        alphabet = string.ascii_uppercase.replace('J', '')  # Playfair loại bỏ J
        matrix = []
        used = set()
        for char in self.key + alphabet:
            if char not in used:
                matrix.append(char)
                used.add(char)
        return [matrix[i * 5:(i + 1) * 5] for i in range(5)]

    def encrypt(self, text):
        return self._transform(text, encrypt=True)

    def decrypt(self, text):
        return self._transform(text, encrypt=False)

    def _transform(self, text, encrypt):
        text = text.upper().replace('J', 'I')  # Playfair thay J bằng I
        pairs = [text[i:i + 2] for i in range(0, len(text), 2)]
        result = []

        for pair in pairs:
            row1, col1 = divmod(self.matrix.index(pair[0]), 5)
            row2, col2 = divmod(self.matrix.index(pair[1]), 5)
            
            if row1 == row2:  # Cùng hàng
                col1 = (col1 + (1 if encrypt else -1)) % 5
                col2 = (col2 + (1 if encrypt else -1)) % 5
            elif col1 == col2:  # Cùng cột
                row1 = (row1 + (1 if encrypt else -1)) % 5
                row2 = (row2 + (1 if encrypt else -1)) % 5
            else:  # Hình chữ nhật
                col1, col2 = col2, col1

            result.append(self.matrix[row1][col1] + self.matrix[row2][col2])
        
        return ''.join(result)
