n = str( input() )

ans = 0
for c in n:
    ans += int( c )
    ans = ans % 9

if ans == 0:
    print( "Yes" )
else:
    print( "No" )