#!/bin/bash
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root."
    exit 1
fi


vPWD=$(dirname $0)
vFILESYSTEM=$(df -P . | sed -n '$s/[[:blank:]].*//p')
vUUID=$(/usr/sbin/blkid -s UUID -o value "$vFILESYSTEM")

#: Dependancies.
aDEPENDS=("sudo" "cmake" "libmariadb3" "mariadb-server" "build-essential" "libssl-dev" "libffi-dev" "python3-dev" "libmariadb-dev" "python3.11-venv" "python3-opencv" "python3-matplotlib" "python3-numpy" "xfce4" "xfonts-base" "tightvncserver")
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
sudo groupadd 
sudo usermod -aG sudo drone
sudo usermod -aG video drone
sudo usermod -aG gpio drone


#: Create Files and Folders
mkdir -v -p "/home/drone/Pictures/Faces/catologued/admin"
mkdir -v "/home/drone/Pictures/Faces/onscreen"


#: SQL.
    #: Create DB tables.
mariadb -e "CREATE DATABASE droneDB;"
mariadb -e "USE droneDB; CREATE TABLE system (initBoot NVARCHAR(255) );"
mariadb -e "USE droneDB; CREATE TABLE userID (fullpath NVARCHAR(255) PRIMARY KEY, name NVARCHAR(255), priv VARCHAR(224), lastTag NVARCHAR(255) );"
    #: Create DB Users.
mariadb -e "CREATE USER 'drone'@'localhost' IDENTIFIED BY ''"
mariadb -e "GRANT ALL PRIVILEGES ON droneDB.system TO 'drone'@'localhost' WITH GRANT OPTION"

#Python Files
cp -r -p -f -a "$vPWD/python3" "/home/drone/"
chown -R drone:drone "/home/drone"

#VNC Files
cp -p -f "$vPWD/xstartup" "/home/drone/.vnc/xstartup"
mkdir -v "/home/drone/.vnc"

#: Python3 Settings
sudo -H -u drone bash -c 'cd "/home/drone" && python3 -m venv ".venv"'
sudo -H -u drone bash -c '/home/drone/.venv/bin/pip3 install OPi.GPIO mediapipe mariadb tensorflow face-recognition --use-pep517'

#: Disable suspend
sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target

sudo reboot
