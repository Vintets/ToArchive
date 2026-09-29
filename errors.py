import os

from accessory import cprint


def process_critical_exception(message: str | None = None) -> None:
    """Prints message, describing critical situation, and exit."""

    if message is not None:
        print(message)
    cprint('14\n{dash}   ^12_ERROR   ^14_{dash}'.format(dash='-' * 20))
    input()
    os._exit(1)


class ArgumentNotPassedError(Exception):
    """Error argument not passed."""
    def __init__(self) -> None:
        self.msg = f'Не передан файл для обработки!'

    def __str__(self) -> str:
        return self.msg


class ArgumentIsNotFileError(Exception):
    """Error this is not a file."""
    def __init__(self, arg: str) -> None:
        super().__init__(arg)
        self.msg = f"Передан не файл! '{arg}'"

    def __str__(self) -> str:
        return self.msg


class FileNotExistError(Exception):
    """Error argument file not exist."""
    def __init__(self, file_in: str, ext_info: str = '') -> None:
        super().__init__(file_in, ext_info)
        self.msg = f"{ext_info}Файл '{file_in}' не существует!"

    def __str__(self) -> str:
        return self.msg


class NotSECTIONError(Exception):
    """Error Not section in config file."""
    def __init__(self, given_section: str, found_sections: tuple[str, ...]) -> None:
        super().__init__(given_section, found_sections)
        self.msg = f"Секция '{given_section}' не найдена в config.toml. Найдены {found_sections}"

    def __str__(self) -> str:
        return self.msg


class FileIsLockedError(Exception):
    """File is locked error."""
    def __init__(self, filename: str) -> None:
        super().__init__(filename)
        self.msg = f"Файл '{filename}' заблокирован!"

    def __str__(self) -> str:
        return self.msg


class SaveError(Exception):
    """Error save file."""
    def __init__(self, filename: str) -> None:
        super().__init__(filename)
        self.msg = f'Ошибка сохранения файла {filename}'

    def __str__(self) -> str:
        return self.msg
