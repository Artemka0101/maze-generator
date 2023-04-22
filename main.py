import random
import numpy as np
import cv2
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as mb
from collections import deque
from datetime import datetime

use_count = 0
img = []
line_size = 0
square_size = 0
img_h = 0
img_w = 0
maze_img = []
g = []
x_nums = []
y_nums = []
x_img = 0
y_img = 0
height = 0
width = 0


def file_write():
    file_name = str(datetime.now().date())+"-"+str(datetime.now().hour)+str(datetime.now().minute)+str(datetime.now().second)+".maze"
    file = open(file_name, 'wb+')
    bt = ("IHATEPYTHON!"+'\n').encode()
    file.write(bt)
    bt = (str(height)+'\n').encode()
    file.write(bt)
    bt = (str(width) + "\n").encode()
    file.write(bt)
    for i in range(len(g)):
        for j in range(len(g[i])):
            bt = (str(g[i][j])+"\n").encode()
            file.write(bt)
        bt = (str(-1) + "\n").encode()
        file.write(bt)
    bt = (str(-2) + "\n").encode()
    file.write(bt)


def file_read():
    global g, height, width

    filepath = filedialog.askopenfilename()
    file = open(filepath, 'rb')

    signature = file.read(12)
    if signature != "IHATEPYTHON!".encode():
        mb.showerror("Error", 'Selected file is not a maze (the extension must be ".maze")')
        return

    data = file.read()
    data = data.decode().split('\n')
    #print(data)

    data.pop(0)
    height = int(data[0])
    width = int(data[1])
    print(height, width)
    for i in range(2):
        data.pop(0)

    #print(data)
    data.pop(len(data)-1)

    g = [[]]
    for i in range(len(data)):
        if data[i] == '-1':
            g.append(list())
        else:
            g[len(g)-1].append(int(data[i]))
    #print(g)

    image()


def gen_click():
    global g, height, width

    height = int(height_field.get())
    width = int(width_field.get())

    #print(height, width)

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
    global use_count
    use_count += 1


def paint(way):
    global x_img, y_img, height, width
    image()
    center_size = square_size//6
    for q in range(len(way)):
        x = way[q] % width
        y = way[q]//width
        lg = (line_size+square_size)*x
        rg = lg+square_size+line_size+1
        hg = (line_size+square_size)*y
        bg = hg+square_size+line_size+1
        cx = (lg+rg)//2
        cy = (bg+hg)//2

        for i in range(cy-center_size//2, cy+center_size//2):
            for j in range(cx - center_size // 2, cx + center_size // 2):
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
            for i in range(lh_y, rb_y):
                for j in range(lh_x, rb_x):
                    img[i][j] = [0, 255, 0]

        else:
            lh_y = min(cy1 - center_size // 2, cy2 - center_size // 2)
            lh_x = cx2 - center_size // 2
            rb_y = max(cy1 - center_size // 2, cy2 - center_size // 2)
            rb_x = cx2 + center_size // 2
            for i in range(lh_y, rb_y):
                for j in range(lh_x, rb_x):
                    img[i][j] = [0, 255, 0]

    cv2.imwrite("C:/Users/user/PycharmProjects/labirint/maze.png", img)
    h_image = PhotoImage(file="C:/Users/user/PycharmProjects/labirint/maze.png")
    global maze_img
    maze_img.image = h_image
    maze_img['image'] = maze_img.image
    maze_img.place(x=x_img, y=y_img)



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

window = Tk()
window.title("Maze generator")
window.geometry("700x500")

maze_img = Label(window)

dy = 40
dx = 13

width_text = Label(window, text="Width: ")
width_text.grid(column=0, row=0, pady=10)

width_field = Entry(window, width=10)
width_field.grid(column=1, row=0)

height_text = Label(window, text="Height: ")
height_text.grid(column=0, row=1, pady=0)

height_field = Entry(window, width=10)
height_field.grid(column=1, row=1)

gen_button = Button(window, text="Generate!", command=gen_click, width=14)
gen_button.place(x=1, y=72)

build_text = Label(text="BUILD A WAY")
build_text.place(x=1, y=122)

point1_text = Label(text="Point 1")
point1_text.place(x=1, y=142)

x1_text = Label(text="x:")
x1_text.place(x=1, y=162)

x1_field = Entry(window, width=4)
x1_field.place(x=16, y=162)

y1_text = Label(text="y:")
y1_text.place(x=50+dx, y=162)

y1_field = Entry(window, width=4)
y1_field.place(x=66+dx, y=162)

point2_text = Label(text="Point 2")
point2_text.place(x=1, y=142+dy)

x2_text = Label(text="x:")
x2_text.place(x=1, y=162+dy)

x2_field = Entry(window, width=4)
x2_field.place(x=16, y=162+dy)

y2_text = Label(text="y:")
y2_text.place(x=50+dx, y=162+dy)

y2_field = Entry(window, width=4)
y2_field.place(x=66+dx, y=162+dy)

way_button = Button(text="Build", command=build_way, width=14)
way_button.place(x=1, y=230)

save_button = Button(text="Save", command=file_write, width=14)
save_button.place(x=1, y=290)

import_button = Button(text="Import", command=file_read, width=14)
import_button.place(x=1, y=330)

#x1_field = Entry(window, text=)

def replace(a, b, vect):
    for i in range(len(vect)):
        if vect[i] == a:
            vect[i] = b


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

    cv2.imwrite("C:/Users/user/PycharmProjects/labirint/maze.png", img)
    h_image = PhotoImage(file="C:/Users/user/PycharmProjects/labirint/maze.png")
    global maze_img
    maze_img.image = h_image
    maze_img['image'] = maze_img.image
    maze_img.place(x=x_img, y=y_img)

    return img


window.mainloop()

