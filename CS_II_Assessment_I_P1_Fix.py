alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt_6(message, alphabet, words):
    check = []
    for word in words:
        #print(words)
        #print(word)
        for character in word:
            #print(character)
            for letter in alphabet:
                #print(letter)
                if character == letter:
                    left = alphabet.index(letter) - 6
                    if left < 0:
                        left = left + 25
                        print(left)
                    check.append(left)
    for checker in check:

    return new

message = input("What's the message?")

words = message.split()

print(encrypt_6(message, alphabet, words))
