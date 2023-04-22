def file_write():
    if g == []:
        mb.showerror("Error", "Before saving, first generate the maze")

    file_name = "data\maze"+str(datetime.now().date())+"-"+str(datetime.now().hour)+str(datetime.now().minute)+str(datetime.now().second)+".maze"
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
