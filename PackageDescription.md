# DATA533 LAB2 
## PACKAGE TOPIC :
There are four modules in the package. The package is called `encryptor`. The subpackes are **encrycomplex** and 
**encrysimple** . The developers are :
- encrycomplex --> **DEBANGSHA KUSUM SARKAR**
- encrysimple  --> **SARAH HALIMA BESISIRA**
The `encrycomplex` subpackage contains two modules :    
`sub`       
- The module encrypts a message using one key that is entered as an interger and it shifts the message letter by letter 
according to the key. **This kind of encryption is called Substitution Encryption.**
- The module also decrypts the message given that we know the key value of the encryption.
`tran`
- The module encrypts the message by jumbling up the letters in the message text letter by letter. ** This kind of encryption
is called Transposition Encryption.**

The `encrysimple` subpackage contains two modules :
`mirror`
- The module reverses the message from end to start word by word. It is a method of simple encryption.
`mirrorsquared`
- The module reverses the message from end to start word by word and also letter by letter. It is also a method of 
simple encryption.
-----------------------------------------------------------------------------------------------------------------------------
## PACKAGE STRUCTURE :
`encryptor` --> package
- `encrycomplex` --> subpackage
  - `sub` --> module
  - `tran` --> module
- `encrysimple` --> subpackage
  - `mirror`  --> module
  - `mirrorsquared` --> module
## DETAILS :        
The package `encryptor` has two packages `encrycomplex` and `encrysimple`. We shall discuss them one by one.        
#### encrycomplex       
`sub`   
Module saved as ***sub.py***. The module contains :
- Class `Suben` : Here inside `__init__` method we initialize the **text** and **key** for excryption.
- Class `Encr` : It inherits the `Suben` class.
  - The `__init__` method encrypts the message by taking the message letter by letter and saving the ASCII value in a variable.
    Then it shifts the value by key amount and converts it back to the string. Thus we get the encrypted message.
  - The `display` method returns the encrypted message
- Class `Decr` : It inherits the `Suben` class.
  - The `__init__` method decrypts the encrypted message by taking the message letter by letter and saving the ASCII value in
    a variable. Then it shifts the value back by key amount and converts it back to the string to the original message. 
    Thus we get the decrypted message.
  - The `display` method returns the decrypted message   

`tran`                        
Module saved as ***tran.py***. The module contains :          
- The method `tran` imports random module. It creates a sample of random numbers of the length of text and 
  it looks for the character present in the message indexed at that random number in the message and assigns it to a new string. 
  So the output is a encrypted message. Since the numbers are random we can only decrypt it by setting a seed for the number generator.
  
 #### encrysimple
 `mirror`       
 This module is saved as ***mirror.py***. The module contains :
 - Class `Mirror` : The class has two methods.
    - `__init__` method initializes the text that needs to be mirrored.
    - `text_revmirror` method reverses the text to generate the encrypted text.
  
  `mirrorsquared`       
  This module is saved as ***mirrorsquared.py***. The module contains :
  - Class `MirrorSquared` : The class has two methods:
    - `__init__` method initializes the text message to be encrypted.
    - `text_revsquared` method revereses the the message first word by word and then letter by letter and generates the output.
    
  ## IMPORTED MODULES :
  -  random
