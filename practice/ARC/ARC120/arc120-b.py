H, W = map( int, input().split() )
S = [ str( input() ) for _ in range( H ) ]

MOD = 998244353

# RBBRB
# BBRBR
# BRBRR
# RBRRB
# BRRBB
# こんな感じでy=xのグループを同色にする方法を数える

from collections import Counter
naname = [ Counter() for _ in range( H + W - 1 ) ]

for i in range( H ):
    for j in range( W ):
        naname[ i + j ][ S[ i ][ j ] ] += 1

ans = 1
for n in naname:
    if n[ "R" ] == 0 and n[ "B" ] == 0:
        ans *= 2
        ans %= MOD
    elif n[ "R" ] > 0 and n[ "B" ] > 0:
        ans *= 0

print( ans )