# n = int( input() )
# alphabet = [chr(i) for i in range(97, 97+26)]

# conv = []
# k = n - 1
# while True:
#     conv.append( k % 26 )
#     k = k // 26
#     if k == 0:
#         break

# ans = []
# for c in conv:
#     ans.append( alphabet[ c ] )

# print( "".join( reversed( ans ) ) )

n = int( input() )
bound = [ 26 ]
add = 26
while bound[ -1 ] < 1000000000000001:
    add *= 26
    bound.append( add + bound[ -1 ] )

d = 0
while bound[ d ] < n:
    d += 1

k = n - bound[ d - 1 ] - 1

alphabet = [chr(i) for i in range(97, 97+26)]
conv = []
for _ in range( d + 1 ):
    conv.append( k % 26 )
    k = k // 26

ans = []
for c in conv:
    ans.append( alphabet[ c ] )

print( "".join( reversed( ans[ : d + 1 ] ) ) )