def flip(text):
    words = text.split()
    final = []
    for word in words:
        new = []
        for letter in word:
            new.append(letter)
        new.reverse()
        new = "".join(new)
        final.append(new)
    final = " ".join(final)
    return final
