currencyNames=["USD", "Pound", "Yen", "Ksh", "Ush", "Rand", "Rupee"]
while True:
    print("Welcome to Hella Convertion")
    print("Your Genuine and best Offer convertion Company")
    print("CURRENY TYPES TODAY")
    
    print("1.  USD")
    print("2. Pound")
    print("3. Japanese Yen")
    print("4. Indian Rupee")
    print( "5. Ugandan Shilling")
    print("6. South African Rand")
    
    
    print("Input the Currency type you would like to convert to Ksh")
    currencytype=str(input())
    if currencytype=="1":
        print("1USD is equal to 120Ksh")
        print("Please insert the amount you would wish to convert: ")
        x=int(input())
        y=x*120
        print("Your Converted Currency is Ksh", +y)
    elif currencytype=="2":
        print("1 Pound is equal to 140Ksh")
        print("Please insert the amount you would wish to convert: ")
        p=int(input())
        a=x*120
        print("Your Converted Currency is KSh", +a)
    elif currencytype=="3":
        print("1 Japanese Yen is equal to 140Ksh")
        print("Please insert the amount you would wish to convert: ")
        v=int(input())
        b=v*17
        print("Your Converted Currency is Ksh", +b)
    elif currencytype=="4":
        print("1 Indian Rupee is equal to 1.2Ksh")
        print("Please insert the amount you would wish to convert: ")
        i=int(input())
        c=i*1.2
        print("Your Converted Currency is Ksh", +c)
    elif currencytype=="5":
        print("1 Kenyan Shilling is equal to 33 Ugsh")
        print("Please insert the amount you would wish to convert: ")
        w=int(input())
        d=w/33
        print("Your Converted Currency is Ksh", +d)
    elif currencytype=="6":
        print("1 South African Rand is equal to 8Ksh")
        print("Please insert the amount you would wish to convert: ")
        o=int(input())
        e=o*8
        print("Your Converted Currency is Ksh", +e)
    else:
        print("Invalid Option Try Again!")

        