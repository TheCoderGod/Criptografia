import argparse
from cryptography.fernet import Fernet
import os

# Gerar uma chave e armazená-la em um arquivo
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Chave gerada e salva em key.key")

# Carregar a chave
def load_key():
    return open("key.key", "rb").read()

# Criptografar o arquivo
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    
    with open(file_path, "rb") as file:
        file_data = file.read()
    
    encrypted_data = fernet.encrypt(file_data)
    
    with open(file_path, "wb") as file:
        file.write(encrypted_data)
    
    print(f"{file_path} foi criptografado com sucesso.")

# Descriptografar o arquivo
def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(file_path, "wb") as file:
        file.write(decrypted_data)
    
    print(f"{file_path} foi descriptografado com sucesso.")

def main():
    parser = argparse.ArgumentParser(description="Ferramenta de Criptografia de Arquivos")
    parser.add_argument("action", choices=["encrypt", "decrypt"], help="Ação a ser realizada")
    parser.add_argument("file", help="Caminho do arquivo a ser processado")

    args = parser.parse_args()

    # Verificar se a chave já existe
    if not os.path.exists("key.key"):
        generate_key()
    
    if args.action == "encrypt":
        if os.path.exists(args.file):
            encrypt_file(args.file)
        else:
            print(f"Arquivo {args.file} não encontrado.")
    elif args.action == "decrypt":
        if os.path.exists(args.file):
            decrypt_file(args.file)
        else:
            print(f"Arquivo {args.file} não encontrado.")

if __name__ == "__main__":
    main()
