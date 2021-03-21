n = int( input() )

while n > 0:
    if n%10 == 7:
        print("Yes")
        exit()
    else:
        n = int( n / 10 )

print("No")