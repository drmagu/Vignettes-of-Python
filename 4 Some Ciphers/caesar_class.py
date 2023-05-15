class Caesar:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    def __init__(self, shift=13):
        self.shift = shift
        # check shift
        if not abs(shift) < len(self.alphabet) + 1:
            print(f"invalid shift parameter") 
            exit()

    def _crypt(self, message: str, type: str='e') -> str:
        cipher = []
        message = self.clean(message)
        for letter in message:
            index = self.alphabet.index(letter)
            if type == 'e':
                new_index = (index + self.shift) % len(self.alphabet)
            elif type == 'd':
                new_index = (index - self.shift) % len(self.alphabet)
            cipher.append(self.alphabet[new_index])
        return ''.join(cipher)
    
    def clean(self, message):
        message = message.lower() 
        message_list = list(message)
        for letter in message:
            if not letter in self.alphabet:
                message_list.remove(letter)
        return ''.join(message_list)
    
    def encrypt(self, message):
        return self._crypt(message)
    
    def decrypt(self, cipher):
        return self._crypt(cipher, 'd')

if __name__ == "__main__":
    ## some tests
    csr = Caesar(-13)
    message = "attackatdawn"
    print(f"message: {message}")
    print(f"cipher: {csr.encrypt(message)}")
    print(f"decrypted: {csr.decrypt(csr.encrypt(message))}")
    print()

    csr = Caesar(7)
    message = "the Dog ate MY HOMEWORK!"
    print(f"message: {message}")
    print(f"cleaned: {csr.clean(message)}")
    print(f"cipher: {csr.encrypt(message)}")
    print(f"decrypted: {csr.decrypt(csr.encrypt(message))}")
    print()


