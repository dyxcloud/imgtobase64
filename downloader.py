import re
import urllib.request

import mytool
import imagemapping



def _get_name_from_url(url,contenttype):
    #文件名
    pattern = re.compile(r"\?.*")
    name = re.sub(pattern,"",url)
    # end = url.index("?")-1
    # name = url[:end]
    name = name.rpartition("/")[2]
    # 根据content type 判断文件类型
    if contenttype in imagemapping.content_types:
        ex = imagemapping.content_types[contenttype]
    else:
        for type in set(imagemapping.content_types.values()):
            if type in url:
                ex = type
                break
    return name+ex

def get_response_imgname(img_url):
    request = urllib.request.Request(img_url)
    response = urllib.request.urlopen(request)
    if (response.getcode() == 200):
        contenttype = response.headers['Content-Type']
        img_name = _get_name_from_url(img_url,contenttype)
        return response,img_name
    else:
        print("request fail!")
        return None,None

def download_by_bytes(bytes,filename):
    with open(filename, "wb") as f:
        f.write(bytes)

def download_img(img_url):
    '''下载图片'''
    response,img_name = get_response_imgname(img_url)
    filename = mytool.psworkspace + img_name
    download_by_bytes(response,filename)
    return img_name


if __name__ == "__main__":
    name = _get_name_from_url("https://upload-images.jianshu.io/upload_images/5831473-8898ffb67b096b56.png","")
    print(name)
    # print(imagemapping.content_types.values)
    