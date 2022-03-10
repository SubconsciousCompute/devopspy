"""
Sanity tests.
"""

__author__           = "Dilawar Singh"
__email__            = "dilawar@subcom.tech"

import pytest

import subcom
from loguru import logger

def test_sanity():
    a = subcom.DevOps()
    assert a

def test_find_executable():
    """This may pass on developer machine.
    """
    from subcom.command import find_executable
    cmake = find_executable("cmake")
    assert cmake is not None and cmake.exists()

    msbuild = find_executable("msbuilddumdum")
    assert msbuild is None

    msbuild = find_executable("msbuild.exe", hints=["C:/Program Files (x86)"], recursive=True)
    logger.info(f" msbuild = {msbuild=}")
    assert msbuild.exists()
