import pip

try:
    import subcom
except ImportError:
    pip.main(["install", "git+https://github.com/SubconsciousCompute/subcompy"])

import subcom
from loguru import logger

logger.info("Seting up devops")
cicd = subcom.CICD()
