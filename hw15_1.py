import argparse
from collections import namedtuple
import os
import logging

FORMAT = ("{asctime} - {levelname}: {msg}")

logging.basicConfig(filename='file_list.txt', filemode='w', format=FORMAT, style='{', level=logging.NOTSET)
common_log = logging.getLogger()

FSObject = namedtuple('FSObject', 'name ext is_dir parent', defaults=['', '', False, ''])  

def walk_dir(path_string: str):
    fs_objects = []
    if not path_string:
        path_string = os.getcwd()
        common_log.warning(f'Путь установлен по умолчанию {path_string}')
    path_string = os.path.abspath(path_string)
    parent = path_string.rstrip('/').rsplit('/', 1)[1]        
    for item in os.listdir(path_string):
        obj_name, obj_ext = None, None
        item: str = item.rsplit('/',1)[1]
        if item.rfind('.') != -1 and not item.startswith('.'):
            obj_name, obj_ext = item.rsplit('.', 1)
        else:
            obj_name = item
        fs_objects.append(FSObject(name=obj_name, ext=obj_ext, parent=parent, is_dir=False))
        fs_objects.append(FSObject(name=obj_name, ext=obj_ext, is_dir=False))
    common_log.info(msg=str(fs_objects[-1]))

    return fs_objects 


def parse_ars():
    parser = argparse.ArgumentParser(description="path parser")
    parser.add_argument('-p', metavar='path', type=str, nargs='*', default='.', help='введите путь к директории')
    args = parser.parse_args()
    return args.p

def main():
    for place in parse_ars():
        for item in (walk_dir(place)):
            print(repr(item))

if __name__ == '__main__':
    main()

