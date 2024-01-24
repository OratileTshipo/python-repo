
#text = 'Hello Zaira'
#shift = 3
message = input("Please enter the message you want to encrypt: ")
offset = int(input('What is the encryption offset number? '))

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

#caesar(message,offset)
#caesar(message,5)

def main():
    caesar(message,offset)

if __name__ == "__main__":
    main()