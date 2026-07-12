#Exception handing
#Prevent program crashes
#Display user friendly messages
#Handle unexpected sitiuations gracefully
#Try block will place the code which I may uncertain of.
#Finally --> Irrespecive of code runs or fails finally it will excicute.


#Example code:

# num1 = int(input("Enter first number: " ))
# num2 = int(input("Enter second number: " ))
# result = num1 / num2
# print(result)
# print("Program finished")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Program ended")