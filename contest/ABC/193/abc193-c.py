N = int( input() )

found = {}
ans = N
root_N = int( N ** 0.5 )
for i in range( 2, root_N + 1 ):
    if i in found.keys():
        continue
    j = i * i
    while j <= N:
        if i in found.keys():
            continue
        found[ j ] = 1
        j *= i
        ans -= 1

print( ans )