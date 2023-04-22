def file_read():
    global g
    global height
    global width

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
