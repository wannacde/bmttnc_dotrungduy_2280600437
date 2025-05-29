import string

class PlayfairCipher:
    def __init__(self, key):
        self.key = key.upper()
        self.matrix = self._generate_matrix()

    def _generate_matrix(self):
        alphabet = string.ascii_uppercase.replace('J', '')  # Playfair removes 'J'
        matrix = []
        used = set()
        # Add key characters first
        for char in self.key:
            if char not in used and char in alphabet:
                matrix.append(char)
                used.add(char)
        # Add remaining alphabet characters
        for char in alphabet:
            if char not in used:
                matrix.append(char)
                used.add(char)
        return [matrix[i * 5:(i + 1) * 5] for i in range(5)]

    def _format_text(self, text, for_encryption=True):
        text = text.upper().replace('J', 'I')
        # Remove non-alpha characters
        filtered = [ch for ch in text if ch.isalpha()]
        # For encryption, split into pairs and add 'X' if letters in a pair are same or odd length
        if for_encryption:
            i = 0
            pairs = []
            while i < len(filtered):
                a = filtered[i]
                b = ''
                if (i + 1) < len(filtered):
                    b = filtered[i + 1]
                if b == '':
                    pairs.append(a + 'X')
                    i += 1
                elif a == b:
                    pairs.append(a + 'X')
                    i += 1
                else:
                    pairs.append(a + b)
                    i += 2
            return pairs
        else:
            # For decryption, just split by 2 chars
            pairs = []
            i = 0
            while i < len(filtered):
                pairs.append(''.join(filtered[i:i+2]))
                i += 2
            return pairs

    def _find_position(self, char):
        for row_idx, row in enumerate(self.matrix):
            if char in row:
                return (row_idx, row.index(char))
        raise ValueError(f"Character {char} not found in matrix.")

    def _transform(self, text, encrypt):
        pairs = self._format_text(text, for_encryption=encrypt)
        result = []

        for pair in pairs:
            row1, col1 = self._find_position(pair[0])
            row2, col2 = self._find_position(pair[1])

            if row1 == row2:
                # same row: move right (encrypt) or left (decrypt)
                if encrypt:
                    col1 = (col1 + 1) % 5
                    col2 = (col2 + 1) % 5
                else:
                    col1 = (col1 - 1) % 5
                    col2 = (col2 - 1) % 5
            elif col1 == col2:
                # same column: move down (encrypt) or up (decrypt)
                if encrypt:
                    row1 = (row1 + 1) % 5
                    row2 = (row2 + 1) % 5
                else:
                    row1 = (row1 - 1) % 5
                    row2 = (row2 - 1) % 5
            else:
                # rectangle swap columns
                col1, col2 = col2, col1

            result.append(self.matrix[row1][col1] + self.matrix[row2][col2])

        return ''.join(result)

    def encrypt(self, text):
        return self._transform(text, encrypt=True)

    def decrypt(self, text):
        return self._transform(text, encrypt=False)

