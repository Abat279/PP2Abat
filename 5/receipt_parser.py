import re

# Read receipt file
with open("raw.txt", "r") as file:
    text = file.read()

print("----- Example 1: re.search() -----")
date = re.search(r'\d{2}/\d{2}/\d{4}', text)
if date:
    print("Date:", date.group())

print("\n----- Example 2: re.findall() prices -----")
prices = re.findall(r'\d+\.\d{2}', text)
print("Prices:", prices)

print("\n----- Example 3: re.findall() products -----")
products = re.findall(r'[A-Za-z]+(?=\s\d+\.\d{2})', text)
print("Products:", products)

print("\n----- Example 4: re.split() -----")
lines = re.split(r'\n', text)
print("Lines:", lines)

print("\n----- Example 5: re.sub() -----")
clean_text = re.sub(r'\$', '', text)
print("Clean text:", clean_text)

# Calculate total
numbers = re.findall(r'\d+\.\d{2}', text)
total = sum(float(n) for n in numbers)
print("\nTotal:", total)
