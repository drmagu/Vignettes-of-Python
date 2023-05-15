from os import sys

# applying the Vigenere cipher.
from vigenere_class import Vigenere

class Usecases:
    # the use cases need two elements: the text to encrypt, the key to use
    def __init__(self):
        self.usecases = []

    def add(self, name: str, text: str, key=None):
        usecase = {name:{"key":key, "text":text}}
        self.usecases.append(usecase)
    
    def select(self, casenumber: int):
        # we need to return the case title, text and key
        if casenumber not in range(len(self.usecases)):
            print(f"invalid case number: {casenumber}")
            return
        usecase = self.usecases[casenumber]
        case_name = list(self.usecases[casenumber].keys())[0]
        case_text = usecase[case_name]['text']
        case_key = usecase[case_name]['key']
        return (case_name, case_text, case_key)
    
if __name__ == "__main__":
    # what we like to see for each usecase
    def process_use_case(usecases: list, case_number: int):
        usecase = usecases.select(case_number)
        if usecase is not None:
            (name, text, key) = usecase
            print(f"usecase: {name}, key: {key}")
            vgn = Vigenere(key)
            original = text
            encrypted = vgn.encrypt(text)
            decrypted = vgn.decrypt(encrypted)
            print(f"\noriginal: \n{original}")
            print(f"\nencrypted: {encrypted}")
            print(f"\ndecrypted: \n{decrypted}")    
        return
    
    usecases = Usecases()
    usecases.add('simple', 'expectattackatdawn')
    usecases.add('symbol_table', 
                'Did you see those 4 lizzards? They were really jumpin!',
                "Bob'sYourUncle")
    message = "On the count of 3 .. we GO!\n..1\n..2\n..3\nHURRAH!!"
    usecases.add("multi-line", message, "SeeIfYouGetThis")
    
    # get a message from a text file
    script_folder = sys.path[0] + '/'
    with open(script_folder + 'tomsawyer.txt') as f:
        message = f.read()
    usecases.add("from_a_file", message, "tomsawyer.txt")

    process_use_case(usecases, 0)
    print()
    
    process_use_case(usecases, 1)
    print()
    
    process_use_case(usecases, 2)
    print()
    
    process_use_case(usecases, 3)
    print()

    process_use_case(usecases, 4)
    print()

    