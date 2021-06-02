## The First Program
# print (-2)

## Arithmetic Operators

# 1 + 1 # Addition

# 1 - 1 # subtraction

# 1 / 1 # Division

# 1 * 1 # Multiplication

# 2**4 # exponentiation

## Values and Types

# Int

# Float

# String

## Formal and Natural Languages

## Debugging

## Glossary

## Exercises

# - Exercise 1:
    # 1. In a print statement, what happens if you leave out one of the parentheses, or both?

        # You got SyntaxError: Missing parentheses in call to 'print'

    # 2. If you are trying to print a string, what happens if you leave out one of the quotation marks,
    #   or both?
        # You got SyntaxError: EOL while scanning string literal

    # 3. You can use a minus sign to make a negative number like -2. What happens if you put a plus
        #sign before a number? What about 2++2?
    # I got correct result 4, WOWWWW

    # 4. In math notation, leading zeros are ok, as in 09. What happens if you try this in Python?
    # What about 011?

    # print(011) # I got error, SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

    # 5. What happens if you have two values with no operator between them?
    # print(2 2) # invalid syntaxe

# Exercise 1.2. Start the Python interpreter and use it as a calculator.

# 1. How many seconds are there in 42 minutes 42 seconds?

# minutes = 42
# seconds = 42
# minutes_to_seconds = minutes * 60
# final_result = minutes_to_seconds + seconds

# print(f"Convert 42 minutes 42 seconds to seconds, the result is : {final_result}")

# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

# result = 10 / 1.61

# print(result)

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
# mile in minutes and seconds)? What is your average speed in miles per hour?

average_pace = None
average_speed = None 