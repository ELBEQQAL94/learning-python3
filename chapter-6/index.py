import math

# Fruitful functions
def area(radius):
    temp = math.pi * radius**2
    return temp

def compare(a, b):
    if a > b:
        return 1
    elif a == b:
        return 0
    else: return -1

# def distance(x1, y1, x2, y2):
#     test = pow((y1 - y2), 2) + pow((x1 - x2), 2)
#     result = pow(test, (1/2)) 
#     return result

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dSquared = dx**2 + dy**2
    result = math.sqrt(dSquared)
    return result
    
print(f"The distance is: {distance(1, 2, 4, 6)}")