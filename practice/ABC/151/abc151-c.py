n, m = map( int, input().split() )
p = []
s = []
for _ in range( m ):
    p_i, s_i = input().split()
    p.append( int( p_i ) )
    s.append( str( s_i ) )

aced = [ False for _ in range( n ) ]
wa_cnt = [ 0 for _ in range( n ) ]

for i in range( m ):
    if s[ i ] == "AC":
        aced[ p[ i ] - 1 ] = True
    elif aced[ p[ i ] - 1 ] == False:
        wa_cnt[ p[ i ] - 1 ] += 1

ac_cnt = 0
penalty = 0

for i in range( n ):
    if aced[ i ] == True:
        ac_cnt += 1
        penalty += wa_cnt[ i ]

print( ac_cnt, penalty )