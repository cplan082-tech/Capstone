#!/bin/bash

echo "Welcome to Steph's setup script!"
echo ""

echo "Starting updates"

sudo apt-get update
sudo apt-get dist-upgrade

echo ""
echo "Upgrading pip"
python -m pip install --upgrade pip
sudo apt-get install python3-pip

sudo apt-get install python3-pandas

echo ""
echo "Installing required AWS packages"

pip install boto3
pip3 install boto3
python3 -m pip install AWSIoTPythonSDK
python3 -m pip install awscrt
pip3 install awsiotsdk

sudo pip install awscli
#pip3 install awscli --upgrade --user
export PATH=/home/pi/.local/bin:$PATH

echo ""
echo "Configuring aws now, please follow Steph's instructions"

aws --version
aws configure

echo ""
echo "Done!!!"
