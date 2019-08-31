# imgtobase64

将本地或web图片压缩并转为base64图片链接

下载:
[imgtobase64_v0.4_windows.zip](https://github.com/dyxcloud/imgtobase64/releases/download/0.4/imgtobase64_v0.4_windows.zip)



imgtobase64.exe启动程序

![](http://dyxmarkdown-1258036571.cos.ap-beijing.myqcloud.com/mdimg/d3447cc33e5961aa5fac1c679eaf137ece0debdf.png)

输入url点击转换, 成功后结果自动复制到系统剪贴板

![](http://dyxmarkdown-1258036571.cos.ap-beijing.myqcloud.com/mdimg/947d6c98ffaa98f847c3c4771dcf1c71c30b2ce5.png)



支持的输入格式:

.jpg;.jpeg;.png;.gif;.ico;.bmp;.webp;.tif;.tiff;.svg

支持的输出格式:

原始格式, 压缩webp, 压缩png



使用工具库:
- google libwebp-1.0.3
- pngquant.exe 2.12.0
- nconvert v7.25 + XnConvert 1.80 lib + rsvg-convert-dll-2.40.16



## TODO

1. 转换参数可配置
