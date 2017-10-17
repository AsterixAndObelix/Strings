alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt_6(message, alphabet):
    for word in message:
        for character in word:
            for letter in alphabet:
                if character == letter:
                    left = alphabet.index(character) - 6
                    if left < 0:
                        left = left + 27
                        message = " ".join(message)
                    message = message.replace(character, alphabet[left])
    return message


message = input("What's the message?")
message = message.split()

print(encrypt_6(message, alphabet))
