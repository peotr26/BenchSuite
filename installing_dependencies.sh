#! /bin/sh

fedora() {
    sudo dnf install \
        python3 \
        dash \
        vkmark \
        glmark2
}

ubuntu() {
    sudo apt install \
        python3 \
        dash \
        vkmark \
        glmark2
}

arch() {
    sudo pacman -S \
    python \
    dash \
    vkmark \
    glmark2
}

if command -v apt-get >/dev/null 2>&1; then
ubuntu
elif command -v zypper >/dev/null 2>&1; then
fedora
elif command -v dnf >/dev/null 2>&1; then
fedora
elif command -v pacman >/dev/null 2>&1; then
arch
fi