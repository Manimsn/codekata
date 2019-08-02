x = 2000

if(x%4 == 0):
    if(x%100 == 0):
        if(x%400 ==0 ):
            print("Leap Year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap yer")
