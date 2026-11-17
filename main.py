import caesar
import monoalph



def combo_encipher(message, keyword, shift):
    '''
    Purpose: To encrypt the plaintext message with a monoalph
    keyword and a Caesar shift.

    Parameters: 
        message - the plaintext message to be enciphered; str
        keyword - the keyword used for the monoalph cipher; str 
        shift - the amount to shift each letter; int

    Return Value: The ciphertext that has been encrypted; str
    
    Examples:
        >>> m_word = "SECRET"
        >>> c_key = 6
        >>> combo_encipher("", m_word, c_key)
        ''
        >>> combo_encipher("a", m_word, c_key)
        'Y'
        >>> combo_encipher("abc", m_word, c_key)
        'YKI'
        >>> combo_encipher("hello", m_word, c_key)
        'JZOOR'
    '''

    

def combo_decipher(message, keyword, shift):
    '''
    Purpose: To decrypt the ciphertext message with a monoalph
    keyword and a Caesar shift.

    Parameters:
        message - the ciphertext that needs to be decrypted; str
        keyword - the keyword that was used for the monoalph portion of the encryption; str
        shift - the shift that was used to encrypt the ciphertext; str

    Return Value: The decrypted text; str

    Examples:
        >>> m_word = "SECRET"
        >>> c_key = 6
        >>> combo_decipher("", m_word, c_key)
        ''
        >>> combo_decipher("Y", m_word, c_key)
        'a'
        >>> combo_decipher("YKI", m_word, c_key)
        'abc'
        >>> combo_decipher("JZOOR", m_word, c_key)
        'hello'
    '''

    

if __name__ == "__main__":
    pass