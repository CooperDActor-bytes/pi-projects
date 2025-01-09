#!/bin/bash

# Update and upgrade the system
sudo apt-get update && sudo apt-get upgrade -y

# Install dependencies for all projects
sudo apt-get install -y git curl build-essential make libraspberrypi-dev docker docker-compose

# Function to install FM Transmitter
install_fm_transmitter() {
    echo "Installing FM Transmitter..."
    git clone https://github.com/markondej/fm_transmitter
    cd fm_transmitter
    make
    echo "FM Transmitter installed. Run using: sudo ./fm_transmitter -f <frequency> <file.wav>"
    cd ..
}

# Function to install FreeTube
install_freetube() {
    echo "Installing FreeTube..."
    flatpak install -y flathub io.freetubeapp.FreeTube
    echo "FreeTube installed. Run using Flatpak: flatpak run io.freetubeapp.FreeTube"
}

# Function to install Gitea
install_gitea() {
    echo "Installing Gitea..."
    wget -O gitea https://dl.gitea.io/gitea/1.19.3/gitea-1.19.3-linux-amd64
    chmod +x gitea
    sudo mv gitea /usr/local/bin/
    echo "Gitea installed. Run using: gitea web"
}

# Function to install Kodi
install_kodi() {
    echo "Installing Kodi..."
    sudo apt-get install -y kodi
    echo "Kodi installed. Run using: kodi"
}

# Function to install PiVPN
install_pivpn() {
    echo "Installing PiVPN..."
    curl -L https://install.pivpn.io | bash
    echo "PiVPN installed. Configure using: pivpn"
}

# Function to set up WordPress with Docker
setup_wordpress_docker() {
    echo "Setting up WordPress with Docker..."
    curl -sSL get.docker.com | sh
    curl -s https://packagecloud.io/install/repositories/Hypriot/Schatzkiste/script.deb.sh | sudo bash
    sudo apt-get update && sudo apt-get install -y docker-compose
    git clone https://github.com/your-repo/wordpress-docker
    cd wordpress-docker
    docker-compose up
    echo "WordPress setup complete. Access it locally at http://localhost"
}

# Main menu
PS3='Please select an option to install: '
options=(
    "FM Transmitter"
    "FreeTube"
    "Gitea"
    "Kodi"
    "PiVPN"
    "WordPress (Docker)"
    "Quit"
)
select opt in "${options[@]}"; do
    case $opt in
        "FM Transmitter")
            install_fm_transmitter
            ;;
        "FreeTube")
            install_freetube
            ;;
        "Gitea")
            install_gitea
            ;;
        "Kodi")
            install_kodi
            ;;
        "PiVPN")
            install_pivpn
            ;;
        "WordPress (Docker)")
            setup_wordpress_docker
            ;;
        "Quit")
            break
            ;;
        *)
            echo "Invalid option $REPLY"
            ;;
    esac
    echo "\nReturning to the main menu..."
done
