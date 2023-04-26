def image():
    global img, line_size, square_size, img_h, img_w, x_img, y_img, height, width, g

   # for i in range(len(x_nums)):
       # x_nums[i].

    x_img = 150
    y_img = 20

    square_size = 400//max(height, width)
    line_size = square_size//10

    img_h = height*square_size+line_size*(height-1)
    img_w = width*square_size+line_size*(width-1)

    img = np.zeros((img_h, img_w, 3))
    for i in range(img_h):
        for j in range(img_w):
            img[i][j] = [255, 255, 255]

    for i in range(height):
        for j in range(width):
            if (i != height-1) and (not (i*width+j+width in g[i*width+j])):
                posy = (square_size+line_size)*(i+1)
                posx1 = (square_size+line_size)*j
                posx2 = (square_size+line_size)*j+square_size-1
                for pos in range(posx1, min(posx2+line_size+1, img_w)):
                    img[posy][pos] = [0, 0, 0]

            if (j != width-1) and (not (i*width+j+1 in g[i*width+j])):
                posy1 = (square_size+line_size)*i
                posy2 = (square_size+line_size)*i+square_size-1
                posx = (square_size+line_size)*(j+1)
                for pos in range(posy1, min(posy2+line_size+1, img_h)):
                    img[pos][posx] = [0, 0, 0]

    cv2.imwrite("data/maze.png", img)
    h_image = PhotoImage(file="data/maze.png")
    global maze_img
    maze_img.image = h_image
    maze_img['image'] = maze_img.image
    maze_img.place(x=x_img, y=y_img)
    return img
