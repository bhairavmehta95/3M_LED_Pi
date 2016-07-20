git clone https://github.com/sarfata/pi-blaster
sudo apt-get install autoconf
Y
cd pi-blaster
./autogen.sh
./configure
make
cd ..
sudo apt-get install bluetooth
sudo apt-get install python-bluez
python raspi_code.py
