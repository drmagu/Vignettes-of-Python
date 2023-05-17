# Vigenere Extended cipher
## What it is
The original vigenere cipher was meant to encode text consisting of (lower case) alpha characters. 
Read here: [Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)  
It can be extended to:
* allow more characters
* allow multi-line text

In the file *vigenere_class.py*, we define:
* the _class_ **Vigenere**
* which can be instantiated with a **key**
    * vigenere = __Vigenere__("ThisIsTheKey")
* the following methods are available:
    * vigenere.__encrypt__(message: str) -> str
    * vigenere.__decrypt__(cipher: str) -> str

One more thing: 
* the _key_ can not be an _empty_ string
* the _key_ may only contain symbols that are in the symbol table



## Implementation
All is implemented in Python 3.
The file *vigenere_class.py* has the class definition, methods, etc as described above.  
The **Vigenere** class uses a symbol table which has most of the keys on a standard (US) keyboard.  
The _symbols_ that can be handled are stored in a string of length 74.
The _symbol table_ functionality is implemented:
* looking up the index of a symbol in the symbols string:
    * example: symbols.index('a') would return 1.
* looking up the symbol at a particular index:
    * example: symbols[2] would return 'b'.
* to be able to encrypt larger texts, we also need a symbol for the 'newline'.

In the **encrypt** method, we make sure that there are no spaces or newlines in he encryption.
* when we encounter a space, ' ', we encrypt it as '~'
* when a newline, '\n', is encountered it is encrypted as '`'

In the **decrypt** method, any '~' and '`' is replaced with ' ' and '\n' respectively.

## Testing
To demo and test we have a file *vigenere_demo.py*  
We import the **Vigenere** class, and define a **Usecases** class.

_usecases_ are kept in an array in **Usecases**.  
A __usecase__ can be added using the __add__ method wich takes 3 parameters:
* a _name_, which is descriptive
* the _text_ to be encrypted
* the _key_ for the _vigenere_ instance to be used

A __usecase__ is selected by providing an index.  
So if there are 4 _usecases_, as in the *vigenere_demo.py* file 0, 1, 2, 3 will select a usecase.  

The **process_use_case()** function does encryption, decryption and provides output on the console.  
* example: process_use_case(usecases, 0)
    * usecase: simple, key: None (meaning not specified, so the class default key is used)
    * original: expectattackatdawn
    * encrypted: uLuxsHfLIphCqHitLB
    * decrypted: expectattackatdawn

In the *vigenere_demo* we have a 
* simple demo ... just lower case alpha
* a line with some punctutuation and other symbols
* a multi-line message
* a longer message read from the included text file _tomsawyer.txt_

