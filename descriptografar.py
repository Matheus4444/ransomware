from cryptography.fernet import Fernet
import os

def carregar_chave():
    return open("chave.key", "rb").read()

def descriptografar_arquivo(arquivo, chave):
	f = Fernet(chave)
	with open(arquivo, "rb") as file:
		dados_encriptados = file.read()
		dados_desencriptados = f.decrypt(dados_encriptados)
	with open(arquivo, "wb") as file:
		file.write(dados_desencriptados)

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

def main():
	chave = carregar_chave()
	arquivos_para_descriptografar = encontrar_arquivos("test_files")
	for arquivo in arquivos_para_descriptografar:
		descriptografar_arquivo(arquivo, chave)
	print("Todos os arquivos foram descriptografados!")

if __name__ == "__main__":
	main()