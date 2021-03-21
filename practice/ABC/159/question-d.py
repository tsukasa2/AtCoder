n = int( input() )
a = list( map( int, input().split() ) )

cnt = [ 0 ] + [ 0 ] * n

for a_i in  a:
    cnt[a_i] += 1

all_combi = 0
for m in cnt:
    all_combi += m * ( m - 1 ) // 2

for k in range( 1, n+1 ):
    print( all_combi - ( cnt[a[k-1]] - 1 ) )