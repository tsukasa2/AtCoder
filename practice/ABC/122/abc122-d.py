N = int( input() )
MOD = 10 ** 9 + 7

from collections import Counter
DP = [ Counter() for _ in range( 101 ) ]
for x in "ATGC":
    for y in "ATGC":
        for z in "ATGC":
            DP[ 3 ][ x + y + z ] = 1
DP[ 3 ][ "AGC" ], DP[ 3 ][ "GAC" ], DP[ 3 ][ "ACG" ] = 0, 0, 0
# DP[ i ][ s ] = 条件を満たすi文字の文字列のうち，後ろの3文字がsであるものの数

for i in range( 4, 101 ):
    for x in "ATGC":
        for y in "ATGC":
            for z in "ATGC":
                DP_xyz = DP[ i - 1 ][ x + y + z ]
                if y + z == "AG" or y + z == "GA":
                    # AGC，GACを除去
                    for w in "ATG":
                        DP[ i ][ y + z + w ] += DP_xyz
                        DP[ i ][ y + z + w ] %= MOD
                
                elif y + z == "AC":
                    # ACGを除去
                    for w in "ATC":
                        DP[ i ][ y + z + w ] += DP_xyz
                        DP[ i ][ y + z + w ] %= MOD
                
                elif x + y + z in [ "ATG", "AGG", "AGT" ]:
                    # ATGC，AGGC，AGTCを除去
                    for w in "ATG":
                        DP[ i ][ y + z + w ] += DP_xyz
                        DP[ i ][ y + z + w ] %= MOD
                
                else:
                    for w in "ATGC":
                        DP[ i ][ y + z + w ] += DP_xyz
                        DP[ i ][ y + z + w ] %= MOD

ans = 0
for v in DP[ N ].values():
    ans += v
    ans %= MOD
    
print( ans )