#!/bin/bash
if [[ $EUID -ne 0 ]]; then
    echo "This script must be run as root."
    exit 1
fi


vPWD=$(dirname $0)
vFILESYSTEM=$(df -P . | sed -n '$s/[[:blank:]].*//p')
vUUID=$(/usr/sbin/blkid -s UUID -o value "$vFILESYSTEM")

#: Dependancies.
aDEPENDS=("sudo" "libmariadb3" "mariadb-server" "build-essential" "libssl-dev" "libffi-dev" "python3-dev" "libmariadb-dev" "python3.11-venv" "python3-opencv" "python3-matplotlib" "python3-numpy")
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

#: Create Files and Folders
mkdir -v -p "/home/drone/Pictures/Faces/admin"
mkdir -v "/home/drone/Pictures/Faces/uncatologued"

#: SQL.
    #: Create DB tables.
mariadb -e "CREATE DATABASE droneDB;"
mariadb -e "USE droneDB; CREATE TABLE paths (fullpath NVARCHAR(255) PRIMARY KEY, parent NVARCHAR(255), name NVARCHAR(255),date VARCHAR(224), size VARCHAR(255), mtime CHAR(244) );"
    #: Create DB Users.
mariadb -e "CREATE USER 'drone'@'localhost' IDENTIFIED BY ''"
mariadb -e "GRANT ALL PRIVILEGES ON droneDB.paths TO 'drone'@'localhost' WITH GRANT OPTION"


#Copy Files
cp -r -p -f -a "./SecurityDrone-Prototype/." "/home/drone/"
chown -R drone:drone "/home/drone"

#: Python3 Settings
sudo -H -u drone bash -c 'cd "/home/drone" && python3 -m venv ".venv"'
sudo -H -u drone bash -c '/home/drone/.venv/bin/pip3 install mediapipe mariadb tensorflow --use-pep517'
