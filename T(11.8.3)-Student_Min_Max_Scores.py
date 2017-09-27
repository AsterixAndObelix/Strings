fileref = open ("T(11.8.1-3)-Student_Data" , "r")

def set (text):
    for lines in text:
        values = lines.split()
        name = values.pop(0)
        print(name , " " , max(values) , min(values))

set(fileref)
