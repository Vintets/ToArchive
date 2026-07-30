#!/usr/bin/env python

"""
Added date to name file and added file to archive.

/*******************************************************
 * Copyright 2026 Vintets <programmer@vintets.ru> - All Rights Reserved
 * Written by Vintets <programmer@vintets.ru>, July 2026
*******************************************************/

# for python 3.12.0 and over
"""


from functools import lru_cache
# import json
from pathlib import Path
import sys
import tomllib
from typing import Any

from __about__ import __author__, __copyright__, __title__, __version__
from accessory import (add_date_to_filename, authorship, check_version, cprint,
                       create_dirs, exit_from_program, init_console, logger)
import errors as err
import py7zr


CONFIG_FILE = 'config.toml'
CONFIG_SECTION = 'main'


def get_transferred_argument() -> str:
    try:
        arg = sys.argv[1]
    except IndexError:
        raise err.ArgumentNotPassedError()  # from None
    return arg


def validate_transferred_argument(arg: str) -> Path:
    file_in = Path(arg)
    if not file_in.exists():
        raise err.FileNotExistError(str(file_in))
    elif not file_in.is_file():
        raise err.NotFileError(str(file_in))
    return file_in


@lru_cache
def read_config(target_path: Path) -> dict[str, Any]:
    try:
        with open(target_path.joinpath(CONFIG_FILE), 'rb') as f:
            conf_data = tomllib.load(f)
            config: dict[str, Any] = conf_data[CONFIG_SECTION]
    except FileNotFoundError:
        print('Файл конфига не найден')
        config = {}
    except KeyError:
        raise err.NotSECTIONError(CONFIG_SECTION, tuple(conf_data.keys()))
    return config


def parse_config(config: dict[str, Any], target_path: Path) -> dict[str, Any]:
    config['output_folder'] = target_path.joinpath(config.get('path_to_archive', ''))
    print_config(config)
    return config


def print_config(config: dict[str, Any]) -> None:
    # config_str = {key: str(value) for key, value in config.items()}
    # print(json.dumps(config_str, indent=4, ensure_ascii=False))
    # print(f'{config=}')
    print(f'{CONFIG_FILE}')
    for key, value in config.items():
        print(f"    '{key}': '{str(value)}'")


def add_to_archive(config: dict[str, Any], cur_name: Path, new_name: Path) -> Path:
    output_folder: Path = config['output_folder']
    create_dirs(output_folder)
    archive_name = str(config.get('archive_name', ''))
    arch_name = archive_name if archive_name != '' else cur_name.stem
    archive = output_folder.joinpath(f'{arch_name}.7z')
    try:
        with py7zr.SevenZipFile(archive, 'a') as arch:
            arch.write(cur_name, arcname=new_name.name)
    except PermissionError:
        raise err.FileIsLockedError(str(archive))
    return archive


def main() -> None:
    arg = get_transferred_argument()
    cur_name = validate_transferred_argument(arg)
    target_path = cur_name.parent
    config = parse_config(read_config(target_path), target_path=target_path)
    new_name = add_date_to_filename(cur_name)
    cprint(f'20Архивируем файл ^14_{str(cur_name)} ^20_с новым именем ^13_{str(new_name.name)}')
    archive = add_to_archive(config, cur_name=cur_name, new_name=new_name)
    logger.info(f'Файл {str(cur_name.name)} добавлен в архив {str(archive)}')


if __name__ == '__main__':
    init_console(width=120, hight=50)
    check_version(version=(3, 12, 0))
    PATH_SCRIPT = Path(__file__).parent
    # print(f'PATH_SCRIPT {PATH_SCRIPT}')
    # os.chdir(PATH_SCRIPT)
    print(Path.cwd())

    authorship(__author__, __title__, __version__, __copyright__)  # width=_width

    try:
        main()
    except KeyboardInterrupt:
        logger.info('Отмена. Скрипт остановлен.')
        exit_from_program(code=0)
    except (err.ArgumentNotPassedError,
            err.FileNotExistError,
            err.NotFileError,
            err.FileIsLockedError,
            ) as e:
        logger.error(e)
        err.process_critical_exception()
    except Exception as e:
        logger.critical(e)  # __str__()
        # raise e
        err.process_critical_exception()
    # input()
    exit_from_program(code=0, close=True)
