from pywinauto.application import Application


def dops_toweb():
    """操作photoshop"""
    app = Application().connect(class_name="Photoshop", title="Adobe Photoshop CC 2019")
    win = app.top_window()
    win.type_keys("%f")
    win.type_keys("ub")
    win.type_keys("{ENTER}")
    win.minimize()
    # print("done!")


'''def _tryfile(filepath):
    #自旋10秒,判断文件是否导出完毕
    #供ps生成, 需要改进
    
    start = time.time()
    long = 10.0

    # isnot_exist = True
    # while time.time()-start<long and isnot_exist:
    #     isnot_exist = not os.path.exists(filepath)

    time.sleep(1)

    # isnot_exist = True
    # while time.time()-start<long and isnot_exist:
    #     size = not os.path.getsize(filepath)
    #     if size>10 :
    #         isnot_exist = False

    # isnot_exist = True
    # while time.time()-start<long and isnot_exist:
    #     try:
    #         f =open(filepath,"ab")
    #         f.close()
    #         isnot_exist = False
    #     except IOError:
    #         print("File is not accessible")'''


def main():
    app = Application().connect(class_name="Photoshop", title="Adobe Photoshop CC 2019")
    win = app.top_window()
    win.type_keys("^o")
    # win.minimize()
    print()


if __name__ == "__main__":
    main()
