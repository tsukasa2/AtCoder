n, m = map( int, input().split() )
a = list( map( int, input().split() ) )

best_sushi = [ 0 ] * n
ans = [ -1 ] * m

max_n = 10 ** 5
sushi_cnt = [ 0 ] * ( max_n + 1 )

for sushi in a:
    sushi_cnt[ sushi ] += 1

sum_sushi
