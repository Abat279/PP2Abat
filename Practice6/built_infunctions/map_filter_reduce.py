from functools import reduce



numbers = [1,2,3,4,5]
squares = list(map(lambda x: x**2, numbers))
print(squares)



names = ["ali","dana","aida"]
upper = list(map(str.upper, names))
print(upper)



nums = [10,15,20,25]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)


big = list(filter(lambda x: x > 15, nums))
print(big)



total = reduce(lambda x,y: x+y, numbers)
print(total)