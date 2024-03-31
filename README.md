# PyFileCrypt - AES-256/RSA File Encryption Tool


PyFileCrypt is a simple command-line tool that allows users to encrypt and decrypt files using the Advanced Encryption Standard (AES) with 256-bit keys, along with RSA encryption for session key encryption. This tool uses the standalone PyCryptodome library under the hood for its cryptographic operations.

# TODO
- Unify into one script file *DONE*
- Add support for command line arguments (i.e. passing file path directly)
- Add ability to change certificate storage path
- Implement a method to preserve original file, instead of replacing.

## Installation/Setup Instructions


1. Clone this repository to your local machine: `git clone https://github.com/rsandxo/pyfilecrypt.git`
2. Navigate to the project directory in your terminal or command prompt.
3. Create a new virtual environment by running the following commands (optional, but recommended):
  ```
   python -m venv env
   source env/bin/activate  # On Unix systems (Linux, macOS)
   env\Scripts\Activate.ps1  # On Windows systems
  ``` 
4. Install the required dependencies inside your virtual environment by running:
   `pip install -r requirements.txt`

   
5. Ensure that you have Python 3 installed on your machine, as this tool is written for Python 3.
6. Generate RSA keys by running `python pyfilecrypt.py` in the terminal or command prompt. Select 'G' on the interactive screen. This will create two files: 'key.pem' (private key) and 'key.pub' (public key). Keep these files secure, as they are essential for encrypting/decrypting your data. They will be stored in `/home/{yourusername}`.

## Usage Information

### IMPORTANT: BACK UP DATA BEFORE USING THIS TOOL.
This tool is a proof-of-concept at best. I do not recommend using it on critical data. I am not responsible for any potential data loss as a result of using this tool.

To encrypt a file using PyFileCrypt:
1. Run `python pyfilecrypt.py` in the terminal or command prompt, enter 'E', the tool will ask you for the path of the file you wish to encrypt. Before any data is modified you will be asked for confirmation. The tool will read the contents of the specified file and replace it with its encrypted version.
2. A message confirming successful encryption will be displayed in the terminal.
3. To decrypt a previously encrypted file, simply run `python pyfilecrypt.py` in your terminal. Follow the prompts on the interactive screen. The tool will ask you for the path of the file you wish to decrypt. The tool will read and decrypt the previously decrypted data and replace it with the original data.
4. A message confirming successful decryption will be displayed in the terminal.
   
### Contribution Guidelines


If you'd like to contribute to this project, please feel free to submit a pull request with your changes or improvements. When submitting a pull request:
- Ensure that your code adheres to PEP 8 standards for Python code style and formatting.
- Include appropriate tests to validate the functionality of any new features or bug fixes.
- Make sure that you have updated all relevant documentation, including this README file.

### Contact Information

For questions, suggestions, or support, you can open an issue if you encounter any problems.
