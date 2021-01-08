import os
import shutil
import time

from base64 import b64encode

from src import downloader, image_mapping, size_reduce

ps_workspace = r"../wowrkspace/"
ps_result = ps_workspace + "result/"
# 初始化工作目录
if not os.path.exists(ps_result):
    os.makedirs(ps_result)


def filename_change(filename, ex):
    """更改后缀名,ex=png"""
    name = os.path.splitext(filename)[0]
    return name + "." + ex


def do_base64_with_bytes(byte, filename):
    data = b64encode(byte)
    return _base64_getheader(filename) + data.decode()


def do_base64(filename):
    """本地图片转base64"""
    if not os.path.isfile(filename):
        raise FileNotFoundError("转base64时文件不存在" + filename)
    with open(filename, "rb") as f:  # 转为二进制格式
        data = b64encode(f.read())  # 使用base64进行加密
        return _base64_getheader(filename) + data.decode()


def _base64_getheader(filename):
    """获取base64头"""
    ex = os.path.splitext(filename)[1]
    return image_mapping.base64headers[ex]


def _with_md(result_line, imgname, url=None):
    """为base64结果添加md格式"""
    if url is None:
        pass
        return "![{}]({})".format(imgname, result_line)
    else:
        return "[![{}]({})]({})".format(imgname, result_line, url)


def work_url(url, index=0, if_auto=1, with_md=0):
    """0不压缩,1webp,2png"""
    response, img_name = downloader.get_response_img_name(url)
    byte = response.read()
    s = "{:.2f}".format(len(byte) / 1024.0)
    if if_auto and len(byte) < 60 * 1024:
        index = 0
    if index == 0:
        result_line = do_base64_with_bytes(byte, img_name)
        show_len = "nochange {}k".format(s)
    else:
        source_path = ps_workspace + img_name
        downloader.download_by_bytes(byte, source_path)
        is_to_png = index == 2
        if is_to_png:
            # 先判断source路径是否是ascii
            is_ascii = all(ord(c) < 128 for c in source_path)
            if not is_ascii:
                new_source = ps_workspace + str(int(time.time())) + "temp.png"
                shutil.copy(source_path, new_source)
                os.remove(source_path)
                source_path = new_source
                result_path = ps_result + str(int(time.time())) + "temp.png"
            else:
                result_path = ps_result + filename_change(img_name, "png")
        else:
            result_path = ps_result + filename_change(img_name, "webp")
        size_reduce.compression(source_path, result_path, is_to_png)
        result_line = do_base64(result_path)
        r = "{:.2f}".format(os.path.getsize(result_path) / 1024.0)
        show_len = "img_size {}k to {}k".format(s, r)
        os.remove(source_path)
        os.remove(result_path)
    if with_md:
        result_line = _with_md(result_line, img_name, url)
    return result_line, show_len


def work_file(source_path, index=0, ifauto=1, with_md=0):
    """0不压缩,1webp,2png"""
    img_name = os.path.basename(source_path)
    s = "{:.2f}".format(os.path.getsize(source_path) / 1024.0)
    if ifauto and os.path.getsize(source_path) < 60 * 1024:
        index = 0
    if index == 0:
        result_line = do_base64(source_path)
        show_len = "nochange {}k".format(s)
    else:
        is_to_png = index == 2
        if is_to_png:
            # 先判断source路径是否是ascii 如果不是的话需要复制到workspace
            is_ascii = all(ord(c) < 128 for c in source_path)
            if not is_ascii:
                new_source = ps_workspace + str(int(time.time())) + "temp.png"
                shutil.copy(source_path, new_source)
                source_path = new_source
                result_path = ps_result + str(int(time.time())) + "temp.png"
            else:
                result_path = ps_result + filename_change(img_name, "png")
        else:
            result_path = ps_result + filename_change(img_name, "webp")
        size_reduce.compression(source_path, result_path, is_to_png)
        result_line = do_base64(result_path)
        r = "{:.2f}".format(os.path.getsize(result_path) / 1024.0)
        show_len = "img_size {}k to {}k".format(s, r)
        os.remove(result_path)
        # noinspection PyUnboundLocalVariable
        if is_to_png and not is_ascii:
            os.remove(source_path)
    if with_md:
        result_line = _with_md(result_line, img_name)
    return result_line, show_len


# program
'''
基本流程:
1. url转本地图片
2. 本地图片压缩
3. 图片转base64
4. gui
'''
if __name__ == "__main__":
    pass
    # result,show = work_url("https://hustcat.github.io/assets/GPU/cpu_vs_gpu_00.png",2,False)
    # print(result)
    # print(show)
