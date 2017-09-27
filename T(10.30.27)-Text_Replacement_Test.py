text = open ("T(10.30.27)-Text_Replacement_Text_File" , "r")

def replace(original, remove, plus):
    new = original.split()
    print(new)
    num = new.count(remove)
    for counter in range (num):
        position = new.index(remove)
        newPosition = int(new.pop(position))
        new.insert(newPosition, plus)

print(text)

remove = input("What would you like to remove from the string? ")
plus = input("What would you like to put instead? ")

replace(text, remove, plus)

text.close()
