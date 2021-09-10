L, Q = map( int, input().split() )
Query = [ tuple( map( int, input().split() ) ) for _ in range( Q ) ]

from bisect import bisect_left, insort_left
import array

lst = array.array( "i", [ 0, L ] )
for c, x in Query:
    if c == 1:
        insort_left( lst, x )
    else:
        i = bisect_left( lst, x )
        print( lst[ i ] - lst[ i - 1 ] )