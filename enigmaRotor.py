

class EnigmaRotor:
    def __init__(self, permutation):
        self.__forward_permutation = permutation
        self.__backward_permutation = self.__inverse_permutation(permutation)
        self.offset = 0

    def get_permutation(self):
        return self.__forward_permutation

    def get_offset(self):
        return self.offset

    def advance(self):
        carry = False
        self.offset += 1
        if self.offset == 26:
            self.offset = 0
            carry = True
        return carry

    def forward_encryption(self, letter):
        return self.__apply_permutation(self.__forward_permutation, letter)


    def backward_encryption(self, letter):
        return self.__apply_permutation(self.__backward_permutation, letter)

    def __apply_permutation(self, permutation, letter):
        index = ord(letter) - ord('A')
        index = (index + self.offset) % 26
        letter = permutation[index]
        index = ord(letter) - ord('A')
        index = (index - self.offset) % 26
        letter = chr(ord('A') + index)
        return letter

    def __letter_to_index(self, letter):
        return ord(letter) - ord('A')

    def __index_to_letter(self, index):
        return chr(ord('A') + index)

    def __inverse_permutation(self, permutation):
        newpermutation = ['A'] * 26
        for index, letter in enumerate(permutation):
            newpermutation[self.__letter_to_index(letter)] = chr(ord('A') + index)
        return ''.join(newpermutation)




if __name__ == '__main__':
    print(14 % 10)
    print(-4 % 10)
