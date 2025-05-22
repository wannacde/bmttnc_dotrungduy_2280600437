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
        fence = [[] for _ in range(self.rails)]
        index = 0
        direction = 1
        pattern = [index]

        for _ in text[1:]:
            index += direction
            pattern.append(index)
            if index == 0 or index == self.rails - 1:
                direction *= -1

        sorted_indices = sorted(range(len(text)), key=lambda i: pattern[i])
        for i, char in zip(sorted_indices, text):
            fence[pattern[i]].append(char)

        return ''.join(''.join(row) for row in fence)
