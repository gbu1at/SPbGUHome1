def caesar_encrypt_char(letter: str, n: int) -> str:
    n = n % 26
    if letter in ".-' ,!?": return letter
    new_letter = ""
    if ord(letter) >= ord('a'):
        new_letter = chr((ord(letter) - ord('a') + n) % 26 + ord('a'))
    else:
        new_letter = chr((ord(letter) - ord('A') + n) % 26 + ord('A'))
    return new_letter


def caesar_encrypt(message: str, n: int) -> str:
    """Encrypt message using caesar cipher

    :param message: message to encrypt
    :param n: shift
    :return: encrypted message
    """

    res = []
    for letter in message: res.append(caesar_encrypt_char(letter, n))
    return "".join(res)
