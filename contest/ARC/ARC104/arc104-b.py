# raw_in = input().split()
# n = int( raw_in[ 0 ] )
# s = raw_in[ 1 ]

# a, t, g, c = [ 0 ], [ 0 ], [ 0 ], [ 0 ]

# for x in s:
#     if x == "A":
#         a.append( a[ -1 ] + 1 )
#         t.append( t[ -1 ] )
#         g.append( g[ -1 ] )
#         c.append( c[ -1 ] )
#     elif x == "T":
#         a.append( a[ -1 ] )
#         t.append( t[ -1 ] + 1 )
#         g.append( g[ -1 ] )
#         c.append( c[ -1 ] )
#     elif x == "G":
#         a.append( a[ -1 ] )
#         t.append( t[ -1 ] )
#         g.append( g[ -1 ] + 1 )
#         c.append( c[ -1 ] )
#     elif x == "C":
#         a.append( a[ -1 ] )
#         t.append( t[ -1 ] )
#         g.append( g[ -1 ] )
#         c.append( c[ -1 ] + 1 )

# # print( a, t, c, g )

# ans = 0

# for i in range( n + 1 ):
#     for j in range( i ):
#         # print( i, j, a[ i ], t[ i ], g[ j ], c[ j ] )
#         if a[ i ] - a[ j ] == t[ i ] - t[ j ]:
#             if g[ i ] - g[ j ] == c[ i ] - c[ j ]:
#                 ans += 1
#                 # print( i, j )

# print( ans )

raw_in = input().split()
n = int( raw_in[ 0 ] )
s = raw_in[ 1 ]

at, gc = [ 0 ], [ 0 ]

for x in s:
    if x == "A":
        at.append( at[ -1 ] + 1 )
        gc.append( gc[ -1 ] )
    elif x == "T":
        at.append( at[ -1 ] - 1 )
        gc.append( gc[ -1 ] )
    elif x == "G":
        at.append( at[ -1 ] )
        gc.append( gc[ -1 ] + 1 )
    elif x == "C":
        at.append( at[ -1 ] )
        gc.append( gc[ -1 ] - 1 )

# print( at )
# print( gc )

ans = 0

for i in range( n + 1 ):
    for j in range( i ):
        # print( i, j, a[ i ], t[ i ], g[ j ], c[ j ] )
        if at[ i ] == at[ j ] and gc[ i ] == gc[ j ]:
                ans += 1
                # print( i, j )

print( ans )