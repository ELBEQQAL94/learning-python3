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
    dx = calc_diff(x1, x2)
    dy = calc_diff(y1, y2)
    dSquared = dx**2 + dy**2
    result = math.sqrt(dSquared)
    return result

def calc_diff(point1, point2):
    return point2 - point1

def is_between(x, y, z):
    if y > x and y < z:
        return True
    return False

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def countdown(n):
    if n <= 0:
        return 1
    else:
        print(n)
        countdown(n - 1)

def fib(n):
    if not isinstance(n, int):
        print("Enter an iteger")
        return None
    elif n < 0:
        print("Should not return an negative number")
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print(f"{fib(4)}")