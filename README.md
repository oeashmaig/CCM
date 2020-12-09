# CCM
A Platform for Chronic Cognitive Monitoring (CCM) of Neurosurgical Patients During Hospitalization


# Materials:


# Expanded Instructions:

## 1. Open the terminal and run the following commands:

a. 	Sudo apt-get update

b. 	Sudo apt-get upgrade

c. 	Sudo apt-get install -f

d. 	Sudo apt install qt5-default

e. 	Sudo apt-get install libasound2-dev

f.  	Sudo python3 -m pip install simpleaudio

g. 	Sudo python2 -m pip install pyxid

h. 	Sudo pip install pygame

i.  	If a dependency error occurs in any of the above commands, run Sudo apt --fix-broken install

## 2. 	Download and install the required D2xx driver

a. 	https://www.ftdichip.com/Drivers/D2XX.htm

    i. 	The raspberry Pi uses an ARM processor structure, thus download the hard-float versions of the driver

b. 	Make sure the Cedrus StimTracker is not currently connected to the Raspberry Pi

c. 	tar xfvz libftd2xx-<platform>-x.x.x.tgz
  
    i. 	replace x.x.x with the driver version   
  
d. 	Cd build
  
e. 	Sudo -s

f.  	cp libftd2xx.* /usr/local/lib

g. 	chmod 0755 /usr/local/lib/libftd2xx.so.x.x.x

h. 	ln -sf /usr/local/lib/libftd2xx.so.x.x.x /usr/local/lib/libftd2xx.so

i.  	Exit

j.  	Cd examples

k. 	Plug in the Cedrus StimTracker before continuing

l.  	make -B

m.   cd EEPROM/read

n. 	sudo ./read

o. 	If the message "FT_Open failed" appears, the VCP driver is likely enabled, you must disable before continuing

p. 	sudo lsmod

q. 	If "ftdi_sio" is listed:

    i. 	sudo rmmod ftdi_sio
                                                      
    ii. 	sudo rmmod usbserial
                                                    
r.  	If a dependency error

    i. Run this command :

## 3. 	Edit your rc.local file to run the bash script automatically at boot

a. 	Sudo nano /etc/rc.local

b. 	Sudo $bash script location

c. 	The bash script runs both python scripts simulatenously, make sure it is properly edited to point to the correct location of the python files
