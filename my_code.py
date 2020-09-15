# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

def factorial_calc(num):   #you may choose the name of the parameter

    factorial = 1

    if num < 0:
        print("factorial does not exist for negative numbers.")
    elif num == 0:
        print("The factorial of 0 is 1.")   
    else:
        for x in range(1, num + 1):
            factorial = x + 1     
    return x    # be sure to return the factorial


if __name__ == '__main__':

    num = input("Enter number: ")
    # Test your code with this first
    # Change the argument to try different values
    print(factorial_calc(num))

    # After you are satisfied with your results, use input() to prompt the user for a value:
    #num = input("Enter value to factorialize: ")
    #print(factorial_calc(int(num)))
