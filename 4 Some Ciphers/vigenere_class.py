from copy import copy

class Vigenere:
     
    def __init__(self, key=None):
        self.symbols = " abcdefghijklmnopqrstuvwxyz" + "\n" + \
             "ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
             ".,?!1234567890" + "\"'" + "-:;–"

        if key is None:
            key='poes'
        self.key = key
        self.key_len = len(key)
        # check the key
        if len(key) == 0:
            print(f"Invalid key {key}:\nKey can not be \'\'.")
            exit()
        for symbol in key:
            if not symbol in self.symbols:
                print(f"Invalid key '{key}':\nsymbol '{symbol}' may not be used in the key.")
                exit()
        # good key :)
        self.key = key
        self.key_len = len(key)
    
    def encrypt(self, message: str) -> str:
        # clean message
        message = [message[i] for i in range(len(message)) if message[i] in self.symbols]
        # split in chunks of key_len
        split_message = []
        for i in range(0, len(message), self.key_len):
            split_message.append(''.join(message[i:i + self.key_len]))
        # print(split_message)
        # encode the chunks by shifting
        cipher_chunks = []
        for split in split_message:
            chunk = ""
            for i in range(len(split)):
                new_index = (self.symbols.index(split[i]) + \
                            self.symbols.index(self.key[i])) % len(self.symbols)
                # avoid having spaces in the cipher
                # substitute by '~'
                if self.symbols[new_index] == ' ':
                    chunk += '~'
                # avoid having new lines in the cipher
                # substitute by '`'
                elif self.symbols[new_index] == '\n':
                    chunk += '`'
                else:
                    chunk += self.symbols[new_index]
            cipher_chunks.append(chunk)
        return ''.join(cipher_chunks)

    def decrypt(self, cipher: str) -> str:
        # take care of '~', which is NOT in the symbol table
        # take care of '`', which is NOT in the symbol table
        if '~' in cipher or '`' in cipher:
            cleaned_cipher = ""
            for symbol in cipher:
                if symbol == '~':
                    cleaned_cipher += ' '
                elif symbol == '`':
                    cleaned_cipher += '\n'
                else:
                    cleaned_cipher += symbol  
            cipher = cleaned_cipher
        # split in chunks of key_len
        split_cipher = []
        for i in range(0, len(cipher), self.key_len):
            split_cipher.append(''.join(cipher[i:i + self.key_len]))
        # print(split_cipher)
        # decode the chunks by shifting
        message_chunks = []
        for split in split_cipher:
            chunk = ""
            # print(f"split: {split}")
            for i in range(len(split)):
                new_index = (self.symbols.index(split[i]) - \
                    self.symbols.index(self.key[i])) % len(self.symbols)
                chunk += self.symbols[new_index]
            message_chunks.append(chunk)
        return ''.join(message_chunks)


def main():
    # vgn = Vigenere('B~n!')
    # vgn = Vigenere('')
    # vgn = Vigenere('Poes')
    # vgn = Vigenere('cegcgcecdefg')
    # vgn = Vigenere('bobsyouruncle')
    vgn = Vigenere()
    
    # original_message = 'Did you see? Those lizzards were jumping!'
    # original_message = "bob's your uncle could be used as a key for Vinegere."
    # original_message = "Line 1\nLine 2"
    original_message = "abc\ndef"
    print(f"original message: {original_message}")
    cipher = vgn.encrypt(original_message)
    print(f"cipher: {cipher}")
    decrypted = vgn.decrypt(cipher)
    print(f"decrypted: {decrypted}")
    
if __name__ == "__main__":
    main()
