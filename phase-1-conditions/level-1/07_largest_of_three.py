# Problem:
# Find and print the largest among three numbers

# Input:
# Three integer numbers

# Output:
# Print the largest number

# Logic:
num1 = int(input("enter a number :"))
num2 = int(input("enter a number :"))
num3 = int(input("enter a number :"))

if num1 > num2 | num1 > num3:
    print("num1 is greater than among three")
elif num2 > num1 | num2 > num3:
    print("num2 is greater than among three")
else:
    print("num3 is greater than among three")
# Time Complexity:


# Space Complexity:

