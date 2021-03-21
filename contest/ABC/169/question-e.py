import statistics
n = int( input() )
a = []
b = []
for _ in range( n ):
    a_i, b_i = map( int, input().split() )
    a.append( a_i )
    b.append( b_i )

m_a = statistics.median( a )
m_b = statistics.median( b )

if n % 2 == 1:
    print( int( m_b - m_a + 1 ) )
else:
    print( int( ( m_b - m_a ) * 2 + 1 ) )