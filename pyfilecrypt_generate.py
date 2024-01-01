#!/usr/bin/env python

from pyfilecrypt_encrypt import generatekey

if __name__ == '__main__':
    print("Generating public/private RSA 4096-bit key pair...")
    generatekey()
    print("Done.")
