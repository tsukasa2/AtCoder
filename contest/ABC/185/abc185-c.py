L = int( input() )

ans = 1
for i in range( 11 ):
    ans = ans * ( L - 1 - i )

for i in range( 11 ):
    ans = ans // ( i + 1 )

print( ans )