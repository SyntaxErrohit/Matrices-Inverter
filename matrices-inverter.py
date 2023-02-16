def d2(m):
    return m[0]*m[3] - m[1]*m[2]

def invert(m):
    adj = [[0]*3, [0]*3, [0]*3]
    sign = 1
    n = len(m)
    for imain in range(n):
        for jmain in range(n):
            l = []
            for i in range(n):
                for j in range(n):
                    if i != imain and j != jmain:
                        l.append(m[i][j])
            adj[jmain][imain] = d2(l)*sign
            sign *= -1
    print(*adj, sep='\n')
        

a = [[3, -3, 4], [2, -3, 4], [0, -1, 1]]
invert(a)