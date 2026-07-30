from . import cprint


class UnsupportedResolutionError(Exception):
    """Unsupported screen resolution."""
    def __init__(self, size: tuple[int, int]) -> None:
        self.msg = f'Не поддерживаемое разрешение экрана  {size[0]} x {size[1]}'

    def logger_error(self) -> None:
        cprint(f'12{self.msg}')

    def __str__(self) -> str:
        return self.msg


class RefusalError(Exception):
    """Refusal action. Not input 'Y'."""

    pass
