import copy
n, m, x = map( int, input().split() )
c = [ 0 ]
a = [[]]
for _ in range( n ):
    line = input().split()
    c = c + [ int( line[0] ) ]
    a = a + [ [ 0 ] + list( map( int, line[1:] ) ) ]

#print( n, m, x, c, a )

def search( understood, money, i ):
    if i > n:
        #print( understood )
        for j in range( 1, m+1 ):
            if understood[j] < x:
                return
        sum_money.append( money )
        return money
    else:
        search( understood, money, i+1 )
        next_understood = copy.deepcopy( understood )
        for j in range( 1, m + 1 ):
            next_understood[j] += a[i][j]
        next_money = money + c[i]
        search( next_understood, next_money, i+1 )

understood = [ 0 ] * ( m + 1 )
sum_money = []
search( understood, 0, 1 )
#sum_money.append( search( understood, 0, 1 ) )

try:
    print( min( sum_money ) )
except ValueError:
    print( "-1" )