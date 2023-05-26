class Caesar:
    """Implements a Caesar cipher with customizable shift."""
     
    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, shift: int = 13):
        """Initializes Caesar with a provided shift or default shift 13."""
        if not abs(shift) < len(self.ALPHABET) + 1:
            raise ValueError("Invalid shift.")
        self.shift = shift

    def _encrypt_decrypt(self, message: str, encrypt: bool = True) -> str:
        """Encrypts or decrypts a message depending on the 'encrypt' parameter."""
        cleaned_message = self._clean_message(message)
        cipher = []
        for letter in cleaned_message:
            index = self.ALPHABET.index(letter)
            if encrypt:
                new_index = (index + self.shift) % len(self.ALPHABET)
            else:
                new_index = (index - self.shift) % len(self.ALPHABET)
            cipher.append(self.ALPHABET[new_index])
        return ''.join(cipher)
    
    def _clean_message(self, message: str) -> str:
        """Cleans a message by converting to lower case and removing non-alphabet characters."""
        return ''.join(char for char in message.lower() if char in self.ALPHABET)
    
    def encrypt(self, message: str) -> str:
        """Encrypts a message."""
        return self._encrypt_decrypt(message, encrypt=True)
    
    def decrypt(self, cipher: str) -> str:
        """Decrypts a cipher."""
        return self._encrypt_decrypt(cipher, encrypt=False)

if __name__ == "__main__":
    csr = Caesar(-13)
    message = "attackatdawn"
    print(f"message: {message}")
    print(f"cipher: {csr.encrypt(message)}")
    print(f"decrypted: {csr.decrypt(csr.encrypt(message))}")

    csr = Caesar(7)
    message = "the Dog ate MY HOMEWORK!"
    print(f"message: {message}")
    print(f"cleaned: {csr._clean_message(message)}")
    print(f"cipher: {csr.encrypt(message)}")
    print(f"decrypted: {csr.decrypt(csr.encrypt(message))}")
