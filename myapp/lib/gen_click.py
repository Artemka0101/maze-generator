def gen_click():
    global g, height, width

    height = int(height_field.get())
    width = int(width_field.get())


    g = [[] for i in range(width * height)]
    component = [i for i in range(width * height)]
    count_comp = height * width

    while count_comp > 1:
        ux = random.randint(0, width - 1)
        uy = random.randint(0, height - 1)

        dx = 0
        dy = 0

        t = random.randint(0, 1)
        if t == 0:
            dx = random.choice([-1, 1])
        else:
            dy = random.choice([-1, 1])

        vx = ux + dx
        vy = uy + dy

        #print(ux, uy)
        #print(vx, vy)
        #print()

        if vx>=0 and vy>=0 and vy<height and vx<width and component[uy * width + ux] != component[vy * width + vx]:
            replace(component[uy * width + ux], component[vy * width + vx], component)
            g[uy * width + ux].append(vy*width+vx)
            g[vy * width + vx].append(uy*width+ux)
            count_comp -= 1
    image()
