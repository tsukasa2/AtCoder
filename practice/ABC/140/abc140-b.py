N = int( input() )
A = list( map( int, input().split() ) )
B = list( map( int, input().split() ) )
C = list( map( int, input().split() ) )

satisfied = 0

for i in range( N ):
    satisfied += B[ A[ i ] - 1 ]

for i in range( N - 1 ):
    if A[ i ] + 1 == A[ i + 1 ]:
        satisfied += C[ A[ i ] - 1 ]

print( satisfied )