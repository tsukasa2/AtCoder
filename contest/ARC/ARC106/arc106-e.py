N, K = map( int, input().split() )
A = list( map( int, input().split() ) )

# ans = N * K
# for d in range( N * K ):
#     for e in range( N ):
#         if ( d // A[ e ] ) % 2 == 0:
#             break
#     else:
#         ans += 1

# print( ans )

rest = N * K
d = 0
while rest > 0:
    for e in range( N ):
        if ( d // A[ e ] ) % 2 == 0:
            rest -= 1
            break
    d += 1

print( d )