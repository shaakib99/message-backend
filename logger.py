import logging
from dataclasses import dataclass, field
from abc import ABC, abstractmethod


class LogABC(ABC):
    @abstractmethod
    def log(self) -> None:
        pass


@dataclass(order=False)
class Logger(LogABC):
    message: str
    save_to_file: bool = field(default=False)
    log_file_name: str = field(default="log.log")
    logger: logging.Logger = field(default=logging.getLogger("default"))
    __date_format: str = field(init=False, default="%d-%b-%y %H:%M:%S")
    __log_format: str = field(
        init=False, default="[%(asctime)s - %(levelname)s] - %(message)s"
    )
    log_level: int = field(init=False, default=logging.DEBUG)

    def __post_init__(self):
        self.logger.setLevel(self.log_level)
        if self.save_to_file:
            logging.basicConfig(
                format=self.__log_format,
                datefmt=self.__date_format,
                filemode="a",
                filename=self.log_file_name,
            )
        else:
            logging.basicConfig(format=self.__log_format, datefmt=self.__date_format)

    def log(self) -> None:
        return self.logger.log(level=self.log_level, msg=self.message)


def log(logger: Logger) -> None:
    return logger.log()
