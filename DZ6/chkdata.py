""" Запуск модуля проверки даты из коммандной строки"""

from task_021 import check_data as chkd
from sys import argv

if __name__ == '__main__':
    chkd(argv[1])