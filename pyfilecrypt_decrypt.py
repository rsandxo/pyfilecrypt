#!/usr/bin/env python

from pyfilecrypt_encrypt import decrypt
import os
import sys

if __name__ == '__main__':

    filename = input("Enter the path to the file you wish to decrypt: ")
    print(filename)

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
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)
    except IsADirectoryError as e:
        print(e)
        sys.exit(1)
