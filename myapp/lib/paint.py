def paint(way):
    global x_img, y_img, height, width
    image()
    center_size = max(square_size//6, 1)
    for q in range(len(way)):
        x = way[q] % width
        y = way[q]//width
        lg = (line_size+square_size)*x
        rg = lg+square_size+line_size+1
        hg = (line_size+square_size)*y
        bg = hg+square_size+line_size+1
        cx = (lg+rg)//2
        cy = (bg+hg)//2

        for i in range(cy-center_size//2, cy+center_size//2+1):
            for j in range(cx - center_size // 2, cx + center_size // 2 +1):
                img[i][j] = [0, 255, 0]

    for q in range(len(way)-1):
        x1 = way[q] % width
        y1 = way[q] // width
        lg1 = (line_size + square_size) * x1
        rg1 = lg1 + square_size + line_size + 1
        hg1 = (line_size + square_size) * y1
        bg1 = hg1 + square_size + line_size + 1
        cx1 = (lg1 + rg1) // 2
        cy1 = (bg1 + hg1) // 2

        x2 = way[q+1] % width
        y2 = way[q+1] // width
        lg2 = (line_size + square_size) * x2
        rg2 = lg2 + square_size + line_size + 1
        hg2 = (line_size + square_size) * y2
        bg2 = hg2 + square_size + line_size + 1
        cx2 = (lg2 + rg2) // 2
        cy2 = (bg2 + hg2) // 2

        if y1 == y2:
            lh_x = min(cx1 - center_size // 2, cx2 - center_size//2)
            lh_y = cy2 - center_size // 2
            rb_x = max(cx1 - center_size // 2, cx2 - center_size//2)
            rb_y = cy2 + center_size // 2
            for i in range(lh_y, rb_y+1):
                for j in range(lh_x, rb_x+1):
                    img[i][j] = [0, 255, 0]

        else:
            lh_y = min(cy1 - center_size // 2, cy2 - center_size // 2)
            lh_x = cx2 - center_size // 2
            rb_y = max(cy1 - center_size // 2, cy2 - center_size // 2)
            rb_x = cx2 + center_size // 2
            for i in range(lh_y, rb_y+1):
                for j in range(lh_x, rb_x+1):
                    img[i][j] = [0, 255, 0]

    cv2.imwrite("data/maze.png", img)
    h_image = PhotoImage(file="data/maze.png")
    global maze_img
    maze_img.image = h_image
    maze_img['image'] = maze_img.image
    maze_img.place(x=x_img, y=y_img)
