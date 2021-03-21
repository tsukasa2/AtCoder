N, L = map( int, input().split() )

sum_taste = 0
for i in range( N ):
    sum_taste += L + i

if L + 1 - 1 > 0:
    print( sum_taste - ( L + 1 - 1 ) )
elif L + N - 1 < 0:
    print( sum_taste - ( L + N - 1 ) )
else:
    print( sum_taste )