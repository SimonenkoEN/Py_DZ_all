# Задание 1
#  Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
#  Соберите информацию о содержимом в виде объектов namedtuple.
#  Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
#  В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import os
import argparse
import logging
from collections import namedtuple

logging.basicConfig(level=logging.INFO, filename='log_dz1.txt', filemode='w', encoding='utf-8')
logger = logging.getLogger(__name__)

data = namedtuple(typename='data', field_names='obj_name, ext, flag, parrent_dir')


def directory_list(dir_path: str = os.getcwd()) -> None:
    os.chdir(dir_path)
    parrent_name = os.getcwd().rsplit(os.path.sep, maxsplit=1)[1]
    for obj in os.listdir():
        if os.path.isfile(obj):
            tmp = (obj.rsplit('.', maxsplit=1))
            obj_info = data(tmp[0], tmp[1], 'file', parrent_name)
        else:
            obj_info = data(obj, '', 'DIR', parrent_name)
        logger.info(obj_info)


def pars():
    parser = argparse.ArgumentParser(prog='dz_s15d1.py', description='Get directory info')
    parser.add_argument('-p', '--path', default=os.getcwd(), type=str, help='Path to directory')
    args = parser.parse_args()
    logger.info(args.path)
    return directory_list(args.path)


if __name__ == '__main__':
    pars()