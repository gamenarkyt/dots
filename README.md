# ArchLinux Hyprland dots

BUILDDIR=~/.build
mkdir $BUILDDIR

## Install reflector and sort mirror
```bash
sudo pacman -S reflector --noconfirm && sudo reflector -p https -c "Russia" -l 5 --sort rate --save /etc/pacman.d/mirrorlist  --verbose
```

## Install yay
```bash
cd $BUILDDIR && git clone https://aur.archlinux.org/yay-bin/ && cd yay-bin && makepkg -sric
```

## Install base utils
```bash
yay -S git bat btop neovim pfetch yt-dlp kitty --noconfirm
```

## Install user apps
```bash
yay -S vlc visual-studio-code-bin telegram-desktop obsidian firefox qbittorrent mpv --noconfirm
yay -S tlpui tlp
```

## Fonts
```bash
yay -S noto-fonts-sc ttf-jetbrains-mono-nerd ttf-firacode-nerd --noconfirm
```
## Prog
- VSCodes
- kitty

...
