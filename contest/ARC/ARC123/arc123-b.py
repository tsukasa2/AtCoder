N = int( input() )
A = list( map( int, input().split() ) )
B = list( map( int, input().split() ) )
C = list( map( int, input().split() ) )

A.sort()
B.sort()
C.sort()

new_B = []
i = 0
j = 0
while j < N:
    if A[ i ] < B[ j ]:
        new_B.append( B[ j ] )
        i += 1
        j += 1
    else:
        j += 1

M = i
new_C = []
i = 0
j = 0
while j < N and i < M:
    if new_B[ i ] < C[ j ]:
        new_C.append( C[ j ] )
        i += 1
        j += 1
    else:
        j += 1

print( len( new_C ) )