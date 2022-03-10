__author__ = "Dilawar Singh"
__email__ = "dilawar@subcom.tech"

import platform


def is_windows() -> bool:
    return platform.system().startswith("win")
