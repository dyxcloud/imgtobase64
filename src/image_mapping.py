select_file_types = '*.jpg;*.jpeg;*.png;*.gif;*.ico;*.bmp;*.webp;*.tif;*.tiff;*.svg'

content_types = {
    'image/jpeg': '.jpg',
    'application/x-jpg': '.jpg',
    'application/x-png': '.png',
    'image/png': '.png',
    'image/gif': '.gif',
    'image/x-icon': '.ico',
    'application/x-ico': '.ico',
    'image/bmp': '.bmp',
    'image/webp': '.webp',
    'image/tiff': '.tif',
    'application/x-tif': '.tif',
    'image/svg+xml': '.svg',
    'text/xml': '.svg'
}

base64headers = {
    '.jpg': "data:image/jpeg;base64,",
    '.png': "data:image/png;base64,",
    '.gif': "data:image/gif;base64,",
    '.ico': "data:image/x-icon;base64,",
    '.bmp': 'data:image/bmp;base64,',
    '.webp': "data:image/webp;base64,",
    '.tif': "data:image/tiff;base64,",
    '.tiff': "data:image/tiff;base64,",
    '.svg': "data:image/svg+xml;base64,"
}

file_headers = {
    "68746D6C3E": 'html',
    "D0CF11": 'xls',
    "44656C69766572792D64": 'eml',
    'ffd8ff': 'jpg',
    '89504e470d0a1a0a0000': 'png',
    '47494638396126026f01': 'gif',
    '49492a00227105008037': 'tif',
    '424d228c010000000000': 'bmp',
    '424d8240090000000000': 'bmp',
    '424d8e1b030000000000': 'bmp',
    '41433130313500000000': 'dwg',
    '3c21444f435459504520': 'html',
    '3c21646f637479706520': 'htm',
    '48544d4c207b0d0a0942': 'css',
    '696b2e71623d696b2e71': 'js',
    '7b5c727466315c616e73': 'rtf',
    '38425053000100000000': 'psd',
    '46726f6d3a203d3f6762': 'eml',
    'D0CF11E0': 'doc',
    'd0cf11e0a1b11ae10000': 'vsd',
    '5374616E64617264204A': 'mdb',
    '252150532D41646F6265': 'ps',
    '255044462d312e350d0a': 'pdf',
    '2e524d46000000120001': 'rmvb',
    '464c5601050000000900': 'flv',
    '00000020667479706d70': 'mp4',
    '49443303000000002176': 'mp3',
    '000001ba210001000180': 'mpg',
    '3026b2758e66cf11a6d9': 'wmv',
    '52494646e27807005741': 'wav',
    '52494646d07d60074156': 'avi',
    '4d546864000000060001': 'mid',
    '504b0304140000080044': 'zip',
    '504b03040a0000080000': 'zip',
    '504B3030': 'zip',
    '526172211a0700cf9073': 'rar',
    '235468697320636f6e66': 'ini',
    '504b03040a0000000000': 'jar',
    '4d5a9000030000000400': 'exe',
    '3c25402070616765206c': 'jsp',
    '4d616e69666573742d56': 'mf',
    '3c3f786d6c2076657273': 'xml',
    '494e5345525420494e54': 'sql',
    '7061636b616765207765': 'java',
    '406563686f206f66660d': 'bat',
    '1f8b0800000000000000': 'gz',
    '6c6f67346a2e726f6f74': 'properties',
    'cafebabe0000002e0041': 'class',
    '49545346030000006000': 'chm',
    '04000000010000001300': 'mxp',
    '504b0304140006000800': 'docx',
    '6431303a637265617465': 'torrent',
}

file_header_png = "89504E47"
