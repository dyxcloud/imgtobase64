import os
import shutil
import time

from base64 import b64encode

from src import downloader, imagemapping, sizereduce

psworkspace = r"./wowrkspace/"
psresult = psworkspace + "result/"
#初始化工作目录
if not os.path.exists(psresult):
    os.makedirs(psresult)


def filename_change(filename,ex):
    '''更改后缀名,ex=png'''
    name = os.path.splitext(filename)[0]
    return name+"."+ex

def dobase64_with_bytes(bytes,filename):
    data = b64encode(bytes)
    return _base64_getheader(filename)+data.decode()

def dobase64(filename):
    '''本地图片转base64'''
    if not os.path.isfile(filename):
        raise FileNotFoundError("转base64时文件不存在"+filename)
    with open(filename, "rb") as f:  # 转为二进制格式
        data = b64encode(f.read())  # 使用base64进行加密
        return _base64_getheader(filename)+data.decode()

def _base64_getheader(filename):
    '''获取base64头'''
    ex = os.path.splitext(filename)[1]
    return imagemapping.base64headers[ex]

def _with_md(result_line,imgname,url=None):
    '''为base64结果添加md格式'''
    if url is None:
        pass
        return "![{}]({})".format(imgname,result_line)
    else:
        return "[![{}]({})]({})".format(imgname,result_line,url)


def work_url(url,index=0,ifauto=1,with_md=0):
    '''0不压缩,1webp,2png'''
    response,imgname = downloader.get_response_imgname(url)
    bytes = response.read()
    s = "{:.2f}".format(len(bytes)/1024.0)
    if ifauto and len(bytes) < 60*1024:
        index = 0
    if index==0:
        result_line = dobase64_with_bytes(bytes,imgname)
        showlen = "nochange {}k".format(s)
    else:
        source_path = psworkspace+imgname
        downloader.download_by_bytes(bytes, source_path)
        is_to_png = index==2
        if is_to_png:
            #先判断source路径是否是ascii
            is_ascii = all(ord(c) < 128 for c in source_path)
            if not is_ascii:
                new_source = psworkspace+str(int(time.time()))+"temp.png"
                shutil.copy(source_path,new_source)
                os.remove(source_path)
                source_path = new_source
                result_path = psresult+str(int(time.time()))+"temp.png"
            else:
                result_path = psresult+filename_change(imgname,"png")
        else:
            result_path = psresult+filename_change(imgname,"webp")
        sizereduce.compression(source_path, result_path, is_to_png)
        result_line = dobase64(result_path)
        r = "{:.2f}".format(os.path.getsize(result_path)/1024.0)
        showlen = "img_size {}k to {}k".format(s,r)
        os.remove(source_path)
        os.remove(result_path)
    if with_md:
        result_line = _with_md(result_line,imgname,url)
    return result_line,showlen

def work_file(source_path,index=0,ifauto=1,with_md=0):
    '''0不压缩,1webp,2png'''
    imgname = os.path.basename(source_path)
    s = "{:.2f}".format(os.path.getsize(source_path)/1024.0)
    if ifauto and os.path.getsize(source_path) < 60*1024:
        index = 0
    if index==0:
        result_line = dobase64(source_path)
        showlen = "nochange {}k".format(s)
    else:
        is_to_png = index==2
        if is_to_png:
            #先判断source路径是否是ascii
            is_ascii = all(ord(c) < 128 for c in source_path)
            if not is_ascii:
                new_source = psworkspace+str(int(time.time()))+"temp.png"
                shutil.copy(source_path,new_source)
                source_path = new_source
                result_path = psresult+str(int(time.time()))+"temp.png"
            else:
                result_path = psresult+filename_change(imgname,"png")
        else:
            result_path = psresult+filename_change(imgname,"webp")
        sizereduce.compression(source_path, result_path, is_to_png)
        result_line = dobase64(result_path)
        r = "{:.2f}".format(os.path.getsize(result_path)/1024.0)
        showlen = "img_size {}k to {}k".format(s,r)
        os.remove(result_path)
        if is_to_png and not is_ascii:
            os.remove(source_path)
    if with_md:
        result_line = _with_md(result_line,imgname)
    return result_line,showlen


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
