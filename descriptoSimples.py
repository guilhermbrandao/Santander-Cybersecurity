from cryptography.fernet import Fernet 
import os 

# carregar a chave 

def carregar_chave():
    return open("chave.key", "rb").read()

# descriptografar 

def descriptografar_arquivos(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
        dados_descriptografados = f.decrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_descriptografados)

# encontrar arquivos 

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransonware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

# função principal

def main():
    chave = carregar_chave()
    arquivo = encontrar_arquivos("test_files")
    for arquivo in arquivo:
        descriptografar_arquivos(arquivo, chave)
    print("Arquivos restaurados com sucesso")

if __name__ == "__main__":
    main()
  
# Utilizar para fins educativos e em ambiente controlados ou com permissão.
