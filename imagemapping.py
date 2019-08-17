
selectfiletypes = '*.jpg;*.jpeg;*.png;*.gif;*.ico;*.bmp;*.webp;*.tif;*.tiff;*.svg'

content_types = {
    'image/jpeg':'.jpg',
    'application/x-jpg':'.jpg',
    'application/x-png':'.png',
    'image/png':'.png',
    'image/gif':'.gif',
    'image/x-icon':'.ico',
    'application/x-ico':'.ico',
    'image/bmp':'.bmp',
    'image/webp':'.webp',
    'image/tiff':'.tif',
    'application/x-tif':'.tif',
    'image/svg+xml':'.svg',
    'text/xml':'.svg'
}

base64headers = {
    '.jpg': "data:image/jpeg;base64,",
    '.png': "data:image/png;base64,",
    '.gif': "data:image/gif;base64,",
    '.ico': "data:image/x-icon;base64,",
    '.bmp':'data:image/bmp;base64,',
    '.webp': "data:image/webp;base64,",
    '.tif':"data:image/tiff;base64,",
    '.tiff':"data:image/tiff;base64,",
    '.svg':"data:image/svg+xml;base64,"
}