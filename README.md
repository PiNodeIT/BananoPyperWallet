CHANGELOG 0.0.2
- add possibility to create multiple wallet at once
- seed/address pair ar stored in a txt named by user 

# BananoPyperWallet
a small python script that uses the nanolib to create seed/address pairs for BANANO

***For security reasons, it is strongly recommended to run this script in an offline environment***

# only tested on linux

## Feature
Generate a seed/address pair for BANANO using Matoking's nanolib library https://github.com/Matoking/nanolib

## Requirements

- Python 3.6.9+
- Pip
  - nanolib

## Installation

Clone or download the repo

if you haven't done so yet, install pip
```sh
sudo apt install python3-pip
```
nanolib requires a working build environment for the C extensions. For example, on Debian-based distros you can install the required Python header files and a C compiler using the following command:
```sh
sudo apt install build-essential python3-dev
```
install the requirements
```sh
pip3 install -r requirements.txt
```

## Usage
run the script, enter the number of seed/address pair to be generated , enter a filename (without extension) where to save your results
```sh
python3 bananopyper.py
```
## What is BANANO?
https://banano.cc/

### credits :
thanks to Matoking for the [nanolib](https://github.com/Matoking/nanolib)
