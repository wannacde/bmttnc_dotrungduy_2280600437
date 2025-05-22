class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, text):
        num_cols = len(self.key)
        num_rows = (len(text) + num_cols - 1) // num_cols
        grid = [[' '] * num_cols for _ in range(num_rows)]

        for index, char in enumerate(text):
            row, col = divmod(index, num_cols)
            grid[row][col] = char

        sorted_key = sorted(enumerate(self.key), key=lambda x: x[1])
        encrypted_text = ''.join(''.join(row[col] for row in grid) for col, _ in sorted_key)
        return encrypted_text

    def decrypt(self, text):
        num_cols = len(self.key)
        num_rows = (len(text) + num_cols - 1) // num_cols
        sorted_key = sorted(enumerate(self.key), key=lambda x: x[1])
        grid = [[' '] * num_cols for _ in range(num_rows)]

        index = 0
        for col, _ in sorted_key:
            for row in range(num_rows):
                if index < len(text):
                    grid[row][col] = text[index]
                    index += 1

        return ''.join(''.join(row) for row in grid)
