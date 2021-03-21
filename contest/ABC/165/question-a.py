k = int( input() )
a, b = input().split()
a = int( a )
b = int( b )

flag = 0

for n in range( a, b+1 ):
    if n % k == 0:
        flag = 1

if flag == 1:
    print("OK")
else:
    print("NG")