fileref = open ("T(11.8.1-3)-Student_Data" , "r")

for line in fileref:
    data = line.split()
    if len(data[1:]) > 6:
        print(data[0])

fileref.close()
