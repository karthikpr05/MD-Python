#marks = int(input("Eenter Marks1: "))
#if marks >= 90:
#    print("Grade A")
#elif marks >=50:
#    print("Grade B")


#product1 = int(input("Enter the value  of the product:"))
#if product1 >= 5000:
#    print("Disccount is 5%")
#elif product1 >= 3000:
#    print("Discount is 3%")
#elif product1 < 1000:
#    print("Discount is not available")





num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number:"))
operator = input("Enter operator (+,-,*,%):")

match operator:
    case "+":
        print("Result =", num1 + num2)
    case "*":
        print("Result =", num1 * num2)
    case "-":
        print("Result =", num1 - num2)
    case "%":
        print("invalid operator")