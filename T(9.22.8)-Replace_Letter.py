text = input("What is the text?\n")
letter = input("What is the letter?\n")

def remove_letter(letter, text):
    text = text.replace(letter, "")
    print(text)

remove_letter(letter, text)
