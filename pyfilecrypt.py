#!/usr/bin/env python

from Cryptodome.Cipher import AES, PKCS1_OAEP
from Cryptodome.PublicKey import RSA
from Cryptodome.Random import get_random_bytes
from io import BytesIO

import base64
import zlib
import sys
import os

def generatekey():
    new_key = RSA.generate(4096)
    private_key = new_key.exportKey()
    public_key = new_key.publickey().exportKey()

    with open('key.pem', 'wb') as f:
        f.write(private_key)

    with open('key.pub', 'wb') as f:
        f.write(public_key)

def get_rsa_cipher(keytype):
    with open(f'key.{keytype}') as f:
        key = f.read()
    rsakey = RSA.importKey(key)
    return (PKCS1_OAEP.new(rsakey), rsakey.size_in_bytes())

def encrypt(plaintext):
    compressed_text = zlib.compress(plaintext)

    session_key = get_random_bytes(32)
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(compressed_text)

    cipher_rsa, _ = get_rsa_cipher('pub')
    enc_session_key = cipher_rsa.encrypt(session_key)

    msg_payload = enc_session_key + cipher_aes.nonce + tag + ciphertext
    enc_data = base64.encodebytes(msg_payload)
    return(enc_data)

def decrypt(enc_data):
    enc_bytes = BytesIO(base64.decodebytes(enc_data))
    cipher_rsa, keysize_in_bytes = get_rsa_cipher('pem')

    enc_session_key = enc_bytes.read(keysize_in_bytes)
    nonce = enc_bytes.read(16)
    tag = enc_bytes.read(16)
    ciphertext = enc_bytes.read()

    session_key = cipher_rsa.decrypt(enc_session_key)
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    dec_data = cipher_aes.decrypt_and_verify(ciphertext, tag)

    plaintext = zlib.decompress(dec_data)
    return(plaintext)

def error_check():
    filename = input("Enter the path to the file you wish to encrypt/decrypt: ")
    print(filename)
    sanity_check = input("Final sanity check. Are you sure of this choice? Type 'yes' in capital letters.\n")
    if sanity_check == 'YES':

        if user_input == 'E' or user_input == 'e':
            try:
                if not os.path.exists(filename):
                    raise FileNotFoundError(f"The specified file '{filename}' does not exist.")
                if not os.path.isfile(filename):
                    raise IsADirectoryError("Please specify a valid filename.")

                with open(filename, 'rb') as f0:
                    contents = f0.read()
                with open(filename, 'wb') as f1:
                    f1.write(encrypt(contents))

                print("File encrypted! Original file replaced!")
                sys.exit(0)

            except FileNotFoundError as e:
                print(e)
                sys.exit(1)
            except IsADirectoryError as e:
                print(e)
                sys.exit(1)
        elif user_input == 'D' or user_input == 'd':
            try:
                if not os.path.exists(filename):
                    raise FileNotFoundError(f"The specified file '{filename}' does not exist.")
                if not os.path.isfile(filename):
                    raise IsADirectoryError("Please specify a valid filename.")

                with open(filename, 'rb') as f0:
                    contents = f0.read()
                with open(filename, 'wb') as f1:
                    f1.write(decrypt(contents))

                print("File decrypted! Original file replaced!")
                sys.exit(0)

            except FileNotFoundError as e:
                print(e)
                sys.exit(1)
            except IsADirectoryError as e:
                print(e)
                sys.exit(1)
    else:
        print("Program will exit... no files changed.")
        sys.exit(1)


def main():
    print("....................PyFileCrypt v1.2.................")
    print("|   Encrypts files using AES-256 / RSA algorithms   |")
    print("......................by rsandxo.....................\n")


    global user_input
    user_input = input("(E)ncrypt, (D)ecrypt, or (G)enerate certificate?\n")
    if user_input == 'G' or user_input == 'g':
        print("Generating public/private RSA key pair...")
        generatekey()
        print("Done.")
        sys.exit(0)
    elif user_input == 'E' or user_input == 'e' or user_input == 'D' or user_input == 'd':
        error_check()
    else:
        print("Invalid input! Exiting...")
        sys.exit(1)

if __name__ == '__main__':
    main()