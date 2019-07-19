from pywinauto.application import Application

def dops_toweb():
    '''操作photoshop'''
    app = Application().connect(class_name="Photoshop", title="Adobe Photoshop CC 2019")
    win = app.top_window()
    win.type_keys("%f")
    win.type_keys("ub")
    win.type_keys("{ENTER}")
    win.minimize()
    # print("done!")

if __name__ == "__main__":
    app = Application().connect(class_name="Photoshop", title="Adobe Photoshop CC 2019")
    win = app.top_window()
    win.type_keys("^o")
    # win.minimize()
    print()