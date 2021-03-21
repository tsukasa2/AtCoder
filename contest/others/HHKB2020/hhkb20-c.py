n = int( input() )
p = list( map( int, input().split() ) )

visited_p = [ 0 for _ in range( 200001 ) ]

ans_i = 0
for i in range( n ):
    visited_p[ p[ i ] ] += 1
    while visited_p[ ans_i ] > 0 and ans_i < 200001:
        ans_i += 1
    print( ans_i )