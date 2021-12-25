
def encrypt_char_caesar(ch, k):
    aski = ord(ch)-ord('a')  # between 0 and 25
    shifted_aski = aski + k
    mod = shifted_aski % 26
    return chr(mod + ord('a'))


def encrypt_caesar(text, key):
    result = ''
    for ch in text:
        result += encrypt_char_caesar(ch, key)
    return result
