y = 3
try:
    x = int(y)
    if(x/2==0):
        print("Even")
    elif(x/2!=0):
        print("odd")
except ValueError:
    print("invalid")
