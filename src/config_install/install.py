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
    ZSH = "zsh"
    OH_MY_POSH = "oh-my-posh"


def backup_and_remove_path(path: Path):
    if path.exists():
        backup_path = path.with_suffix(BACKUP_SUFFIX)
        if backup_path.is_dir():
            shutil.rmtree(backup_path)
        if backup_path.is_file():
            backup_path.unlink()

        logger.info(f"Backing up configs {path} to {backup_path}")

        if path.is_file():
            shutil.copy(path, backup_path)
        else:
            shutil.copytree(path, backup_path)
        path.unlink()


def install_kitty():
    logger.info(f"Installing {ConfigType.KITTY} configs")
    kitty_dir_name = "kitty"
    kitty_configs_dir = REFERENCE_CONFIGS_DIR / kitty_dir_name
    dst_config_dir = CONFIG_DIR / kitty_dir_name
    dst_config_dir.mkdir(exist_ok=True)
    backup_and_remove_path(dst_config_dir)

    logger.info(f"Creating symlink to {dst_config_dir} pointing to {kitty_configs_dir}")
    os.symlink(kitty_configs_dir, dst_config_dir)


def install_zsh():
    logger.info(f"Installing {ConfigType.ZSH} configs")
    zshrc_file_path = REFERENCE_CONFIGS_DIR / "zsh" / ".zshrc"
    dst_zshrc_file_path = HOME_DIR / ".zshrc"

    backup_and_remove_path(dst_zshrc_file_path)
    logger.info(
        f"Creating symlink to {dst_zshrc_file_path} pointing to {zshrc_file_path}"
    )
    os.symlink(zshrc_file_path, dst_zshrc_file_path)


def install_oh_my_posh():
    logger.info(f"Installing {ConfigType.OH_MY_POSH}")
    oh_my_posh_configs_dir_path = REFERENCE_CONFIGS_DIR / "oh-my-posh"
    dst_oh_my_posh_configs_dir_path = HOME_DIR / ".oh-my-posh"
    dst_oh_my_posh_configs_dir_path.mkdir(exist_ok=True)
    zen_config_file_name = "zen_config.toml"

    backup_and_remove_path(dst_oh_my_posh_configs_dir_path / zen_config_file_name)
    logger.info(
        f"Creating symlink to {oh_my_posh_configs_dir_path / zen_config_file_name} pointing to {dst_oh_my_posh_configs_dir_path / zen_config_file_name}"
    )
    os.symlink(
        oh_my_posh_configs_dir_path / zen_config_file_name,
        dst_oh_my_posh_configs_dir_path / zen_config_file_name,
    )


def install(config_type: str):
    config_type_enum = ConfigType(config_type)

    match config_type_enum:
        case ConfigType.KITTY:
            install_kitty()
        case ConfigType.ZSH:
            install_zsh()
        case ConfigType.OH_MY_POSH:
            install_oh_my_posh()
