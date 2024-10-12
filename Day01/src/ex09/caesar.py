import sys

def caesar(mode: str, text: str, shift: int):
    if mode == 'encode':
        encode(text, shift)
    elif mode == 'decode':
        encode(text, 26 - int(shift))
    else:
        print("Enter one of the following modes: encode/decode")
    
def encode(text: str, shift: int):
    encoded = ''
    for char in text:
        if ord(char) > 127:
            raise Exception("The script does not support your language yet")
        
        if char.isalpha():
            if char.isupper():
                char = chr((ord(char) + int(shift) - 65) % 26 + 65)
            else:
                char = chr((ord(char) + int(shift) - 97) % 26 + 97)
        encoded += char
    print(encoded)

if __name__ == "__main__":
    if len(sys.argv) == 4:
        caesar(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        raise Exception("Enter mode (encode/decode), text and shift")

