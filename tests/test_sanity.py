"""
Sanity tests.
"""

__author__ = "Dilawar Singh"
__email__ = "dilawar@subcom.tech"

import sys

import pytest

from loguru import logger

import subcom
from subcom.command import find_executable


def test_find_executable():
    """This may pass on developer machine."""
    cmake = find_executable("cmake")
    assert cmake is not None and cmake.exists()

    py = find_executable("python")
    assert py is not None and py.exists()

    dummy = find_executable("msbuilddumdum")
    assert dummy is None


def test_msbuild():
    if not subcom.common.is_windows():
        logger.warning(f"Not windows {sys.platform=}")
        pytest.skip("Windows only test", allow_module_level=True)

    logger.debug("test_msbuild")
    subcom.install.ensure_visual_studio()

    msbuild = find_executable(
        "msbuild.exe", hints=["C:/Program Files (x86)"], recursive=True
    )
    logger.info(f" msbuild = {msbuild=}")
    assert msbuild is not None and msbuild.exists()
