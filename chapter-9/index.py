file = open("test.txt")
line = file.readline()

for word in line:
    print(f'word: {word}')
