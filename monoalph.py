
PLAINTEXT_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
CIPHERTEXT_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encipher_dict(keyword):
    """
    Construct a plaintext-to-ciphertext substitution dictionary.

    Purpose:
        Construct a monoalphabetic substitution alphabet from a keyword.
        Repeated letters in the keyword are removed, preserving their
        first occurrence. The remaining letters of the alphabet are
        appended in alphabetical order.

    Parameters:
        keyword: The keyword used to construct the cipher alphabet; str

    Return Value:
        A dictionary mapping each plaintext letter to its
        corresponding ciphertext letter; dict

    Examples:
        >>> cipher = encipher_dict("SECRET")
        >>> cipher["a"]
        'S'
        >>> cipher["b"]
        'E'
        >>> cipher["z"]
        'Z'
        >>> len(cipher)
        26
        >>> len(set(cipher.values()))
        26
    """
    

def decipher_dict(cipher_dict):
    """
    Construct the inverse of a substitution dictionary.

    Purpose:
        Reverse a plaintext-to-ciphertext dictionary so that ciphertext
        letters map back to their corresponding plaintext letters.

    Parameters:
        cipher_dict: A dictionary mapping plaintext letters
            to ciphertext letters; dict

    Return Value:
        A dictionary mapping ciphertext letters to plaintext
        letters; dict

    Examples:
        >>> cipher = encipher_dict("SECRET")
        >>> decipher = decipher_dict(cipher)
        >>> decipher["S"]
        'a'
        >>> decipher["E"]
        'b'
        >>> decipher["Y"]
        'y'
        >>> len(decipher)
        26
    """

    

def encipher(message, cipher_dict):
    """
    Encrypt a message using a substitution dictionary.

    Purpose:
        Replace each uppercase or lowercase letter in the message
        according to the substitution dictionary. Preserve the case
        of letters and leave nonalphabetic characters unchanged.

    Parameters:
        message: The plaintext message to encrypt; str
        cipher_dict: A dictionary mapping uppercase plaintext
            letters to uppercase ciphertext letters; dict

    Return Value:
        The encrypted message; str

    Examples:
        >>> cipher = encipher_dict("SECRET")
        >>> encipher("abc", cipher)
        'SEC'
        >>> encipher("hello, world!", cipher)
        'DTIIL, WLOIR!'
        >>> encipher("python 123!", cipher)
        'MYQDLK 123!'
        >>> encipher("", cipher)
        ''
    """
    

def decipher(message, decrypt_dict):
    """
    Decrypt a message using a substitution dictionary.

    Purpose:
        Reverse a monoalphabetic substitution by constructing the
        inverse dictionary and applying it to the ciphertext.

    Parameters:
        message: The ciphertext message to decrypt; str
        decrypt_dict: A dictionary mapping ciphertext letters
            to plaintext letters; dict

    Return Value:
        The decrypted plaintext message; str

    Examples:
        >>> cipher = encipher_dict("SECRET")
        >>> dec_cipher = decipher_dict(cipher)
        >>> decipher("SEC", dec_cipher)
        'abc'
        >>> decipher("DTIIL, WLOIR!", dec_cipher)
        'hello, world!'
        >>> decipher("MYQDLK 123!", dec_cipher)
        'python 123!'
        >>> decipher("", dec_cipher)
        ''
    """


def encrypt(message, keyword):
    '''
    Purpose: Encrypt the message into ciphertext using a 
    monoalph whose key is determined by the keyword.

    Parameters:
        message: the plaintext to encrypt; str
        keyword: the keyword to use to construct the monoalph key; str

    Return Value: encrypted plaintext as ciphertext; str

    Examples:
        >>> key = "SECRET"
        >>> encrypt("abc", key)
        'SEC'
        >>> encrypt("hello, world!", key)
        'DTIIL, WLOIR!'
        >>> encrypt("python 123!", key)
        'MYQDLK 123!'
    '''


def decrypt(message, keyword):
    '''
    Purpose: To decrypt the message into plaintext using a monoalph
    whose key is determined by the keyword.

    Parameters:
        message: the ciphertext to be decrypted; str
        keyword: the keyword to use to construct the monoalph key; str

    Return Value: decrypted ciphertext as plaintext; str

    Examples:
        >>> key = "SECRET"
        >>> decrypt("SEC", key)
        'abc'
        >>> decrypt("DTIIL, WLOIR!", key)
        'hello, world!'
        >>> decrypt("MYQDLK 123!", key)
        'python 123!'
    '''


if __name__ == "__main__":
    pass