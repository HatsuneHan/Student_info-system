from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageTk
from client import *


def hello(ui):
    ui.delete(0, 'end')  # 清空文本框
    ui.select_clear()
    ui.insert(0, "123213")  # 插入值


def upload_file(ui):
    # askopenfilename 1次上传1个；askopenfilenames1次上传多个
    selectFile = tkinter.filedialog.askopenfilename()
    ui.delete(0, 'end')
    ui.insert(0, selectFile)


def load_pic(ui, path1, path2, path3, path4):
    try:
        ui.img_st.destroy()
        ui.img_nd.destroy()
        ui.img_rd.destroy()
        ui.img_th.destroy()
    except:
        pass
    load_st = Image.open(path1)
    load_st = load_st.resize((50, 70))
    render_st = ImageTk.PhotoImage(load_st)
    ui.img_st = Label(ui.fm2_left_st, image=render_st)
    ui.img_st.image = render_st

    load_nd = Image.open(path2)
    load_nd = load_nd.resize((50, 70))
    render_nd = ImageTk.PhotoImage(load_nd)
    ui.img_nd = Label(ui.fm2_left_nd, image=render_nd)
    ui.img_nd.image = render_nd

    load_rd = Image.open(path3)
    load_rd = load_rd.resize((50, 70))
    render_rd = ImageTk.PhotoImage(load_rd)
    ui.img_rd = Label(ui.fm2_left_rd, image=render_rd)
    ui.img_rd.image = render_rd

    load_th = Image.open(path4)
    load_th = load_th.resize((50, 70))
    render_th = ImageTk.PhotoImage(load_th)
    ui.img_th = Label(ui.fm2_left_th, image=render_th)
    ui.img_th.image = render_th

    ui.img_st.pack(ipadx=50, ipady=5)
    ui.img_nd.pack(ipadx=50, ipady=5)
    ui.img_rd.pack(ipadx=50, ipady=5)
    ui.img_th.pack(ipadx=50, ipady=5)


def load_id(ui, id1, id2, id3, id4):
    try:
        ui.idlabel_st.destroy()
        ui.idlabel_nd.destroy()
        ui.idlabel_rd.destroy()
        ui.idlabel_th.destroy()
    except:
        pass
    ui.idlabel_st = Label(ui.fm2_right_st_top,
                          text=id1, font=("Arial", 12))
    ui.idlabel_nd = Label(ui.fm2_right_nd_top,
                          text=id2, font=("Arial", 12))
    ui.idlabel_rd = Label(ui.fm2_right_rd_top,
                          text=id3, font=("Arial", 12))
    ui.idlabel_th = Label(ui.fm2_right_th_top,
                          text=id4, font=("Arial", 12))
    ui.idlabel_st.pack(ipadx=10, ipady=10)
    ui.idlabel_nd.pack(ipadx=10, ipady=10)
    ui.idlabel_rd.pack(ipadx=10, ipady=10)
    ui.idlabel_th.pack(ipadx=10, ipady=10)


def load_name(ui, name1, name2, name3, name4):
    try:
        ui.namelabel_st.destroy()
        ui.namelabel_nd.destroy()
        ui.namelabel_rd.destroy()
        ui.namelabel_th.destroy()
    except:
        pass
    ui.namelabel_st = Label(ui.fm2_right_st_btm,
                            text=name1, font=("Arial", 12))
    ui.namelabel_nd = Label(ui.fm2_right_nd_btm,
                            text=name2, font=("Arial", 12))
    ui.namelabel_rd = Label(ui.fm2_right_rd_btm,
                            text=name3, font=("Arial", 12))
    ui.namelabel_th = Label(ui.fm2_right_th_btm,
                            text=name4, font=("Arial", 12))

    ui.namelabel_st.pack(ipadx=10, ipady=10)
    ui.namelabel_nd.pack(ipadx=10, ipady=10)
    ui.namelabel_rd.pack(ipadx=10, ipady=10)
    ui.namelabel_th.pack(ipadx=10, ipady=10)


def get_id(ui):
    str_id = ui.idEntry.get()
    return str_id


def get_name(ui):
    str_name = ui.nameEntry.get()
    return str_name


def get_path(ui):
    str_path = ui.pathEntry.get()
    return str_path


def inf_add(ui):
    id = get_id(ui)
    name = get_name(ui)
    picpath = get_path(ui)
    send_add_req(id, name, picpath)


