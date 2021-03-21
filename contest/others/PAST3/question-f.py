n = int( input() )
a = []
for _ in range( n ):
    a_i = str( input() )
    a.append( a_i )

s = ""
for i in range( n//2 ):
    found = 0
    for j in range( n ):
        if a[i][j] in a[n-i-1]:
            s = s + str( a[i][j] )
            found = 1
            break
    if found == 0:
        print( -1 )
        exit()

if n % 2 == 0:
    print( s + s[::-1] )
else:
    print( s + str( a[ n//2 ][0] ) + s[::-1] )
