"""
Command module.
"""

__author__ = "Dilawar Singh"
__email__ = "dilawar@subcom.tech"

import subprocess
import shutil
import itertools
import functools

import typing as T

from pathlib import Path
from loguru import logger


def find_executable(
    cmd: str,
    *,
    hints: list[T.Union[str, Path]] = [],
    subdirs: list[str] = [],
    recursive: bool = False,
) -> T.Optional[Path]:
    """Find an executable.

    Parameters
    ----------
        cmd : name of the command. On windows, we also search for `foo.exe` if `foo` is given.
        hints : List of directories in addition to `PATH` where we search for executable.
        subdirs : List of subdirs. Each subdir is suffixed to every hints.
        recursive : If recursive is set to `True`, search as deep as possible to find the executable
        file.

    Returns
    -------

    Path of the executable if found, `None` otherwise.

    """

    winname = f"{cmd}.exe" if not cmd.endswith(".exe") else cmd

    # We full path is given, return it.
    for cmd in (cmd, winname):
        if p := Path(cmd):
            if p.exists():
                return p

    c = shutil.which(cmd)
    if c is not None:
        return Path(c)

    # search in hints and subdirs. Try to mimic cmake's find_command macro.
    subdirs.append(".")
    for hint, subdir in itertools.product(hints, subdirs):
        e = Path(hint) / subdir
        assert e.exists(), f"{str(e)} doesn't exists"
        logger.debug(f" Searching in {str(e)}")
        if not e.exists():
            continue
        if e.is_file() and (e.name == cmd or e.name == winname):
            return e
        if recursive and e.is_dir():
            if fs := list(e.glob(f"**/{cmd}")) + list(e.glob(f"**/{winname}")):
                if fs:
                    return fs[0]
    return None
