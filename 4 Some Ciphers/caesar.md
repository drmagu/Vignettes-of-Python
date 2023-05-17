# Caesar cipher
## Principles
A simple substitution cipher. In our context, we have the following restrictions:
* only lower case alphabetic characters
* the key is the shift that is applied in encryption
* in decryption the same shift is applied in the opposite direction  

Also see [Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) in wikipedia.  

## Implementation
The implementation is in Python 3, see *caesar_class.py*  

We use a class, called Caesar. 
The Caesar class can be instantiated with a 'shift' like so:
* caesar = __Ceasor__(14)  
Onde we have the __caesor__ object, we can use the methods:
* caesar.__clean__(message: str) -> str, which removes all characters not in the lower case alphabet.
* caesor.__encrypt__(message: str) -> str, which encodes the (cleaned) message.
* caesar.__decrypt__(message: str) -> str, which decodes the encoded message.  






