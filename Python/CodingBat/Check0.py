"""
Question #1 - Search for Zero

Write a program that takes multiple numbers as an input.
Return 'Yes' if the digit 0 appears anywhere in the array.
Otherwise, return 'No'.
The first input should be the count of the numbers to be provided.
Each subsequent number will be part of the array.
Each input should be provided in a new line"""
arr = []
size = int(input("Enter the size of an array = "))
print(f"Enter {size} numbers")
for x in range(size):
    num = int(input("Enter num = "))
    arr.append(num)
print(arr)
print("Is there 0 in an array?")
for x in range(size):
    if "0" in str(arr[x]):
        print("Yes!")
        break;
else:
    print("No!")

