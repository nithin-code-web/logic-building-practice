# Problem:
# Check whether a given number is even or odd

# Input:
# An integer number

# Output:
# Print "Even" if the number is divisible by 2
# Print "Odd" if the number is not divisible by 2

# Logic:
def evenOdd(num):
    if num%2 == 0:
        return True
    else:
        return False
    
num = int(input("enter a number :"))
final = evenOdd(num)
print(final)


# Time Complexity:


# Space Complexity:

