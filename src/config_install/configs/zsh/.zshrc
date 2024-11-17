# Export
export PATH=$HOME/brew/bin:$PATH
export PATH=$HOME/brew/opt:$PATH
export ZSH="$HOME/.oh-my-zsh"
export HDF5_DIR="$(brew --prefix hdf5)"
export OPENBLAS="$(brew --prefix openblas)"
export PYENV_ROOT="$HOME/.pyenv"

# oh-my-posh prompt
eval "$(oh-my-posh init zsh --config ~/.oh-my-posh/zen_config.toml)"

# oh-my-szh plugins
plugins=(git 
fast-syntax-highlighting
zsh-syntax-highlighting
zsh-autosuggestions
autojump)

# import oh-my-zsh
source $ZSH/oh-my-zsh.sh

# plugins configuration
bindkey '^I' autosuggest-accept
ZSH_AUTOSUGGEST_CLEAR_WIDGETS+=(buffer-empty bracketed-paste accept-line push-line-or-edit)
ZSH_AUTOSUGGEST_STRATEGY=(history completion)
ZSH_AUTOSUGGEST_USE_ASYNC=true

# Alias
alias vim="nvim"
alias zshconfig="vim  ~/.zshrc"
alias ohmyzsh="vim ~/.oh-my-zsh"
alias sourcerc="source ~/.zshrc"
alias h="cd $HOME"
alias cl="clear"
alias sshadd="ssh-add --apple-use-keychain ~/.ssh/id_rsa"
alias gsu="git submodule update --init --recursive"

# Functions
crepeat() {
	for i in {1..$2}
	do
		eval $1
	done
}

# Activate pyenv and autojump
if command -v pyenv 1>/dev/null 2>&1; then
 eval "$(pyenv init -)"
fi

[ -f /Users/personal/brew/etc/profile.d/autojump.sh ] && . /Users/personal/brew/etc/profile.d/autojump.sh
