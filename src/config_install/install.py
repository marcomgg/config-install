import logging
import os
import shutil
from enum import StrEnum
from pathlib import Path

HOME_DIR = Path.home()
CONFIG_DIR = HOME_DIR / ".config"

REFERENCE_CONFIGS_DIR = Path(__file__).parent / "configs"
BACKUP_SUFFIX = ".bak"

logger = logging.getLogger(__name__)


class ConfigType(StrEnum):
    KITTY = "kitty"


def backup_and_remove_directory(dir_path: Path):
    if dir_path.exists():
        logger.info(f"Backing up configs directory {dir_path}")
        backup_path = dir_path.with_suffix(BACKUP_SUFFIX)
        shutil.rmtree(backup_path)
        shutil.copytree(dir_path, backup_path)
        dir_path.unlink()


def install_kitty():
    logger.info(f"Installing {ConfigType.KITTY} configs")
    kitty_dir_name = "kitty"
    kitty_configs_dir = REFERENCE_CONFIGS_DIR / kitty_dir_name
    dst_config_dir = CONFIG_DIR / kitty_dir_name

    backup_and_remove_directory(dst_config_dir)

    logger.info(f"Creating symlink to {dst_config_dir} pointing to {kitty_configs_dir}")
    os.symlink(kitty_configs_dir, dst_config_dir)


def install(config_type: str):
    config_type_enum = ConfigType(config_type)

    match config_type_enum:
        case ConfigType.KITTY:
            install_kitty()
