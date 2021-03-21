s = [ str( input() ) ]
q = int( input() )
query = []
rev_flag_k = 0
for _ in range( q ):
    query_i = list( input().split() )
    query.append( query_i )
    if query_i[ 0 ] == "1":
        rev_flag_k += 1

top = []
rev_flag = 0
for query_i in query:
    t = query_i[ 0 ]
    if t == "1":
        rev_flag += 1
    else:
        f = query_i[ 1 ]
        c = query_i[ 2 ]
        if f == "1" and rev_flag % 2 == 1:
            s.append( str( c ) )
        elif f == "2" and rev_flag % 2 == 0:
            s.append( str( c ) )
        else:
            top.append( str( c ) )
s = "".join( top )[::-1] + "".join( s )
if rev_flag_k % 2 == 1:
    s = s[::-1]

print( s )