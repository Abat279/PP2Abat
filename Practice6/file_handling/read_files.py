
with open("example.txt", "r") as f:
    print(f.read())



with open("example.txt", "r") as f:
    print(f.readline())



with open("example.txt", "r") as f:
    lines = f.readlines()
    print(lines)



with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())



with open("example.txt", "r") as f:
    print(f.read(10))