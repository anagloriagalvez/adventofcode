import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
data = open(os.path.join(__location__, 'day1.txt')).read().splitlines()

data_modified = []
for index,d in enumerate(data):
    if(index != 0 and index != len(data)-1):
        _r = int(data[index-1]) + int(d) + int(data[index+1])
        print("{} + {} + {} = {}\n".format(data[index-1],d,data[index+1],_r))
        data_modified.append(_r)

increased = 0
for index,d_m in enumerate(data_modified):
    if(index != 0): #avoid crash on first line
        if d_m > data_modified[index-1]:
            print("{} is greater than {}\n".format(d_m, data_modified[index-1]))
            increased = increased + 1

print("N times increased: {}".format(increased))
