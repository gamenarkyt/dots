import subprocess, sys, os
import ascii

TMP_DIR = "/tmp/yakire/"

BASE_PKGS = "base-devel reflector bat exa btop neovim fastfetch yt-dlp gvfs gvfs-mtp"

HYPRLAND_PKGS = "hyprland waybar kitty dunst bibata-cursor-theme nwg-look catppuccin-gtk-theme-mocha rofi"

SOFTWARE_PKGS = "telegram-desktop obsidian mpv"

KDE_SETUP_PKGS = "spectacle dolphin ark kdeconnect"

FONTS_PKGS = "ttf-jetbrains-mono-nerd ttf-firacode-nerd ttf-fira-sans ttf-roboto-mono-nerd ttf-font-awesome"

def install_yay():
    print(ascii.ASCII_INSTALL_YAY)
    subprocess.run("sudo pacman -S git --noconfirm --needed", shell = True, executable="/bin/bash")
    subprocess.run(f"git clone https://aur.archlinux.org/yay-bin {TMP_DIR}yay-bin", shell = True, executable="/bin/bash")
    os.chdir(f"{TMP_DIR}yay-bin/")
    subprocess.run("makepkg -sric --noconfirm --needed", shell = True, executable="/bin/bash")

def install_chaotic_aur():
    with open("/etc/pacman.conf", "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip() == "[chaotic-aur]":
                return
    subprocess.run("sudo pacman-key --recv-key 3056513887B78AEB --keyserver keyserver.ubuntu.com --noconfirm", shell = True, executable="/bin/bash")
    subprocess.run("sudo pacman-key --lsign-key 3056513887B78AEB --noconfirm", shell = True, executable="/bin/bash")
    subprocess.run("sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-keyring.pkg.tar.zst' --noconfirm", shell = True, executable="/bin/bash")
    subprocess.run("sudo pacman -U 'https://cdn-mirror.chaotic.cx/chaotic-aur/chaotic-mirrorlist.pkg.tar.zst' --noconfirm", shell = True, executable="/bin/bash")

    subprocess.run("sudo chmod 777 /etc/pacman.conf", shell = True, executable="/bin/bash")
    subprocess.run("sudo echo \"\n[chaotic-aur]\nInclude = /etc/pacman.d/chaotic-mirrorlist\n\" >> /etc/pacman.conf", shell = True, executable="/bin/bash")
    subprocess.run("sudo chmod 644 /etc/pacman.conf", shell = True, executable="/bin/bash")
    



def clear():
    out = subprocess.run("clear", shell = True, executable="/bin/bash")

def installPKG(pkgs):
    print(ascii.ASCII_INSTALL_DEPENDENCIES)
    out = subprocess.run(f"yay -S {pkgs} --noconfirm --needed --quiet", shell = True, executable="/bin/bash")

def reflector():
    out = subprocess.run("sudo reflector -p https -c \"Germany\" -l 5 --sort rate --save /etc/pacman.d/mirrorlist  --verbose --download-timeout 20", shell = True, executable="/bin/bash")


def main():
    # Setup env
    subprocess.run(f"mkdir {TMP_DIR}", shell = True, executable="/bin/bash")
    os.chdir(TMP_DIR)
    # install_chaotic_aur()

    # subprocess.run("cat /etc/pacman.conf", shell=True, executable="/bin/bash", check=True, stdout=PIPE).stdout
    # print("out", subprocess.check_output())

    # install_yay()
    # reflector()
    # installPKG(BASE_PKGS)
    # installPKG(KDE_SETUP_PKGS)
    # installPKG(SOFTWARE_PKGS)
    installPKG(FONTS_PKGS)


if __name__ == "__main__":
    clear()
    main()
    # clear()
    print(ascii.ASCII_INSTALL_DONE)
    print("\nRun yay -Syyuu\n")
