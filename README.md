# PigCrypt

Description

## Installation

Clone this repository and change directory:  
```sh
git clone https://github.com/AnselOngMJ/PigCrypt
cd PigCrypt
```

Install dependencies:  
```sh
pip install -r requirements.txt
```

## Usage

With default key:  
```sh
$ python encipher.py ciphertext
Enter plaintext (use '.' for newlines): hello world
```

With customised key:  
```sh
$ python encipher.py ciphertext -k
Enter plaintext (use '.' for newlines): hello world
Enter key: qwertyuiopasdfghjklzxcvbnm
```

![Pigpen Key](https://github.com/AnselOngMJ/PigCrypt/blob/main/images/pigpen_key.png "Pigpen Key")

![Pigpen Guide](https://github.com/AnselOngMJ/PigCrypt/blob/main/images/pigpen_guide.png "Pigpen Guide")
