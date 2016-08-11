sudo apt-get install bluetooth
sudo apt-get install python-bluez
sudo apt-get install autoconf
pip install requests
git clone https://github.com/sarfata/pi-blaster
cd pi-blaster
./autogen.sh
./configure
make
cd ..
cd 
python raspi_code.py
