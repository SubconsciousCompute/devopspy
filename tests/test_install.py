__author__ = "Dilawar Singh"
__email__ = "dilawar@subcom.tech"

import subcom.install
import subcom.common

from loguru import logger


def test_ensure():
    logger.info("Running test_ensure")
    if subcom.common.is_windows():
        subcom.install.ensure_choco()
    subcom.install.ensure_cmake()
