import turtle

text = input("What is the text?\n")

letters = {"a" : 0 , "b" : 0 , "c" : 0 , "d" : 0 , "e" : 0 , "f" : 0 , "g" : 0 , "h" : 0 , "i" : 0 , "j" : 0 , "k" : 0 , "l" : 0 , "m" : 0 , "n" : 0 , "o" : 0 , "p" : 0 , "q" : 0 , "r" : 0 , "s" : 0 , "t" : 0 , "u" : 0 , "v" : 0 , "w" : 0 , "x" : 0 , "y" : 0, "z" : 0}

print(letters)

for counter in text:
    for letter in letters:
        if letter == counter:
            letters[letter] = letters[letter] + 1

values = []

for letter in letters:
    if letters[letter] != 0:
        values.append(letters[letter])

print(values)

def main():
    t = turtle.Turtle()           # create the turtle
    wn = turtle.Screen()

    for ctie in values:
        print(ctie)
        t.down(ctie)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(ctie)
        t.left(90)
    wn.exitonclick()

main()
