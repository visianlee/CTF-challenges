def delete_blank_lines(file_path, encoding='utf-8'):
    with open(file_path, 'r', encoding=encoding) as f:
        lines = f.readlines()
    non_blank_lines = [line for line in lines if line.strip()]
    with open(file_path, 'w', encoding=encoding) as f:
        f.writelines(non_blank_lines)

# 尝试使用不同的编码
encodings = ['utf-8', 'iso-8859-1', 'windows-1252', 'gbk']
for encoding in encodings:
    try:
        delete_blank_lines('usbdata.txt', encoding)
        print(f'Successfully processed with encoding: {encoding}')
        break
    except UnicodeDecodeError:
        print(f'Failed to process with encoding: {encoding}')