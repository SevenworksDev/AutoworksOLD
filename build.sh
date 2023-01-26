echo "WARNING! If you are running this on Ubuntu, Run this as Sudo before continuing." 
sleep 5
echo "Updating and Installing python, git and nano."
apt update && apt upgrade
apt install python nano git
clear
sleep 2
echo "Downloading the code for Autoworks"
git clone https://github.com/SevenworksDev/Autoworks
cd Autoworks
clear
sleep 2
echo "Installing pip packages for Autoworks"
python -m pip install requests better_profanity dotenv
clear
sleep 2
echo "Done!"
