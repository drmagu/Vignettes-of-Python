class Vigenere:
    """
    A class used to implement the Vigenère cipher.

    Attributes
    ----------
    VALID_SYMBOLS : str
        A string of valid symbols that can be used in the encryption and decryption process.
    SPACE_SUBSTITUTE : str
        A character used to substitute spaces in the cipher text.
    NEWLINE_SUBSTITUTE : str
        A character used to substitute newline characters in the cipher text.
    key : str
        The key used for encryption and decryption.
    key_len : int
        The length of the key.

    Methods
    -------
    _clean_message(message: str) -> str
        Removes invalid characters from the message.
    _split(text: str) -> list
        Splits text into chunks of size equal to the key length.
    _encrypt_chunk(chunk: str) -> str
        Encrypts a chunk of the message.
    encrypt(message: str) -> str
        Encrypts the entire message.
    _decrypt_chunk(chunk: str) -> str
        Decrypts a chunk of the cipher.
    decrypt(cipher: str) -> str
        Decrypts the entire cipher.
    """


    VALID_SYMBOLS = (
        " abcdefghijklmnopqrstuvwxyz" +
        "\n" +
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ" +
        ".,?!1234567890" + "\"'" + "-:;–"
    )
    SPACE_SUBSTITUTE = '~'
    NEWLINE_SUBSTITUTE = '`'

    def __init__(self, key=None):
        """Initializes Vigenere with a provided key or default key 'poes'."""
        if key is None:
            key='poes'
        if len(key) == 0 or not all(symbol in self.VALID_SYMBOLS for symbol in key):
            raise ValueError("Invalid key. Key must contain only valid symbols and cannot be empty.")
        self.key = key
        self.key_len = len(key)

    def _clean_message(self, message: str) -> str:
        """Removes invalid characters from the message."""
        return ''.join(filter(lambda char: char in self.VALID_SYMBOLS, message))

    def _split(self, text: str) -> list:
        """Splits text into chunks of size equal to the key length."""
        return [
            text[i:i + self.key_len]
            for i in range(0, len(text), self.key_len)
        ]

    def _encrypt_chunk(self, chunk: str) -> str:
        """Encrypts a chunk of the message."""
        cipher_chunk = ""
        for i, symbol in enumerate(chunk):
            new_index = (self.VALID_SYMBOLS.index(symbol) +
                         self.VALID_SYMBOLS.index(self.key[i])) % len(self.VALID_SYMBOLS)
            if self.VALID_SYMBOLS[new_index] == ' ':
                cipher_chunk += self.SPACE_SUBSTITUTE
            elif self.VALID_SYMBOLS[new_index] == '\n':
                cipher_chunk += self.NEWLINE_SUBSTITUTE
            else:
                cipher_chunk += self.VALID_SYMBOLS[new_index]
        return cipher_chunk

    def encrypt(self, message: str) -> str:
        """Encrypts the entire message."""
        cleaned_message = self._clean_message(message)
        split_message = self._split(cleaned_message)
        return ''.join(map(self._encrypt_chunk, split_message))

    def _decrypt_chunk(self, chunk: str) -> str:
        """Decrypts a chunk of the cipher."""
        message_chunk = ""
        for i, symbol in enumerate(chunk):
            new_index = (self.VALID_SYMBOLS.index(symbol) -
                         self.VALID_SYMBOLS.index(self.key[i])) % len(self.VALID_SYMBOLS)
            message_chunk += self.VALID_SYMBOLS[new_index]
        return message_chunk

    def decrypt(self, cipher: str) -> str:
        """Decrypts the entire cipher."""
        cleaned_cipher = cipher.replace(self.SPACE_SUBSTITUTE, ' ').replace(self.NEWLINE_SUBSTITUTE, '\n')
        split_cipher = self._split(cleaned_cipher)
        return ''.join(map(self._decrypt_chunk, split_cipher))

def main():
    # vgn = Vigenere('B~n!')
    # vgn = Vigenere('')
    # vgn = Vigenere('Poes')
    # vgn = Vigenere('cegcgcecdefg')
    vgn = Vigenere('bobsyouruncle')
    # vgn = Vigenere()
    
    original_message = 'Did you see? Those lizzards were jumping!'
    # original_message = "bob's your uncle could be used as a key for Vinegere."
    # original_message = "Line 1\nLine 2"
    # original_message = "abc\ndef"
    print(f"original message: {original_message}")
    cipher = vgn.encrypt(original_message)
    print(f"cipher: {cipher}")
    decrypted = vgn.decrypt(cipher)
    print(f"decrypted: {decrypted}")
    
if __name__ == "__main__":
    main()
