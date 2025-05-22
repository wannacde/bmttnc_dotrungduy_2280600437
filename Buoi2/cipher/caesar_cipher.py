from .alphabet import ALPHABET  


class CaesarCipher:
    def __init__(self, shift):
        self.shift = shift

    def encrypt(self, text):
        return self._transform(text, self.shift)

    def decrypt(self, text):
        return self._transform(text, -self.shift)

    def _transform(self, text, shift):
        result = ""
        for char in text:
            if char in ALPHABET:
                index = ALPHABET.index(char)
                new_index = (index + shift) % len(ALPHABET)
                result += ALPHABET[new_index]
            else:
                result += char  # Giữ nguyên ký tự không thuộc ALPHABET
        return result
