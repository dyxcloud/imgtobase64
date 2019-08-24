import os
from subprocess import run

import mytool
import imagemapping

def compression(source, result,is_to_png = False):
    if not os.path.isfile(source):
        raise FileNotFoundError("压缩时文件不存在"+source)
    if is_to_png:
        if source.endswith(".png") and _is_png_with_stream(source):
            _topng(source,result)
        else:
            tmpfile = _convert(source)
            _topng(tmpfile,result)
            os.remove(tmpfile)
    else:
        _towebp(source,result)
    if not os.path.isfile(result):
        raise FileNotFoundError("压缩结果不存在"+result)

def _towebp(source, result):
    if os.path.splitext(source)[1]==".gif":
        command=".\\lib\\gif2webp.exe -mixed -q 30 -m 6 -mt \"{}\" -o \"{}\"".format(source,result)
    else:
        command = ".\\lib\\cwebp.exe -q 30 -m 6 -mt -size 70000 \"{}\" -o \"{}\"".format(source,result)
        # command = "cwebp.exe -q 30 -m 6 -mt {} -o {}".format(source,result)
    # os.system(command)
    run(command,shell=True)

def _convert(source):
    command=".\\lib\\nconvert.exe -out png  \"{}\"".format(source)
    # os.system(command)
    run(command,shell=True)
    #如果source后缀为png, 则结果为原文件名_1.png
    if source.endswith(".png"):
        result = source[0:-4]+"_1.png"
    else:
        result = mytool.filename_change(source,"png")
    if not os.path.isfile(result):
        raise FileNotFoundError("转换至png错误"+result)
    return result

def _topng(source, result):
    #使用pngquant转换,图源只支持png
    command=".\\lib\\pngquant.exe --force --strip --ordered --speed=1 --quality=20-60 \"{}\" -o \"{}\"".format(source,result)
    # os.system(command)
    run(command,shell=True)


def _is_png_with_stream(file):
    '''读取文件头判断是否是png文件'''
    binfile = open(file, 'rb')
    bytes = binfile.read(10)
    binfile.close()
    #str = ''.join(['%02X' % b for b in bytes])
    str = ''.join(['{:02X}'.format(b) for b in bytes])
    return str.startswith(imagemapping.file_header_png)


if __name__ == "__main__":
    s = "D:/Download/qwe.svg"
    d = s+".webp"
    #_convert(s)
    #print(_is_png_with_stream(s))
    _convert(s)