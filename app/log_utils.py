"""This module defines a logging utility class.

It allows for logging both tostdout and to a local file, and allows for logging
any level of servity from DEBUG to CRITICAL. Using the stdout (default) configuration,
this will also work within Docker and with the `docker logs` command.
"""
import logging
from typing import Any


class LogUtils():
    """Logging class."""

    def __init__(self, to_console: bool=True, to_file: bool=False,
                 log_file: str='log.txt', 
                 msg_format: str='%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s') -> None:  # noqa
        """Initialize the logger object.

        Args:
            to_console: Set to True to use stdout to display the log message
            to_file:    Log output to a local file
            log_file:   File to which output will be written when to_file=True
        """
        self.to_console = to_console
        self.to_file = to_file
        self.log_file = log_file
        self.logger = self._create_logger(msg_format)

    def _create_console_handler(self, formatter: str) -> Any:
        """Define a handler to print output to console.

        Args:
            formatter:  The formatter definition to use in formatting the log output.
        Returns:
            ch:         The logging.StreamHandler object
        """
        ch = logging.StreamHandler()  # Console handler
        ch.setFormatter(formatter)
        return ch

    def _create_file_handler(self, formatter: str) -> Any:
        """Define a handler to print output to a file.

        Args:
            formatter:  The formatter definition to use in formatting the log output.
        Returns:
            fh:         The logging.FileHandler object
        """
        fh = logging.FileHandler(self.log_file, mode='a')  # File handler
        fh.setFormatter(formatter)
        return fh

    def _create_logger(self, msg_format) -> Any:
        """Create the logger object.

        Args:
            msg_format  : The format of the logger message
        Returns:
            The configured logger object.
        For other attributes, see
        https://docs.python.org/3/library/logging.html#logrecord-attributes
        """
        logger = logging.getLogger()
        if (logger.hasHandlers()):
            logger.handlers.clear()

        formatter = logging.Formatter(msg_format)

        if self.to_console:
            ch = self._create_console_handler(formatter)
            logger.addHandler(ch)
        if self.to_file:
            fh = self._create_file_handler(formatter)
            logger.addHandler(fh)
        return logger

    def log_debug(self, msg: str) -> None:
        """Write a DEBUG-level output with the configured logger.

        Args:
            msg:    The message to write
        """
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug(msg)

    def log_info(self, msg: str) -> None:
        """Write a INFO-level output with the configured logger.

        Args:
            msg:    The message to write
        """
        self.logger.setLevel(logging.INFO)
        self.logger.info(msg)

    def log_warn(self, msg: str) -> None:
        """Write a WARNING-level output with the configured logger.

        Args:
            msg:    The message to write
        """
        self.logger.setLevel(logging.WARN)
        self.logger.warn(msg)

    def log_error(self, msg: str) -> None:
        """Write a ERROR-level output with the configured logger.

        Args:
            msg:    The message to write
        """
        self.logger.setLevel(logging.ERROR)
        self.logger.error(msg)

    def log_critical(self, msg: str) -> None:
        """Write a CRITICAL-level output with the configured logger.

        Args:
            msg:    The message to write
        """
        self.logger.setLevel(logging.CRITICAL)
        self.logger.critical(msg)
