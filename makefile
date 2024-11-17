CONFIG_PATH = $(HOME)/.config
KITTY_DIR_REL_PATH = kitty

backup:
	@if [ -d "$$FOLDER" ]; then \
		BAK_FOLDER="$$FOLDER"_bak; \
		echo "Backing up $$FOLDER to $$BAK_FOLDER"; \
		cp -r "$$FOLDER" "$$BAK_FOLDER"; \
		echo "Backup complete."; \
	else \
		echo "Folder $$FOLDER does not exist. Creating one"; \
		mkdir -p $(FOLDER); \
	fi
# Install target depends on backup
install:
	@$(MAKE) backup FOLDER="$(CONFIG_PATH)/$(KITTY_DIR_REL_PATH)"
	@echo "Starting installation..."
	# Add installation commands here
	@echo "Installation complete."
