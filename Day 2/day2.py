import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def get_command(line:str=None):
    _c = line.split(" ")

    if _c[0] == "forward":
        return "horizontal", int(_c[1])

    elif _c[0] == "down":
        return "depth", int(_c[1])

    elif _c[0] == "up":
        return "depth", (-int(_c[1]))

data = open(os.path.join(__location__, 'day2.txt')).read().splitlines()

horizontal_value = 0
depth_value = 0
aim = 0

for d in data:
    instruction, value = get_command(d)

    if instruction == "horizontal":
        horizontal_value = horizontal_value + value
        depth_value = value * aim + depth_value

    elif instruction == "depth":
        aim = aim + value

print("Horizonal position: {}\n Depth: {}\n Total: {}\n".format(horizontal_value, depth_value, horizontal_value * depth_value))
