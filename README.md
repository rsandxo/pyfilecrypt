# PyFileCrypt - AES-256/RSA File Encryption Tool


PyFileCrypt is a simple command-line tool that allows users to encrypt and decrypt files using the Advanced Encryption Standard (AES) with 256-bit keys, along with RSA encryption for session key encryption. This tool uses the standalone PyCryptodome library under the hood for its cryptographic operations.

## Installation/Setup Instructions


1. Clone this repository to your local machine: `git clone https://github.com/rsandxo/pyfilecryptor.git`
2. Navigate to the project directory in your terminal or command prompt.
3. Create a new virtual environment by running the following commands:
  
   ` python -m venv env
    source env/bin/activate  # On Unix systems (Linux, macOS)
    env\Scripts\Activate.ps1  # On Windows systems`
   
6. Install the required dependencies inside your virtual environment by running:
   ` pip install -r requirements.txt`

   
5. Ensure that you have Python 3 installed on your machine, as this tool is written for Python 3.
6. Generate RSA keys by running `python pyfilecryptor_generate.py` in the terminal or command prompt. This will create two files: 'key.pem' (private key) and 'key.pub' (public key). Keep these files secure, as they are essential for encrypting/decrypting your data. They will be stored in `/home/{yourusername}`
7. Make sure that you have the necessary permissions to read and write files in the directory where you plan to use this tool.

## Usage Information


To encrypt a file using PyFileCrypt:
1. Run `python pyfilecrypt_encrypt.py` in the terminal or command prompt, the tool will ask you for the path of the file you wish to encrypt. The tool will read the contents of the specified file and replace it with its encrypted version.
2. A message confirming successful encryption will be displayed in the terminal.
3. To decrypt a previously encrypted file, simply run `python pyfilecryptor_decrypt.py` in your terminal. The tool will ask you for the path of the file you wish to decrypt. The tool will read and decrypt the previously decrypted data and replace it with the original data.
4. A message confirming successful decryption will be displayed in the terminal.
   
### Contribution Guidelines


If you'd like to contribute to this project, please feel free to submit a pull request with your changes or improvements. When submitting a pull request:
- Ensure that your code adheres to PEP 8 standards for Python code style and formatting.
- Include appropriate tests to validate the functionality of any new features or bug fixes.
- Make sure that you have updated all relevant documentation, including this README file.

### Contact Information

For questions, suggestions, or support, please feel free to contact me at `rachel@sandover.ca`. You can also open an issue if you encounter any problems.
