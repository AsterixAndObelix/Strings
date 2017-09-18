text = input("What is the text?")

print(text)

specials = {"sir" : "matey" , "hotel" : "fleabag inn" , "student" : "swabble" , "boy" : "matey" , "madam" : "proud beauty" , "professor" : "foul blaggart" , "restaurant" : "galley" , "your" : "yer" , "excuse" : "are" , "students" : "swabbies" , "are" : "be" , "lawyer" : "foul blaggart" , "the" : "th'" , "restroom" : "head" , "my" : "me" , "hello" : "avast" , "is" : "be" , "man" : "matey"}

for akey in specials:
    text = text.replace(akey , specials[akey])

print(text)
