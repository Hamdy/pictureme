#!/bin/bash

echo "Preparing The environment ...."

echo "Making sure you've the latest version of python-pip"

# Install PIP (apt-get like) for python libraries
sudo apt-get install python-pip

echo "Making sure you've the latest version of virtualenv"

# Install virtualenv (Python Virtual Environment) in which all python dependencies will be installed
pip install virtualenv

echo "Checking the environment ..."
# Create the Environment if not existing
if [ ! -d env ];then
echo "Environment Not found ... creating new one"
mkdir env
virtualenv env
fi

echo "Activating Environment ..." 

# Activate the environment
source env/bin/activate

# Begin installing dependencies from the requirements.pip file
pip install -r requirements.pip

echo "Creating Database ..."

# Create database file and tables
python manage.py syncdb --noinput

# Deactivate environment
deactivate

echo "Done ...."