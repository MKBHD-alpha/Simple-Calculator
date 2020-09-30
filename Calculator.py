def welcome():
    print('''
     Welcome to the calculator :) (Developed by Deebarghya)
     ''')
welcome()

while True:

    a=float(input("Enter the first number:------"))

    b=float(input("Enter the another Number:-----"))

    print("Select the Operation you like")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    c=input("Enter your choice(1,2,3,4) any one at a time:-------")

    if c in ('1','2','3','4'):


        if c== "1":
            print("Result of",a,"+",b, "=", a+b)

        elif c=="2":
            print("Result of",a,"-",b,"=", a-b)

        elif c=="3":
            print("Result of",a,"*",b,"=",a*b)


        elif c=="4":
            print("Result of",a,"/",b,"=",a/b)


    else:

        print("!!!!!!! Invalid Option chosen :( !!!!!!!")
        x = input("do you want to run calculator again(y OR n)")
        if x!="y":
            print("You decided to leave the Calculator, See you Again :)")
            break
