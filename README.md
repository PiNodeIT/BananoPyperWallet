# BananoPyperWallet
a small python script that uses the nanolib to create seed/address pairs for BANANO

***For security reasons, it is strongly recommended to run this script in an offline environment***

## Feature
Generates a seed/addres pair for BANANO Generate a seed/addres pair for BANANO using Matoking's nanolib library https://github.com/Matoking/nanolib

## Requirements

- Python 3.7+
- Pip
  - nanolib

## Installation

if you haven't done so yet, install pip
```sh
sudo apt install python3-pip
```

install the requirements
```sh
pip install -r requirements.txt
```
nanolib requires a working build environment for the C extensions. For example, on Debian-based distros you can install the required Python header files and a C compiler using the following command:
```sh
sudo apt install build-essential python3-dev`
```
## Usage
simply run the script and a seed/address pair will be returned on screen

## What is BANANO?
https://banano.cc/

### credits :
thanks to Matoking for the [nanolib](https://github.com/Matoking/nanolib)
