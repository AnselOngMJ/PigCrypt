# PigCrypt

Description

## Installation

Clone this repository and change directory:  
```sh
git clone https://github.com/AnselOngMJ/PigCrypt
```
```sh
cd PigCrypt
```

Install dependencies:  
```sh
pip install -r requirements.txt
```

## Usage

### With default key:

```sh
$ python encipher.py ciphertext
Enter plaintext (use '.' for newlines): hello world
```
Example output with default key:  
![hello world enciphered with pigpen](https://github.com/AnselOngMJ/PigCrypt/blob/main/images/example.png)

### With customised key:

```sh
$ python encipher.py ciphertext -k
Enter plaintext (use '.' for newlines): hello world
Enter key: qwertyuiopasdfghjklzxcvbnm
```
The key entered should contain each letter of the English alphabet once in the order you desire. The default key is "abcdefghijklmnopqrstuvwxyz". Refer to the [image below](#pigpen-cipher) for how the order of the letters appear on the grids.

## Pigpen Cipher

Example of a pigpen cipher key:  
![pigpen key](https://github.com/AnselOngMJ/PigCrypt/blob/main/images/pigpen_key.png)

How letters translate to symbols:  
![pigpen guide](https://github.com/AnselOngMJ/PigCrypt/blob/main/images/pigpen_guide.png)
