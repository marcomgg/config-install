all: kitty_install zsh_install

kitty_install:
	uv run config-install kitty;

zsh_install:
	uv run config-install zsh;
