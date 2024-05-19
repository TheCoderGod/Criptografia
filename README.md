# CRIPTOGRAFIA DE ARQUIVOS DE TEXTO

Este projeto em Python permite criptografar e descriptografar arquivos de texto. Dependendo do comando fornecido, o programa criptografa ou descriptografa os arquivos. Se não houver uma chave criada, ele gera uma nova chave para criptografar o arquivo. Se uma chave já estiver presente na pasta, ele a utiliza tanto para criptografar quanto para descriptografar. Se você não tiver a chave correta ao tentar descriptografar ou se excluí-la, provavelmente não terá mais acesso àquela informação.


## PRÉ-REQUISITOS

- Python 3.12.3 ou superior
- Biblioteca `cryptography`


### Instalação da Biblioteca `cryptography`

Para instalar a biblioteca necessária, execute:

pip install cryptography



## INSTRUÇÕES PARA USO

1. CRIPTOGRAFANDO
	-Mova ou copie o arquivo "crypto.py" para a pasta onde o arquivo de texto sera criptografado.
	-Crie um arquivo .txt com o nome desejado nessa pasta.
	-Abra seu CMD, navegue ate a pasta desejada, e execute o comando:
	"python crypto.py encrypt exemplo.txt"
	Você irá substituir "exemplo" de "exemplo.txt" pelo nome do seu arquivo gerado no passo anterior!
	-Pronto! O programa irá criptografar a mensagem e no mesmo diretório gerar o arquivo "key.key" com a chave para descriptografar o mesmo! Não perca ela!


2. DESCRIPTOGRAFANDO
	-Abra seu CMD, navegue ate a pasta desejada, e execute o comando:
	"python crypto.py decrypt exemplo.txt"
	Você irá substituir "exemplo" de "exemplo.txt" pelo nome do seu arquivo gerado no passo anterior!
	-O programa irá usar a chave guardada no arquivo "key.key" do diretório atual!

 