# Debian-grub-skipper-ubuntify
READ ALL OF THIS TUTORIAL BEFORE DOING ANYTHING. An open-source project that makes the debian booting screen look more beginer-friendly. This project is made for the noobs that transfer from ubuntu (which we all know steals your data) to Debian. Debian's boot screen might be scary for an ubuntu user, so thats why this project makes the boot screen almost exactly like ubuntu's.
# !!! Important
  This project is created for *Debian 13* and it hasn't been tested on other versions or distros of Debian. Using anything other that *Debian 13* is not recommended, do it at your own risk. Choose between automatic install and manual:

# Automatic Install
For the automatic tutorial you hate to install curl:
  sudo apt install curl
Python 3 is pre-installed on debian 13, if you're using another distro just run the command:
  sudo apt install python3

  Just run this command in the terminal:
    
  curl -L -o repo.zip "https://github.com/Mihnea509/Debian-grub-skipper-ubuntify/releases/download/debian/Debian-grub-skipper.zip" && unzip -o repo.zip -d repo && cd repo && sudo python3 skipgrub.py
  
  Now reboot your PC and watch how that ugly boot screen turns into a fancy scrolling wheel.


# Manual Install
Python 3 is pre-installed on debian 13, if you're using another distro just run the command:
 sudo apt install python3

Download the latest .zip file from the release file and extract it

Open the terminal in the folder you downloaded the file using the cd command or by going to the folder using the files app, right clicking and choosing open in terminal.

run the following command:
  sudo python3 skipgrub.py

Now reboot your PC and watch how that ugly boot screen turns into a fancy scrolling wheel.

# Must-know
If you ever want to acces the grub menu, just spam the SHIFT key while booting.

This will be linked probably to a youtube video made by me, when its out i might put the link here


