n = int( input() )
s = list( input() )
r = []
g = []
b = []

for i in range(n):
    if s[i] == "R":
        r.append(i)
    elif s[i] == "G":
        g.append(i)
    elif s[i] == "B":
        b.append(i) 

cnt = 0
for i in range(n - 2):
    for k in range(i + 2, n):
        if ( i + k ) % 2 != 0:
            continue
        j = ( i + k ) // 2
        if s[i]!=s[j] and s[j]!=s[k] and s[k]!=s[i]:
            cnt += 1

print( len(r) * len(g) * len(b) - cnt )