s = str( input() )

n = len( s )
s_l = s[:(n-1)//2]
s_r = s[(n+1)//2:]

if s == s[::-1] and s_l == s_l[::-1] and s_r == s_r[::-1]:
    print("Yes")
else:
    print("No")