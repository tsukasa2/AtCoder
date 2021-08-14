S = str( input() )

ans = 0
ans_cand = 0
for c in S:
    if c in "ACGT":
        ans_cand += 1
        ans = max( ans, ans_cand )
    else:
        ans_cand = 0

print( ans )