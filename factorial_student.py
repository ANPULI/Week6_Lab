def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num*factorial(num-1)

def main():
    number = int(input("Enter a nonnegative integer: "))
    fact = factorial(number)
    print("The factorial of", number, "is", fact)

print("Test branch.")        
main()
