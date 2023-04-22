def build_way():
    global height, width, g

    sx1 = x1_field.get()
    sy1 = y1_field.get()
    sx2 = x2_field.get()
    sy2 = y2_field.get()

    if not(sx1.isnumeric() and sx2.isnumeric() and sy1.isnumeric() and sy2.isnumeric()):
        mb.showerror("Error", "Сell coordinates must be natural numbers")
        return

    x1 = int(sx1)-1
    y1 = int(sy1)-1
    x2 = int(sx2)-1
    y2 = int(sy2)-1

    if not (x1 >= 0 and x2 >= 0 and y1 >= 0 and y2 >= 0):
        mb.showerror("Error", "Сell coordinates must be natural numbers")
        return
    if not (x1 < width and y1 < height and x2 < width and y2 < height):
        mb.showerror("Error", "Сoordinates exceed maze dimensions")
        return


    s = y1*width+x1
    f = y2*width+x2

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
    print(way)
    paint(way)

def replace(a, b, vect):
    for i in range(len(vect)):
        if vect[i] == a:
            vect[i] = b
