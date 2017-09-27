fileref = open ("T(11.8.1-3)-Student_Data" , "r")

def set (text):
    for lines in text:
        values = lines.split()
        name = values.pop(0)
        adding = 0
        counter = 0
        for value in values:
            counter += 1
            value = int(value)
            adding = adding + value
        average = adding / counter
        print(name , " " , average)

set(fileref)
