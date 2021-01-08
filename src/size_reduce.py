import os
from subprocess import run

from src import my_tool, image_mapping


def compression(source, result, is_to_png=False):
    if not os.path.isfile(source):
        raise FileNotFoundError("压缩时文件不存在" + source)
    if is_to_png:
        if source.endswith(".png") and _is_png_with_stream(source):
            _to_png(source, result)
        else:
            tmp_file = _convert(source)
            _to_png(tmp_file, result)
            os.remove(tmp_file)
    else:
        _to_webp(source, result)
    if not os.path.isfile(result):
        raise FileNotFoundError("压缩结果不存在" + result)


def _to_webp(source, result):
    if os.path.splitext(source)[1] == ".gif":
        command = "..\\lib\\gif2webp.exe -mixed -q 30 -m 6 -mt \"{}\" -o \"{}\"".format(source, result)
    else:
        command = "..\\lib\\cwebp.exe -q 30 -m 6 -mt -size 70000 \"{}\" -o \"{}\"".format(source, result)
        # command = "cwebp.exe -q 30 -m 6 -mt {} -o {}".format(source,result)
    # os.system(command)
    run(command, shell=True)


def _convert(source):
    command = "..\\lib\\nconvert.exe -out png  \"{}\"".format(source)
    # os.system(command)
    run(command, shell=True)
    # 如果source后缀为png, 则结果为原文件名_1.png
    if source.endswith(".png"):
        result = source[0:-4] + "_1.png"
    else:
        result = my_tool.filename_change(source, "png")
    if not os.path.isfile(result):
        raise FileNotFoundError("转换至png错误" + result)
    return result


def _to_png(source, result):
    # 使用pngquant转换,图源只支持png 工具不支持中文文件名与路径
    command = "..\\lib\\pngquant.exe --force --strip --ordered --speed=1 --quality=20-60 \"{}\" -o \"{}\"".format(
        source, result)
    # os.system(command)
    run(command, shell=True)


def _is_png_with_stream(file):
    """读取文件头判断是否是png文件"""
    bin_file = open(file, 'rb')
    byte = bin_file.read(10)
    bin_file.close()
    # str = ''.join(['%02X' % b for b in bytes])
    string = ''.join(['{:02X}'.format(b) for b in byte])
    return string.startswith(image_mapping.file_header_png)


def main():
    s = "D:/Download/TI20190831093249.png"
    # d = s + "222222222.png"
    # compression(s,d,True)
    print(all(ord(c) < 128 for c in s))


if __name__ == "__main__":
    main()
