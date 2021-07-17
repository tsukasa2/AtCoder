N = int( input() )
s = [ str( input() ) for _ in range( N ) ]

connect = {}
for w in s:
    try:
        connect[ w[ : 3 ] ].append( w[ -3 : ] )
    except KeyError:
        connect[ w[ : 3 ] ] = [ w[ -3 : ] ]
    
    if not w[ -3 : ] in connect.keys():
        connect[ w[ -3 : ] ] = []

ans = { v : "" for v in connect.keys() }
visited = { v : False for v in connect.keys() }
def dfs( v ):
    if visited[ v ] == True:
        # if ans[ v ] == "":
        #     ans[ v ] = "Draw"
        return "Draw"
    else:
        visited[ v ] = True
        ans_v = "Takahashi"
        for u in connect[ v ]:
            ans_u = dfs( u )
            if ans_u == "Takahashi":
                ans_v = "Aoki"
            elif ans_u == "Draw":
                if ans_v == "Takahashi":
                    ans_v = "Draw"
        
        ans[ v ] = ans_v
        return ans_v

for v in connect.keys():
    dfs( v )

for w in s:
    print( ans[ w[ -3 : ] ] )
