def cipher(text, shift, encrypt=True):

    """
    Encrypts and Decrypts messages.

    Parameters
    ----------
    text : String
      A string containing message to be encrypted/decrypted.
    shift : Integer
      A shift key to encrypt or decrypt.
    encrypt: Boolean argument
      encrypt = True for encryption; encrypt = False for decryption.



    Returns
    -------
    String
      Encrypted/Decrypted message.

    Examples
    --------
    >>> from cipher_khl2139 import cipher
    >>> text = "python"
    >>> shift = 3
    >>> encrypt = True
    >>> cipher_khl2319.cipher(text, shift)
    "sBwkrq"

    >>> text = "sBwkrq"
    >>> shift = 3
    >>> encrypt = False
    >>> cipher_khl2319.cipher(text, shift)
    "python"

    """


    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

