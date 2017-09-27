text = input("What is the text? ")

def mush(index, counter):
    for count in range(counter):
        print(index[count] , input("insert"))

def push(text):
    index = []
    counter = 0
    for word in text:
        index.append(word)
        counter += 1
    return mush(index, counter)

def mash(text):
    text = text.split()
    return push(text)

def drag(text):
    text = text.strip()
    return mash(text)

print(drag(text))
