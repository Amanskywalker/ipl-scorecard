#!/bin/sh
ROOTUID="0"

if ["$(id -u)" -ne "$ROOTUID"]; then
	echo "run as admin!"
	exit 1
fi

echo "Installing ipl \m/\n"
pip install urllib2 2> /dev/null
pip install bs4 2> /dev/null
pip install prettytable 2> /dev/null

mv ./ipl.py ~/
echo "alias wt20='watch python2 wt20.py'" >> ~/.bashrc
echo "\nSuccessfully installed!"
echo "Usage: \n$ wt20 <team1> <team2>"
