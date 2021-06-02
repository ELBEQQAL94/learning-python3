def main():
    x = 4
    y = 3

    if x > y:
        print("x greater than y")
    elif x > 1:
        print("x greater than 1")
    else: print("programme done!")


def countdown(n):
    if n <= 0:
        print("countdown done!")
    else:
        print(n)
        countdown(n - 1)

def draw_stack_diagram(s, n):
    if n <= 0:
        print("done!")
    else:
        print(f"{n}: {s}")
        draw_stack_diagram(s, n - 1)

def fermat_check_formula(n):
    if n < 2:
        print("No, That doesn't work.")
    else:
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))
        a = int(input("Enter a: "))
        a_plus_b = pow(a, n) + pow(b, n)
        c_pow_n = pow(c, n)

        if a_plus_b == c_pow_n:
            print("Good!")
        else: print("Bad!")


# fermat_check_formula(1)
fermat_check_formula(3)