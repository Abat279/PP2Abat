
with open("file1.txt", "w") as f:
    f.write("Hello Python\n")



with open("file2.txt", "w") as f:
    f.write("Line 1\nLine 2\n")



lines = ["Apple\n", "Banana\n", "Cherry\n"]

with open("file3.txt", "w") as f:
    f.writelines(lines)


name = "Ali"

with open("file4.txt", "w") as f:
    f.write(f"My name is {name}")



numbers = [1,2,3,4,5]

with open("numbers.txt", "w") as f:
    for n in numbers:
        f.write(str(n) + "\n")