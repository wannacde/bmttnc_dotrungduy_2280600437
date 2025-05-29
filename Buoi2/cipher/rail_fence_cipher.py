class RailFenceCipher:
    def __init__(self, rails):
        self.rails = rails

    def encrypt(self, text):
        fence = [[] for _ in range(self.rails)]
        index = 0
        direction = 1

        for char in text:
            fence[index].append(char)
            index += direction
            if index == 0 or index == self.rails - 1:
                direction *= -1

        return ''.join(''.join(row) for row in fence)

    def decrypt(self, text):
        # Create a fence to hold the characters
        fence = [[''] * len(text) for _ in range(self.rails)]
        index = 0
        direction = 1
        pattern = [0] * len(text)

        # Create the pattern for the zigzag
        for i in range(len(text)):
            pattern[i] = index
            index += direction
            if index == 0 or index == self.rails - 1:
                direction *= -1

        # Fill the fence with placeholders from the ciphertext
        char_index = 0
        for rail in range(self.rails):
            for i in range(len(text)):
                if pattern[i] == rail:
                    fence[rail][i] = text[char_index]
                    char_index += 1

        # Read the fence in zigzag order to reconstruct the plaintext
        result = []
        index = 0
        direction = 1
        for i in range(len(text)):
            result.append(fence[index][i])
            index += direction
            if index == 0 or index == self.rails - 1:
                direction *= -1

        return ''.join(result)


