# https://www.codewars.com/kata/556deca17c58da83c00002db/train/python
# def sum_numbers_in_list(list):
#     sum = 0

#     for number in list:
#         sum += number

#     return sum
    
# def tribonacci(signature, n):
    
#     start = 0
#     end = 3

#     if n <= len(signature):
#         # slice signature until n
#         return signature[:n]

#     for i in range(len(signature) - 1, n):
#         signature.append(sum(signature[start:end]))
#         start += 1
#         end += 1

#     return signature[:n]

def tribonacci(signature, n):
    res = signature[:n]
    print("res: ", res[-3:])
  

# print(tribonacci([1, 1, 1], 1)) # [1]
# print(tribonacci([300, 200, 100], 0)) # []
print(tribonacci([3, 2, 1, 4], 10)) # [3, 2, 1, 6, 9, 16, 31, 56, 103, 190])