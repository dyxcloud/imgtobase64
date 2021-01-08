import re
from urllib import request

from src import my_tool, image_mapping

http_proxy_handler = request.ProxyHandler({})
opener = request.build_opener(http_proxy_handler)
request.install_opener(opener)


def _get_name_from_url(url, content_type):
    # 文件名
    pattern = re.compile(r"\?.*")
    name = re.sub(pattern, "", url)
    # end = url.index("?")-1
    # name = url[:end]
    name = name.rpartition("/")[2]
    # 根据content type 判断文件类型
    ex = ".jpg"  # 默认类型
    if content_type in image_mapping.content_types:
        ex = image_mapping.content_types[content_type]
    else:
        for type_str in set(image_mapping.content_types.values()):
            if type_str in url:
                ex = type_str
                break
    return name + ex


def get_response_img_name(img_url):
    req = request.Request(img_url)
    response = request.urlopen(req)
    if response.getcode() == 200:
        content_type = response.headers['Content-Type']
        img_name = _get_name_from_url(img_url, content_type)
        return response, img_name
    else:
        print("request fail!")
        return None, None


def download_by_bytes(byte, filename):
    with open(filename, "wb") as f:
        f.write(byte)


def download_img(img_url):
    """下载图片"""
    response, img_name = get_response_img_name(img_url)
    filename = my_tool.psworkspace + img_name
    download_by_bytes(response.read(), filename)
    return img_name


def main():
    img_link = "https://upload-images.jianshu.io/upload_images/5831473-8898ffb67b096b56.png"
    file_name = my_tool.psworkspace + "qwe.png"
    response, img_name = get_response_img_name(img_link)
    byte_data = response.read()
    download_by_bytes(byte_data, file_name)


if __name__ == "__main__":
    main()
