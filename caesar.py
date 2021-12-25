
def encrypt_char_cesar(ch, k):
    aski = ord(ch)-ord('a')  # between 0 and 25
    shifted_aski = aski + k
    mod = shifted_aski % 26
    return chr(mod + ord('a'))

def hello():
    print("hello")

def hi():
    print("hello")

def encrypt_cesar(text, key): # question 2
    result = ''
    for ch in text:
        result += encrypt_char_cesar(ch, key)
    return result

