#!/bin/bash
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root."
    exit 1
fi


vPWD=$(dirname $0)
vFILESYSTEM=$(df -P . | sed -n '$s/[[:blank:]].*//p')
vUUID=$(/usr/sbin/blkid -s UUID -o value "$vFILESYSTEM")


#: Dependancies.
aDEPENDS=("sudo" "libmariadb3" "libmariadb-dev" "python3.11-venv" "python3-opencv" "python3-numpy" "imagemagick")
    #: Dependancy Check
apt-get install ${aDEPENDS[*]}
if [[ $? > 0 ]]; then
    echo $sERROR"Failed to get dependancies through apt. Exiting."
    exit
else
    :
fi

#: User settings
sudo useradd -m drone
echo drone:1234 | sudo chpasswd
sudo usermod -aG sudo drone

#: Python3 Settings

cp -r -p -f "./SecurityDrone-Prototype/*" "/home/drone/"
chown -R drone:drone "/home/drone"

sudo -H -u drone bash -c 'cd "/home/drone" && python3 -m venv ".venv"'
sudo -H -u drone bash -c '/home/drone/.venv/bin/pip3 install -r mediapipe mariadb'
