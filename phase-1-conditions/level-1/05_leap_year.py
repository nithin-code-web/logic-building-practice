# Problem:
# Check if a given year is a leap year

# Input:
# An integer year

# Output:
# Print "Leap year" if year is a leap year
# Print "Not a leap year" otherwise
# Note: A year is leap if divisible by 4 AND not by 100, OR divisible by 400

# Logic:
year = int(input("enter a year :"))

if year%4==0 and year%100 != 0 or year%400 ==0 :
    print("leap year")
else:
    print("not a leap year")


# Time Complexity:


# Space Complexity:

