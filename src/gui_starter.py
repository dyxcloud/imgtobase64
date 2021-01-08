import traceback
from tkinter import Tk
from tkinter import StringVar
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

from src import my_tool, image_mapping


class Application(ttk.Frame):
    result = ""

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.master.title('图片转Base64')
        self.master.geometry('406x150')
        self.top = self.winfo_toplevel()

        self.style = ttk.Style()

        self.data_url = StringVar(value='')
        self.Text1 = ttk.Entry(self.top, textvariable=self.data_url, font=('微软雅黑', 9))
        self.Text1.place(relx=0.040, rely=0.070, relwidth=0.500, relheight=0.180)

        self.style.configure('Command1.TButton', font=('微软雅黑', 9))
        self.Command1 = ttk.Button(self.top, text='上传', command=self.do_upload, style='Command1.TButton')
        self.Command1.place(relx=0.571, rely=0.070, relwidth=0.120, relheight=0.180)

        self.style.configure('Command2.TButton', font=('微软雅黑', 9))
        self.Command2 = ttk.Button(self.top, text='转换', command=self.do_trans, style='Command2.TButton')
        self.Command2.place(relx=0.730, rely=0.070, relwidth=0.230, relheight=0.180)

        # 下拉
        self.Combo1List = ['不压缩', '压缩至webp', '压缩至png']
        self.Combo1 = ttk.Combobox(self.top, state="readonly", values=self.Combo1List, font=('微软雅黑', 9))
        self.Combo1.current(0)
        self.Combo1.place(relx=0.040, rely=0.300, relwidth=0.350, relheight=0.150)

        # 选择框
        self.auto_compress = StringVar(value='1')
        self.style.configure('Check1.TCheckbutton', font=('微软雅黑', 9))
        self.Check1 = ttk.Checkbutton(self.top, text='小于60k不压缩', variable=self.auto_compress,
                                      style='Check1.TCheckbutton')
        self.Check1.place(relx=0.420, rely=0.300, relwidth=0.300, relheight=0.150)

        self.with_md = StringVar(value='1')
        self.style.configure('Check1.TCheckbutton', font=('微软雅黑', 9))
        self.Check1 = ttk.Checkbutton(self.top, text='md格式', variable=self.with_md, style='Check1.TCheckbutton')
        self.Check1.place(relx=0.760, rely=0.300, relwidth=0.200, relheight=0.150)

        self.copy_text = StringVar(value='点击复制')
        self.style.configure('Command2.TButton', font=('微软雅黑', 9))
        self.Command3 = ttk.Button(self.top, textvariable=self.copy_text, command=self.do_copy, style='Command3.TButton')
        self.Command3.place(relx=0.040, rely=0.500, relwidth=0.920, relheight=0.430)

    def do_upload(self):
        # noinspection PyBroadException
        try:
            local_file_path = filedialog.askopenfilename(title='上传',
                                                         filetypes=[('image', image_mapping.select_file_types),
                                                                    ('All Files', '*')])
            if local_file_path == "":
                return
            self.copy_text.set("making...")
            check_data = self.Combo1.get()
            check_index = self.Combo1List.index(check_data)
            if_auto = int(self.auto_compress.get())
            with_md = int(self.with_md.get())

            self.result, showlen = my_tool.work_file(local_file_path, check_index, if_auto, with_md)
            if len(self.result) > 50:
                add_to_clipboard(self.result)
                self.copy_text.set("点击复制, " + showlen)
            else:
                self.copy_text.set("fail!")
        except Exception:
            messagebox.showinfo(title='error', message=traceback.format_exc())

    def do_trans(self):
        # noinspection PyBroadException
        try:
            self.copy_text.set("making...")
            data_url = self.data_url.get()
            check_data = self.Combo1.get()
            checkindex = self.Combo1List.index(check_data)
            if_auto = int(self.auto_compress.get())
            with_md = int(self.with_md.get())

            if len(data_url) == 0:
                return

            self.result, showlen = my_tool.work_url(data_url, checkindex, if_auto, with_md)
            if len(self.result) > 50:
                add_to_clipboard(self.result)
                self.copy_text.set("点击复制, " + showlen)
            else:
                self.copy_text.set("fail!")
        except Exception:
            messagebox.showinfo(title='error', message=traceback.format_exc())

    def do_copy(self):
        add_to_clipboard(self.result)


def add_to_clipboard(text):
    # command = 'echo ' + text + '| clip'
    # os.system(command)
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update()
    r.destroy()


def run_gui():
    top = Tk()
    Application(top).mainloop()
    # top.destroy()


if __name__ == "__main__":
    run_gui()
