#!/usr/bin/env python
# coding: utf8

import os
import sys
from datetime import date


def main():
	print("Installing Node-RED...")
	print("1. Ensure that the device has a connection to the Internet\n2. Check if the date is correct (current date: " + str(date.today()) + ").")
	print("The official install script will be started now. Unless you have any other requirements, we recommend to answer all following questions with y (yes).")
	res = input("Would you like to proceed? [y/N] ")
	if not (res == "y" or res == "Y"):
		print("Abort.")
		sys.exit(1)

	#original
	# os.system("bash -c \"bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)\"")

	# new
	os.system("bash -c \"bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)\"")

	os.system("systemctl enable nodered")
	os.system("systemctl start nodered")
	os.system("sync")

if __name__ == '__main__':
	main()
