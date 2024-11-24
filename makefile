all: kitty_install zsh_install

kitty_install:
	uv run config-install kitty;

zsh_install:
	uv run config-install zsh;

oh_my_posh_install:
	uv run config-install oh-my-posh
