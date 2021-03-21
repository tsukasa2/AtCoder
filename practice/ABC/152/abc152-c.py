n = int( input() )
p = list( map( int, input().split() ) )

min_p = 2 * ( 10 ** 5 )
cnt = 0

for p_i in p:
    if min_p >= p_i:
        min_p = p_i
        cnt += 1

print( cnt )