def inf_del(ui):
    id = get_id(ui)
    send_del_req(id)


def inf_get(ui):
    student_inf = send_get_req(1)
    load_id(ui, student_inf[0][0], student_inf[0][1],
            student_inf[0][2], student_inf[0][3])
    load_name(ui, student_inf[1][0], student_inf[1][1],
              student_inf[1][2], student_inf[1][3])
    load_pic(ui, student_inf[2][0], student_inf[2][1],
             student_inf[2][2], student_inf[2][3])


def inf_jump(ui):

    pageno = ui.pagenum.get()
    try:
        pageno = int(pageno)
    except:
        pageno = 1
    student_inf = send_get_req(pageno)
    load_id(ui, student_inf[0][0], student_inf[0][1],
            student_inf[0][2], student_inf[0][3])
    load_name(ui, student_inf[1][0], student_inf[1][1],
              student_inf[1][2], student_inf[1][3])
    load_pic(ui, student_inf[2][0], student_inf[2][1],
             student_inf[2][2], student_inf[2][3])


class Application(Frame):
    def __init__(self, master=None):
        self.count = 0
        Frame.__init__(self, master)
        self.pack()
        self.window_init()
        self.createWidgets()

    def window_init(self):
        self.master.title('学生信息系统')
        self.master.geometry("{}x{}".format(600, 420))  # 初始化界面

    def createWidgets(self):
        # fm1
        self.fm1 = Frame(self)
        self.fm1.pack(side=TOP)
        self.fm1_left = Frame(self.fm1)
        self.fm1_left.pack(side=LEFT)

        self.addButton = Button(
            self.fm1_left, text='ADD', bd=4, command=self.createAddWidgets)
        self.addButton.pack(side=LEFT)

        self.lookButton = Button(
            self.fm1_left, text='OVERVIEW', bd=4, command=self.createOverviewWidgets)
        self.lookButton.pack(side=RIGHT)

        self.delButton = Button(self.fm1_left, text='DEL',
                                bd=4, command=self.createDelWidgets)
        self.delButton.pack(side=RIGHT)

        self.fm2 = Frame(self)
        self.fm3 = Frame(self)

    def createAddWidgets(self):
        for widget in self.fm2.winfo_children():
            widget.destroy()
        for widget in self.fm3.winfo_children():
            widget.destroy()
        self.fm2_left = Frame(self.fm2)
        self.fm2_right = Frame(self.fm2)
        self.fm2_left_top = Frame(self.fm2_left)
        self.fm2_left_mid = Frame(self.fm2_left)
        self.fm2_left_bottom = Frame(self.fm2_left)
        self.fm2_right_top = Frame(self.fm2_right)
        self.fm2_right_mid = Frame(self.fm2_right)
        self.fm2_right_bottom = Frame(self.fm2_right)

        self.idlabel = Label(self.fm2_left_top, text="ID", font=("Arial", 12))
        self.namelabel = Label(
            self.fm2_left_mid, text="Name", font=("Arial", 12))

        self.idEntry = Entry(self.fm2_right_top)
        self.nameEntry = Entry(self.fm2_right_mid)
        self.pathEntry = Entry(self.fm2_right_bottom)
        self.uploadbtn = Button(self.fm2_left_bottom,
                                text="Upload Photo", command=lambda: upload_file(self.pathEntry), font=("Arial", 12))

        self.idlabel.pack(side=LEFT, ipadx=10, ipady=5)
        self.namelabel.pack(side=LEFT, ipadx=10, ipady=5)
        self.uploadbtn.pack(side=LEFT, ipadx=10, ipady=5)
        self.idEntry.pack(side=LEFT, ipadx=50, ipady=5)
        # self.idEntry.place(height=4, width=20)
        self.nameEntry.pack(side=LEFT, ipadx=50, ipady=5)
        self.pathEntry.pack(side=LEFT, ipadx=50, ipady=5)

        self.fm2_left_top.pack(side=TOP)
        self.fm2_left_mid.pack(side=TOP)
        self.fm2_left_bottom.pack(side=TOP)
        self.fm2_left.pack(side=LEFT)

        self.fm2_right_top.pack(side=TOP)
        self.fm2_right_mid.pack(side=TOP)
        self.fm2_right_bottom.pack(side=TOP)

        self.fm2_right.pack(side=LEFT)

        self.fm2.pack(side=TOP)

        self.confirmbtn = Button(
            self.fm3, text="Confirm", command=lambda: inf_add(self))
        self.confirmbtn.pack(side=LEFT, ipadx=10, ipady=5)
        self.fm3.pack(side=TOP)

    def createDelWidgets(self):
        for widget in self.fm2.winfo_children():
            widget.destroy()
        for widget in self.fm3.winfo_children():
            widget.destroy()
        self.fm2_left = Frame(self.fm2)
        self.fm2_right = Frame(self.fm2)
        self.idlabel = Label(self.fm2_left, text="ID", font=("Arial", 12))
        self.idEntry = Entry(self.fm2_right)
        self.idlabel.pack(side=LEFT, ipadx=10, ipady=5)
        self.idEntry.pack(side=LEFT, ipadx=50, ipady=5)
        self.fm2_left.pack(side=LEFT)
        self.fm2_right.pack(side=LEFT)
        self.fm2.pack(side=TOP)
        self.confirmbtn = Button(
            self.fm3, text="Confirm", command=lambda: inf_del(self))
        self.confirmbtn.pack(side=LEFT, ipadx=10, ipady=5)
        self.fm3.pack(side=TOP)

    def createOverviewWidgets(self):
        for widget in self.fm2.winfo_children():
            widget.destroy()
        for widget in self.fm3.winfo_children():
            widget.destroy()
        self.fm2_left = Frame(self.fm2)
        self.fm2_right = Frame(self.fm2)
        self.fm2_left_st = Frame(self.fm2_left)
        self.fm2_left_nd = Frame(self.fm2_left)
        self.fm2_left_rd = Frame(self.fm2_left)
        self.fm2_left_th = Frame(self.fm2_left)

        self.fm2_right_st = Frame(self.fm2_right)
        self.fm2_right_nd = Frame(self.fm2_right)
        self.fm2_right_rd = Frame(self.fm2_right)
        self.fm2_right_th = Frame(self.fm2_right)

        self.fm2_right_st_top = Frame(self.fm2_right_st)
        self.fm2_right_nd_top = Frame(self.fm2_right_nd)
        self.fm2_right_rd_top = Frame(self.fm2_right_rd)
        self.fm2_right_th_top = Frame(self.fm2_right_th)

        self.fm2_right_st_btm = Frame(self.fm2_right_st)
        self.fm2_right_nd_btm = Frame(self.fm2_right_nd)
        self.fm2_right_rd_btm = Frame(self.fm2_right_rd)
        self.fm2_right_th_btm = Frame(self.fm2_right_th)

        inf_get(self)

        self.fm2_right_st_top.pack(side=TOP)
        self.fm2_right_nd_top.pack(side=TOP)
        self.fm2_right_rd_top.pack(side=TOP)
        self.fm2_right_th_top.pack(side=TOP)

        self.fm2_right_st_btm.pack(side=TOP)
        self.fm2_right_nd_btm.pack(side=TOP)
        self.fm2_right_rd_btm.pack(side=TOP)
        self.fm2_right_th_btm.pack(side=TOP)

        self.fm2_right_st.pack(side=TOP)
        self.fm2_right_nd.pack(side=TOP)
        self.fm2_right_rd.pack(side=TOP)
        self.fm2_right_th.pack(side=TOP)

        self.fm2_left_st.pack(side=TOP)
        self.fm2_left_nd.pack(side=TOP)
        self.fm2_left_rd.pack(side=TOP)
        self.fm2_left_th.pack(side=TOP)

        self.fm2_left.pack(side=LEFT)
        self.fm2_right.pack(side=LEFT)

        self.fm2.pack(side=TOP)

        self.fm3_left = Frame(self.fm3)
        self.fm3_right = Frame(self.fm3)

        self.pagenum = Entry(self.fm3_left, width=3)
        self.pagenum.pack(side=LEFT, ipady=5)

        self.confirmbtn = Button(
            self.fm3_right, text="Jump to the page inputted", command=lambda: inf_jump(self))
        self.confirmbtn.pack(side=LEFT, ipadx=10, ipady=5)

        self.fm3_left.pack(side=LEFT)
        self.fm3_right.pack(side=LEFT)
        self.fm3.pack(side=TOP)


if __name__ == '__main__':
    app = Application()
    # to do
    app.mainloop()
