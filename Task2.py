#Task2-Basic Arithmetical Operations Simple Calculator 
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("""\nCalculator Menu:
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit""")
a=input("Enter Your Choice:")
if a=="1":
    print("Addition of",num1,"and",num2)
    print("Result:",num1+num2)
elif a=="2":
    print("Subtraction of",num1,"and",num2)
    print("Result:",num1-num2)
elif a=="3":
    print("Multiplication of",num1,"and",num2)
    print("Result:",num1*num2)
elif a=="4":
    print("Division of",num1,"and",num2)
    print("Result:",num1/num2)
elif a=="5":
    print("Exiting....")
else:
    print("Re-Enter choice properly")
