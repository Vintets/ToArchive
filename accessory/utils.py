from __future__ import annotations

from datetime import datetime
import os
from pathlib import Path
import sys
import time

from . import acc_errors
from . import cprint


def check_version(version: tuple[int, int, int] = (3, 12, 0)) -> None:
    if sys.version_info < version:
        print(u'Для работы требуется версия Python %d.%d.%d и выше' % (version[0], version[1], version[2]))
        exit_from_program(code=1)
        raise Exception(u'Для работы требуется версия Python %d.%d.%d и выше' % (version[0], version[1], version[2]))


def create_dirs(path_graphlog: Path) -> None:
    if not (path_graphlog.exists() and path_graphlog.is_dir()):
        path_graphlog.mkdir()


def delete_file(filename: Path) -> None:
    """Удаляем файл"""
    if filename.exists():
        os.remove(str(filename))


def waiting_for_confirmation(msg: str = '') -> None:
    """Action confirmation
    Run:
    waiting_for_confirmation(msg=f'5Для Отправки писем введите ^9_Y : ')

    Args:
        msg (str, optional): message. Defaults to ''.

    Raises:
        acc_errors.RefusalError: Refusal action
    """
    cprint(msg, end='')
    command = input('')
    if command.lower() != 'y':
        raise acc_errors.RefusalError(f'Отмена! Операция не подтверждена') from None


def add_date_to_filename(filename: Path) -> Path:
    cur_date = datetime.today().strftime('%Y.%m.%d')
    return filename.with_name(f'{filename.stem}_{cur_date}{filename.suffix}')


def add_datetime_to_filename(filename: Path) -> Path:
    cur_time = datetime.today().strftime('%Y.%m.%d_%H.%M.%S')
    return filename.with_name(f'{cur_time}_{filename.name}')


def exit_from_program(code: int = 0, close: bool = False) -> None:
    if not close:
        input('\n{dash}   END   {dash}'.format(dash='-' * 20))
    else:
        time.sleep(1)
    try:
        sys.exit(code)
    except SystemExit:
        os._exit(code)
