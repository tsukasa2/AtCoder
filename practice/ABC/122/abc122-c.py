N, Q = map( int, input().split() )
S = str( input() )
lr = [ tuple( map( int, input().split() ) ) for _ in range( Q ) ]

ruisekiwa = [ 0 ]
c_prev = S[ 0 ]
AC = 0
for c in S[ 1 : ]:
    if c_prev == "A" and c == "C":
        AC += 1
    
    ruisekiwa.append( AC )
    c_prev = c

for ( l, r ) in lr:
    print( ruisekiwa[ r - 1 ] - ruisekiwa[ l - 1 ] )