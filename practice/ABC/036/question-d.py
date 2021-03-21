MOD = 10 ** 9 + 7
n = int( input() )
adj_list = [ [] for _ in range( n ) ]
for _ in range( n - 1 ):
    a, b = map( int, input().split() )
    adj_list[ a - 1 ].append( b - 1 )
    adj_list[ b - 1 ].append( a - 1 )

def treedp( vertex, prev_v=None ):
    # input     : 根となる頂点の番号
    # output    : 根を白としたときの塗り分け方，根を黒としたときの塗り分け方
    w = 1
    b = 1
    for next_v in adj_list[ vertex ]:
        if next_v == prev_v:
            continue
        w_i, b_i = treedp( next_v, vertex )
        w *= ( w_i + b_i )
        w = w % MOD
        b *= w_i
        b = b % MOD
    return w, b

w, b = treedp( 0 )
print( ( w + b ) % MOD )