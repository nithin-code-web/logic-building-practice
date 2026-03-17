# Problem:
# Check if a number is divisible by both 3 and 5

# Input:
# An integer number

# Output:
# Print "Divisible by both 3 and 5" if number is divisible by both
# Print "Not divisible by both 3 and 5" otherwise

# Logic:
num = int(input("enter a number:"))

if num%3 == 0 and num%5 ==0:
    print('{num} is divisible by both 3 and 5')
else :
    print('{num} is not divisible by both..')

# Time Complexity:


# Space Complexity:

