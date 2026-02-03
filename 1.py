n = int(input())

numbers = input().split()
mx = int(numbers[0])
for x in numbers:
    if int(x) > mx:
        mx = int(x)
print(mx)

