S = str( input() )

ans = 0
for i in range( 9 ):
    if S[ i : i + 4 ] == "ZONe":
        ans += 1

print( ans )