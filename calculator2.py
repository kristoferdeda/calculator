def main():
    while True:
        try:
            n_1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /, ^): ")           
            while op not in ["+", "-", "*", "/", "^"]:
                op = operator()
            n_2 = float(input("Enter second number: "))
        except ValueError:
            print("You did not enter a valid input!")
        else:
            break
    
    calculate(n_1, op, n_2)

def operator():
        y = input("Invalid input. Please try again: ")
        return y

def calculate(a, b, c):
    if b in ["+", "-", "*", "/", "^"]:
        if b == "+":
            print("Result is: ", a+c)
        elif b == "-":
            print("Result is: ", a-c)
        elif b == "*":
            print("Result is: ", a*c)
        elif b == "/":
            if c != 0:
                print("Result is: ",a/c)
            else:
                print("You cannot divide by 0")
        elif b == "^":
            print("Result is: ", pow(a, c))
        else:
            print("Please use a valid operator!")

    ask = input("Do you want to make another calculation (y|n): ")
    
    while ask not in ["n", "N", "y", "Y"]:
        ask = input("Invalid input. Please try again (y|n): ")
    if ask == "n" or ask =="N":
        print("Thank you for using the Calculator!")
    elif ask == "y" or ask == "Y":
        main()
    
main()