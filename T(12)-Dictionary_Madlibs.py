text = open("T(10.30.27)-Text_Replacement_Text_File", "r")

print(text)

noun = input("Noun:\n")
verb = input("Verb:\n")
adjective = input("Adjective:\n")

specials = {"lists" : noun , "strings" : noun , "tuples" : noun , "change" : verb , "different" : adjective}

for akey in specials:
    text = text.replace(akey, specials[akey])
    print(text)

text.close()
