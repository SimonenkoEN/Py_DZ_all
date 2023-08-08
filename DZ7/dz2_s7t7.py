# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

__all__ = ['sort_file']

import os
from pathlib import Path


EXT_VIDEO = ['avi', 'flv', 'mkv', 'mov', 'mp4', 'mpg', 'mpeg', 'swf', 'vid', 'wmv'] 
EXT_AUDIO = ['aud', 'mid', 'midi', 'mp3', 'ogg', 'wav', 'wma']
EXT_PICTURE = ['bmp', 'gif', 'ico', 'jpg', 'jpeg', 'png', 'psd', 'tiff', 'swg', 'emf', 'wmf', ]
EXT_TEXT = ['txt', 'doc', 'pdf']

DIR_VIDEO = '1_Videos'
DIR_AUDIO = '2_Audios'
DIR_PICTURE = '3_Pictures'
DIR_TEXT = '4_Texts'


def sort_file(folder: str = None) -> None:
    if folder != None:
        os.chdir(folder)
    if not DIR_VIDEO in os.listdir():
        Path(DIR_VIDEO).mkdir()
    if not DIR_AUDIO in os.listdir():
        Path(DIR_AUDIO).mkdir()
    if not DIR_PICTURE in os.listdir():
        Path(DIR_PICTURE).mkdir()
    if not DIR_TEXT in os.listdir():
        Path(DIR_TEXT).mkdir()
    cur_path = Path(Path().cwd())
    for obj in cur_path.iterdir():
        if obj.is_file():
            file_path, file_name = str(obj).rsplit('\\', maxsplit=1)
            file_ext = file_name.rsplit('.', maxsplit=1)[1]
            if file_ext in EXT_VIDEO:
                Path(file_name).replace(Path.cwd() / DIR_VIDEO / Path(file_name))
            if file_ext in EXT_AUDIO:
                Path(file_name).replace(Path.cwd() / DIR_AUDIO / Path(file_name))
            if file_ext in EXT_PICTURE:
                Path(file_name).replace(Path.cwd() / DIR_PICTURE / Path(file_name))
            if file_ext in EXT_TEXT:
                Path(file_name).replace(Path.cwd() / DIR_TEXT / Path(file_name))


if __name__ == '__main__':
    sort_file()