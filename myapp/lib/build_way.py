def build_way():
    global height, width
    x1 = int(x1_field.get())-1
    y1 = int(y1_field.get())-1
    x2 = int(x2_field.get())-1
    y2 = int(y2_field.get())-1

    s = y1*height+x1
    f = y2*height+x2

    q = deque()
    cnt = 0
    q.append(s)
    cnt += 1
    used = [False]*(height*width)
    d = [-1]*(height*width)
    p = [-1]*(height*width)
    used[s] = True
    p[s] = -1

    while cnt > 0:
        v = q[0]
        q.popleft()
        cnt -= 1
        for i in range(len(g[v])):
            u = g[v][i]
            if not used[u]:
                used[u] = True
                q.append(u)
                cnt += 1
                d[u] = d[v]+1
                p[u] = v

    way = []
    c = f
    while c != s:
        way.append(c)
        c = p[c]
    way.append(s)
    paint(way)
