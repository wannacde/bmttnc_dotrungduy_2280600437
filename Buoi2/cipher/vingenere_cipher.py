class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def encrypt(self, text):
        return self._transform(text, encrypt=True)

    def decrypt(self, text):
        return self._transform(text, encrypt=False)

    def _transform(self, text, encrypt):
        key = self.key
        result = []
        key_index = 0

        for char in text.upper():
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord('A')
                new_char = chr((ord(char) - ord('A') + (shift if encrypt else -shift)) % 26 + ord('A'))
                result.append(new_char)
                key_index += 1
            else:
                result.append(char)

        return ''.join(result)
