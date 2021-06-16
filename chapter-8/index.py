# def iter_str(string):
#     index = 0
#     while index < len(string):
#         letter = string[index]
#         print(f'{letter}')
#         index = index + 1

# def iter_str(string):
#     for char in string:
#         print(f"{char}")


# iter_str("Youssef")

# fruit = "banana"

# print(fruit[:])

def is_palindrome(str1, str2):
    return str1 == str2[::-1]

print(f'{is_palindrome("youssef", "deed")}')