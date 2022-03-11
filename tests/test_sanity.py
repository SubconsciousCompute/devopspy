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

    msbuild = find_executable("msbuilddumdum")
    assert msbuild is None


def test_msbuild():
    if not sys.platform.startswith("win"):
        pytest.skip("Windows only test", allow_module_level=True)

    msbuild = find_executable(
        "msbuild.exe", hints=["C:/Program Files (x86)"], recursive=True
    )
    logger.info(f" msbuild = {msbuild=}")
    assert msbuild.exists()
