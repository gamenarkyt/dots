# ArchLinux dots

## Install reflector and sort mirror
```bash
sudo pacman -S reflector --noconfirm && sudo reflector -p https -c "Russia" -l 5 --sort rate --save /etc/pacman.d/mirrorlist  --verbose
```

## Install yay
```bash
git clone https://aur.archlinux.org/yay-bin/ && cd yay-bin && makepkg -sric
```

## Install base utils
```bash
yay -S git z exa bat btop neovim fastfetch yt-dlp pipewire pipewire-pulse gvfs gvfs-mtp --noconfirm
```

## Install user apps
```bash
yay -S vlc code telegram-desktop obsidian firefox transmission power-profiles-daemon mpv nemo nemo-fileroller --noconfirm
```

## Chaotic aur
```bash
sudo -i
pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com
pacman-key --lsign-key 3056513887B78AEB
pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst'
pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst'

Append (adding to the end of the file) to /etc/pacman.conf:

[chaotic-aur]
Include = /etc/pacman.d/chaotic-mirrorlist 
```
## Hyprland
```bash
yay -S hyprland-git waybar kitty dunst bibata-cursor-theme nwg-look catppuccin-gtk-theme-mocha rofi --noconfirm
```
## Configure zsh
```bash
yay -S zsh zsh-autosuggestions zsh-completions zsh-syntax-highlighting zsh-history-substring-search 

sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

git clone https://github.com/zsh-users/zsh-autosuggestions.git $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
git clone https://github.com/zdharma-continuum/fast-syntax-highlighting.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/plugins/fast-syntax-highlighting
git clone --depth 1 -- https://github.com/marlonrichert/zsh-autocomplete.git $ZSH_CUSTOM/plugins/zsh-autocomplete
git clone https://github.com/agkozak/zsh-z ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-z


```


## Install Fonts
```bash
yay -S ttf-jetbrains-mono-nerd ttf-firacode-nerd ttf-roboto-mono-nerd ttf-font-awesome --noconfirm

yay -S noto-fonts-sc --noconfirm
```

## Mount btrfs on liveusb archlinux
```bash
mount -o compress=zstd,subvol=@ /dev/nvme0n1p2 /mnt
mount /dev/nvme0n1p1 /mnt/boot
```
