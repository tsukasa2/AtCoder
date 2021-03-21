N, C = map( int, input().split() )
services = [ ( map( int, input().split() ) ) for _ in range( N ) ]

d_cost_dic = {}

for ( a, b, c ) in services:
    try:
        d_cost_dic[ a ] += c
    except KeyError:
        d_cost_dic[ a ] = c
    try:
        d_cost_dic[ b + 1 ] += -c
    except KeyError:
        d_cost_dic[ b + 1 ] = -c

d_cost = []
for day in d_cost_dic.keys():
    d_cost.append( ( day, d_cost_dic[ day ] ) )
d_cost.sort()

cost = 0
pay = 0
for i in range( len( d_cost ) - 1 ):
    day, d_pay = d_cost[ i ]
    next_day, _ = d_cost[ i + 1 ]
    pay += d_pay
    cost += ( next_day - day ) * min( C, pay )

print( cost )