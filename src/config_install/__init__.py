import logging

import clize
from config_install.install import install


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S",
        format="%(levelname)s: %(asctime)s - [%(filename)s:%(lineno)d] - %(message)s",
    )
    clize.run(install)
