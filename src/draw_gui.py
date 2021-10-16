import os
import tkinter.messagebox
from tkinter import Button, Entry, Frame, Label, StringVar, Tk
from tkinter.constants import E, N, S, W
from tkinter.filedialog import askdirectory, askopenfilename

from src.wordcloud_gen import generator_cloud_image, handle_picture, resize_picture

imagedir = "images"
default_original_mask = os.path.join(os.path.join(os.getcwd(), imagedir), "default_mask.png")
default_generator_mask = os.path.join(os.path.join(os.getcwd(), imagedir), "cn.jpg")
global current
global picture_dir


def GUI():
    def move_to_picture_view():
        window2.grid_forget()
        window3.grid_forget()
        window.grid(row=2, columnspan=3)

    def move_to_word_cloud():
        window.grid_forget()
        window3.grid_forget()
        window2.grid(row=2, columnspan=3)

    def move_to_change_pic():
        window.grid_forget()
        window2.grid_forget()
        window3.grid(row=2, columnspan=3)

    def select_text_file():
        """
        功能：选择某一特定类型的图片，返回一个由图片绝对路径组成的元祖
        """
        text_name = askopenfilename(title="选择分词文件 ", filetypes=[("文件（TXT）", "*.txt"), ("All Files", "*")])
        if len(text_name) != 0:
            print("您选择的文件是：" + text_name)  # 返回的是绝对路径
            file_path.set(text_name)
            tkinter.messagebox.showinfo("提示", "选择的文件是 :[%s]" % text_name)
            return text_name
        else:
            print("您没有选择任何文件")
            tkinter.messagebox.showinfo("提示", "您本次没有选择任何文件")
            return ""

    def select_image():
        """
        功能：选择某一特定类型的图片，返回一个由图片绝对路径组成的元祖

        """
        image_name = askopenfilename(
            title="选择图片 ",
            filetypes=[("图片（PNG）", "*.png"), ("图片（JPG）", "*.jpg"), ("All Files", "*")],
        )
        if len(image_name) != 0:
            print("您选择的文件是：" + image_name)  # 返回的是绝对路径
            image_path.set(image_name)

            photo = handle_picture(image_name)
            original_image["image"] = photo
            original_image.image = photo

            # original_image.configure(image=photo)
            # tkinter.messagebox.showinfo('提示', '选择的图片是 :[%s]' % image_name)
        else:
            print("您没有选择任何文件")
            tkinter.messagebox.showinfo("提示", "您本次没有选择任何文件")
            return ""

    def select_images():
        image_name = askdirectory(
            title="选择图片文件夹 ",
        )
        if len(image_name) != 0:
            print("您选择的文件夹：" + image_name)  # 返回的是绝对路径

            image_pics = get_image_files(image_name)
            if len(image_pics) == 0:
                tkinter.messagebox.showinfo("提示", "您本次选择的文件夹内没有图片")
                return ""
            else:
                images_path.set(image_name)
                # tkinter.messagebox.showinfo('提示', '选择的图片是 :[%s]' % image_name)
                return image_name
        else:
            print("您没有选择任何文件")
            tkinter.messagebox.showinfo("提示", "您本次没有选择任何文件")
            return ""

    def generator_image():
        if len(file_path.get()) == 0:
            tkinter.messagebox.showinfo("提示", "请先选择分词文件")
            return
        if len(image_path.get()) == 0:
            tkinter.messagebox.showinfo("提示", "请先选择图片文件")
            return
        new_word_cloud_image = generator_cloud_image(file_path.get(), image_path.get())
        new_photo = handle_picture(new_word_cloud_image)
        generator_image["image"] = new_photo
        generator_image.image = new_photo
        # generator_image.configure(image=new_photo)

    def get_image_files(imagedir=imagedir):
        global current
        global picture_list
        suffix = (".jpg", ".bmp", ".png")
        imgpath = os.path.join(os.getcwd(), imagedir)
        pics = [os.path.join(imgpath, p) for p in os.listdir(imgpath) if p.endswith(suffix)]
        picture_list = pics
        current = -1
        return pics

    def changePic(flag):
        """flag=-1表示上一个，flag=1表示下一个"""
        global current
        global picture_list

        new = current + flag
        if len(picture_list) == 0:
            get_image_files()
        elif new < 0:
            tkinter.messagebox.showerror("", "这已经是第一张图片了")
        elif new >= len(picture_list):
            tkinter.messagebox.showerror("", "这已经是最后一张图片了")
        else:
            # 获取要切换的图片文件名
            pic = picture_list[new]
            # 创建Image对象并进行缩放
            new_photo = handle_picture(pic)

            show_pic["image"] = new_photo
            show_pic.image = new_photo
            show_pic2["image"] = new_photo
            show_pic2.image = new_photo
            current = new

    def select_change_image():
        """
        功能：选择某一特定类型的图片，返回一个由图片绝对路径组成的元祖

        """
        image_name = askopenfilename(
            title="选择图片 ",
            filetypes=[("图片（PNG）", "*.png"), ("图片（JPG）", "*.jpg"), ("All Files", "*")],
        )
        if len(image_name) != 0:
            print("您选择的文件是：" + image_name)  # 返回的是绝对路径
            image_change_path.set(image_name)

            photo = handle_picture(image_name)
            show_change_pic["image"] = photo
            show_change_pic.image = photo
        else:
            print("您没有选择任何文件")
            tkinter.messagebox.showinfo("提示", "您本次没有选择任何文件")
            return ""

    def change_pic():
        if len(image_change_path.get()) == 0:
            tkinter.messagebox.showinfo("提示", "请先选择图片文件")
            return
        if len(image_change_x_var.get()) == 0:
            tkinter.messagebox.showinfo("提示", "请设置图片高度")
            return
        if len(image_change_y_var.get()) == 0:
            tkinter.messagebox.showinfo("提示", "请设置图片宽度")
            return
        changed_pic = resize_picture(
            image_change_path.get(), int(image_change_x_var.get()), int(image_change_y_var.get())
        )
        show_change_pic2["image"] = changed_pic
        show_change_pic2.image = changed_pic
        tkinter.messagebox.showinfo("提示", "修改图片成功")

    root = Tk()
    root.geometry("860x640")  # 设置窗口大小
    root.title("词云生成器和图片浏览器")  # 设置标题

    Label(
        root,
        text="由Python制作而成的词云生成器",
        height=2,
        width=18,
        font=("Times", 15, "bold"),
    ).grid(row=0, column=0, padx=5, pady=5, sticky=N + S + W + E, columnspan=10)

    # 切换窗口
    word_button = Button(master=root, text="词云", command=move_to_picture_view)
    word_button.grid(row=1, column=0, padx=5, pady=5, sticky=N + S + W + E)
    pic_button = Button(master=root, text="浏览照片", command=move_to_word_cloud)
    pic_button.grid(row=1, column=1, padx=5, pady=5, sticky=N + S + W + E)
    pic_change = Button(master=root, text="修剪照片", command=move_to_change_pic)
    pic_change.grid(row=1, column=2, padx=5, pady=5, sticky=N + S + W + E)

    window = Frame(root, bg="green")
    window.grid(row=2, columnspan=3)
    window2 = Frame(root, bg="blue")
    window3 = Frame(root, bg="white")

    # 图片修剪器
    image_change_path = StringVar()
    image_change_label = Label(window3, text="目标路径:")
    image_change_label.grid(row=0, column=0, padx=5, pady=5)
    image_change_entry = Entry(window3, textvariable=image_change_path)
    image_change_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=8, sticky=N + S + W + E)
    image_change_path_button = Button(window3, text="选择图片", fg="#ffffff", bg="#dd33cc", command=select_change_image)
    image_change_path_button.grid(row=0, column=9, padx=5, pady=5, sticky=N + S + W + E)

    image_change_x_label = Label(window3, text="图片高度:")
    image_change_x_label.grid(row=1, column=0, padx=5, pady=5)

    image_change_x_var = StringVar()
    image_change_x_entry = Entry(window3, textvariable=image_change_x_var)
    image_change_x_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=5, sticky=N + S + W + E)

    image_change_y_label = Label(window3, text="图片宽度:")
    image_change_y_label.grid(row=2, column=0, padx=5, pady=5)
    image_change_y_var = StringVar()
    image_change_y_entry = Entry(window3, textvariable=image_change_y_var)
    image_change_y_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=5, sticky=N + S + W + E)

    image_change_button = Button(window3, text="修改图片", fg="#ffffff", bg="#dd82f0", command=change_pic)
    image_change_button.grid(row=1, column=6, columnspan=4, rowspan=2, padx=5, pady=5, sticky=N + S + W + E)

    show_change_pic = Label(window3)
    show_change_pic.grid(row=3, column=0, columnspan=5, padx=5, pady=5)
    show_change_pic2 = Label(window3)
    show_change_pic2.grid(row=3, column=5, columnspan=5, padx=5, pady=5)

    # 图片浏览器
    images_path = StringVar()
    images_label = Label(window2, text="目标路径:")
    images_label.grid(row=0, column=0)
    images_entry = Entry(window2, textvariable=images_path)
    images_entry.grid(row=0, column=1, columnspan=8, sticky=N + S + W + E)
    images_button = Button(window2, text="选择图片文件夹", fg="#ffffff", bg="#cc82f0", command=select_images)
    images_button.grid(row=0, column=9, padx=5, pady=5, sticky=N + S + W + E)

    show_pic = Label(window2)
    show_pic.grid(row=1, column=0, columnspan=5, padx=5, pady=5)
    show_pic2 = Label(window2)
    show_pic2.grid(row=1, column=5, columnspan=5, padx=5, pady=5)

    btn_pre = Button(window2, text="上一张", command=lambda: changePic(-1))
    btn_pre.grid(row=2, column=0, columnspan=5, padx=5, pady=5, sticky=N + S + W + E)
    btn_next = Button(window2, text="下一张", command=lambda: changePic(1))
    btn_next.grid(row=2, column=5, columnspan=5, padx=5, pady=5, sticky=N + S + W + E)
    get_image_files()
    changePic(1)

    # 词云生成器
    file_path = StringVar()
    file_label = Label(window, text="目标路径:")
    file_label.grid(row=1, column=0)
    file_entry = Entry(window, textvariable=file_path)
    file_entry.grid(row=1, column=1, columnspan=8, sticky=N + S + W + E)
    file_button = Button(window, text="选择文件", fg="#ffffff", bg="#cc82f0", command=select_text_file)
    file_button.grid(row=1, column=9, padx=5, pady=5, sticky=N + S + W + E)

    image_path = StringVar()
    image_label = Label(window, text="目标路径:")
    image_label.grid(row=2, column=0)
    image_entry = Entry(window, textvariable=image_path)
    image_entry.grid(row=2, column=1, columnspan=8, sticky=N + S + W + E)
    image_button = Button(window, text="选择图片", fg="#ffffff", bg="#cc82f0", command=select_image)
    image_button.grid(row=2, column=9, padx=5, pady=5, sticky=N + S + W + E)

    generator_button = Button(window, text="生成词云图", fg="#ffffff", bg="#0082f0", command=generator_image)
    generator_button.grid(row=3, padx=5, pady=5, sticky=N + S + W + E, columnspan=10)

    o_img_open = handle_picture(default_original_mask)
    original_image = Label(window, image=o_img_open)
    original_image.grid(row=4, column=0, columnspan=5, padx=5, pady=5, sticky=N + S + W + E)

    g_img_open = handle_picture(default_generator_mask)
    generator_image = Label(window, image=g_img_open)
    generator_image.grid(row=4, column=5, columnspan=5, padx=5, pady=5, sticky=N + S + W + E)

    root.mainloop()


GUI()
