N, K = map( int, input().split() )
a = list( map( int, input().split() ) )
a.append( 4 * ( 10 ** 5 ) )

count_dict = {}
for a_i in a:
    try:
        count_dict[ a_i ] += 1
    except KeyError:
        count_dict[ a_i ] = 1

count_list = []
for a_i in count_dict.keys():
    count_list.append( ( a_i, count_dict[ a_i ] ) )

count_list.sort()

min_count = K
x_cur = 0
prev_a = -1
ans = 0
for a_i, c_i in count_list:
    if a_i > prev_a + 1:
        ans += x_cur * min_count
        break
    if c_i < min_count:
        ans += x_cur * ( min_count - c_i )
        min_count = c_i
    prev_a = a_i
    x_cur += 1


print( ans )