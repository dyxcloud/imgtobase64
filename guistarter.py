from tkinter import Tk
from tkinter import StringVar
from tkinter import scrolledtext
from tkinter import filedialog
from tkinter.font import Font
from tkinter import ttk

import mytool

class Application_ui(ttk.Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.master.title('图片转Base64')
        self.master.geometry('406x150')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = ttk.Style()

        self.data_url = StringVar(value='')
        self.Text1 = ttk.Entry(self.top, textvariable=self.data_url, font=('微软雅黑',9))
        self.Text1.place(relx=0.040, rely=0.070, relwidth=0.500, relheight=0.180)

        self.style.configure('Command1.TButton',font=('微软雅黑',9))
        self.Command1 = ttk.Button(self.top, text='上传', command=self.doupload, style='Command1.TButton')
        self.Command1.place(relx=0.571, rely=0.070, relwidth=0.120, relheight=0.180)

        self.style.configure('Command2.TButton',font=('微软雅黑',9))
        self.Command2 = ttk.Button(self.top, text='转换', command=self.dotrans, style='Command2.TButton')
        self.Command2.place(relx=0.730, rely=0.070, relwidth=0.230, relheight=0.180)

        #下拉
        self.Combo1List = ['不压缩','压缩至webp','压缩至png']
        self.Combo1 = ttk.Combobox(self.top,state="readonly", values=self.Combo1List, font=('微软雅黑',9))
        self.Combo1.current(0)
        self.Combo1.place(relx=0.040, rely=0.300, relwidth=0.400, relheight=0.150)

        # 选择框
        self.auto_compress = StringVar(value='1')
        self.style.configure('Check1.TCheckbutton',font=('微软雅黑',9))
        self.Check1 = ttk.Checkbutton(self.top, text='小于60k不压缩', variable=self.auto_compress, style='Check1.TCheckbutton')
        self.Check1.place(relx=0.480, rely=0.300, relwidth=0.400, relheight=0.150)

        self.copytext = StringVar(value='点击复制')
        self.style.configure('Command2.TButton',font=('微软雅黑',9))
        self.Command3 = ttk.Button(self.top, textvariable =self.copytext, command=self.docopy, style='Command3.TButton')
        self.Command3.place(relx=0.040, rely=0.500, relwidth=0.920, relheight=0.430)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    result = ""

    def doupload(self, event=None):
        local_file_path = filedialog.askopenfilename(title='上传', filetypes=[('image', '*.jpg;*.jpeg;*.png;*.gif;*.ico;*.bmp;*.webp'), ('All Files', '*')])
        self.copytext.set("making...")
        checkdata = self.Combo1.get()
        checkindex = self.Combo1List.index(checkdata)
        ifauto = int(self.auto_compress.get())

        self.result,showlen = mytool.work_file(local_file_path,checkindex,ifauto)
        if len(self.result)>50:
            addToClipBoard(self.result)
            self.copytext.set("点击复制, "+showlen)
        else:
            self.copytext.set("fail!")

    def dotrans(self, event=None):
        self.copytext.set("making...")
        dataurl = self.data_url.get()
        checkdata = self.Combo1.get()
        checkindex = self.Combo1List.index(checkdata)
        ifauto = int(self.auto_compress.get())

        self.result,showlen = mytool.work_url(dataurl,checkindex,ifauto)
        if len(self.result)>50:
            addToClipBoard(self.result)
            self.copytext.set("点击复制, "+showlen)
        else:
            self.copytext.set("fail!")
    
    def docopy(self, even=None):
        addToClipBoard(self.result)


def addToClipBoard(text):
        # command = 'echo ' + text + '| clip'
        # os.system(command)
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(text)
        r.update()
        r.destroy()

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    top.destroy()