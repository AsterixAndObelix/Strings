fileref = open ("T(11.8.4)-Lab_Data" , "r")

counter = 0
xavg = 0
yavg = 0

for lines in fileref:
    counter += 1
    num = lines.split()
    xavg += int(num[0])
    yavg += int(num[1])

xavg = xavg / counter
yavg = yavg / counter

def mguy():

ytie = yavg + mguy()
