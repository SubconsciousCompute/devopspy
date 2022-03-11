__author__ = "Dilawar Singh"
__email__ = "dilawar@subcom.tech"

import typing as T
import platform
import sys


def system() -> T.Tuple[str, str]:
    return (platform.system(), sys.platform)


def is_windows(cygwin_is_windows: bool = True) -> bool:
    """Check if we are running on windows.

    Parameters
    ----------
        cygwin_is_windows : (default `True`). When set to `True`, consider cygwin as Windows.

    Returns
    -------
    `True` if on Windows, `False` otherwise.
    """
    _sys = system()
    if _sys[0].startswith("windows"):
        return True
    return cygwin_is_windows and _sys[1] == "cygwin"
