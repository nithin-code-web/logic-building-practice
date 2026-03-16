def evenOdd(num):
    if num%2 == 0:
        return True
    else:
        return False
    
num = int(input("enter a number :"))
final = evenOdd(num)
print(final)

