a, b, c, d = input().split()
a = int( a )
b = int( b )
c = int( c )
d = int( d )

while a > 0 and c > 0:
    c = c - b
    if c <= 0:
        print("Yes")
        exit()
    a = a - d
    if a <= 0:
        print("No")
        exit()
