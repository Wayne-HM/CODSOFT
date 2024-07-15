#Task2-Basic Arithmetical Operations Simple Calculator 
b=int(input("Enter first number:"))
c=int(input("Enter second number:"))
print("""\nCalculator Menu:
1.Addition
2.Subtraction
3.Multiplication
4.Division
5.Exit""")
a=input("Enter Your Choice:")
if a=="1":
    print("Addition of",b,"and",c)
    print("Result:",b+c)
elif a=="2":
    print("Subtraction of",b,"and",c)
    print("Result:",b-c)
elif a=="3":
    print("Multiplication of",b,"and",c)
    print("Result:",b*c)
elif a=="4":
    print("Division of",b,"and",c)
    print("Result:",b/c)
elif a=="5":
    print("Exiting....")
else:
    print("Re-Enter choice properly")
