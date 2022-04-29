n=21
guess_count=1
print("no. of count is 6")
while (guess_count<=6) :
    gn = int(input("enter a number /n"))
    if gn>21:
        print("Decrease the value")
    elif gn<21:
        print("Increase the value")
    else:
        print("You guessed it right")  
        break
    print(6-guess_count,"attempts left")
    guess_count = guess_count + 1

if (guess_count>6):
    print("Too many wrong attempts, try again")
