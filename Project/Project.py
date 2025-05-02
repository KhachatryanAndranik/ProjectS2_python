import os

def xor_encrypt_decrypt(input_file, output_file, key):
    """
    Encrypts or decrypts the content of a file using XOR cipher.

    Args:
        input_file (str): Path to the input file.
        output_file (str): Path to the output file.
        key (str): The key (as a string).
    """
    try:
        key_bytes = key.encode()  

        with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
            input_bytes = infile.read()
            output_bytes = bytearray()

            for i in range(len(input_bytes)):
                output_bytes.append(input_bytes[i] ^ key_bytes[i % len(key_bytes)])

            outfile.write(output_bytes)

        print(f"[+] Operation successful. Output written to: {output_file}")
    except FileNotFoundError:
        print(f"[!] Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

def main():
    while True:
        print("\nSimple XOR File Encryptor/Decryptor")
        print("1. Encrypt File")
        print("2. Decrypt File")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            input_filename = input("Enter the name of the file to encrypt: ")
            output_filename = input("Enter the name for the encrypted output file: ")
            encryption_key = input("Enter the encryption key: ")
            xor_encrypt_decrypt(input_filename, output_filename, encryption_key)
        elif choice == '2':
            input_filename = input("Enter the name of the file to decrypt: ")
            output_filename = input("Enter the name for the decrypted output file: ")
            decryption_key = input("Enter the decryption key (must be the same as the encryption key): ")
            xor_encrypt_decrypt(input_filename, output_filename, decryption_key)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("[!] Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    main()
