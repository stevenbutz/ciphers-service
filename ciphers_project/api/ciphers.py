

def caesar_encode(plain_text, shift):
    cipher_text = ""
    for c in plain_text:
        if c.isalpha():
            # Adjust shift for uppercase and lowercase letters
            base = ord('A') if c.isupper() else ord('a')
            # Shift within the alphabet range
            c_encoded = (ord(c) - base + shift) % 26 + base
        else:
            # Non-alphabetic characters are not shifted
            c_encoded = ord(c)
        cipher_text += chr(c_encoded)
    return cipher_text

