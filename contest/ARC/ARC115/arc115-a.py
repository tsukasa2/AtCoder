N, M = map( int, input().split() )
S = [ str( input() ) for _ in range( N ) ]

odd = 0
even = 0

for s in S:
    sum_s = sum( map( int, s ) )
    if sum_s % 2 == 0:
        even += 1
    else:
        odd += 1

print( even * odd )