
def read_file(flle_name):
    try:
        with open(flle_name, 'r', encoding='utf8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print('文件未找到')


def write_file(flle_name, data):
    with open(flle_name, 'w', encoding='utf8') as file:
        file.write(data)
        file.close()
