import os
import time

#from tools.imgtool import pscontrol

def _tryfile(filepath):
    '''自旋10秒,判断文件是否导出完毕
    供ps生成, 需要改进
    '''
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
    #         print("File is not accessible")


def compression(source, result,is_to_png = False):
    #暂不使用ps
    #pscontrol.dops_toweb()
    #_tryfile(result_path)
    if is_to_png:
        if not source.endswith(".png"):
            _convert(source,result)
            source = result
        _topng(source,result)
    else:
        _towebp(source,result)

def _towebp(source, result):
    if os.path.splitext(source)[1]==".gif":
        commond=".\\lib\\gif2webp.exe -mixed -q 30 -m 6 -mt \"{}\" -o \"{}\"".format(source,result)
    else:
        commond = ".\\lib\\cwebp.exe -q 30 -m 6 -mt -size 70000 \"{}\" -o \"{}\"".format(source,result)
        # commond = "cwebp.exe -q 30 -m 6 -mt {} -o {}".format(source,result)
    os.system(commond)

def _convert(source,result):
    commond=".\\lib\\convert.exe  \"{}\" \"{}\"".format(source,result)
    os.system(commond)

def _topng(source, result):
    #使用pngquant转换,图源只支持png
    if os.path.splitext(source)[1]==".png":
        commond=".\\lib\\pngquant.exe --force --strip --ordered --speed=1 --quality=20-60 \"{}\" -o \"{}\"".format(source,result)
    os.system(commond)

if __name__ == "__main__":
    s = r"D:\Download\TIM截图20190722095713.png"
    r = r"D:\Download\TIM截图20190722095713111.png"
    compression(s,r,True)
    print()