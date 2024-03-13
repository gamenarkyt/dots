# ArchLinux Hyprland dots

BUILDDIR=~/.build
mkdir $BUILDDIR

## Install reflector and sort mirror
sudo pacman -S reflector --noconfirm && sudo reflector -p https -c "Russia" -l 5 --sort rate --save /etc/pacman.d/mirrorlist  --verbose

## Install yay
cd $BUILDDIR && git clone https://aur.archlinux.org/yay-bin/ && cd yay-bin && makepkg -sric

## Install base utils
sudo pacman -S git bat btop neovim pfetch yt-dlp kitty --noconfirm

## Install user apps
yay -S vlc visual-studio-code-bin telegram-desktop obsidian firefox qbittorrent mpv --noconfirm
yay -S tlpui tlp


## Prog
- VSCodes
- kitty

...
