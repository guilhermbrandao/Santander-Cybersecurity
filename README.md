# Santander-Cybersecurity

## Simulando Malware Ransomware, Keylogger Simples em Python e Aprendendo a se Proteger. O projeto é educacional em ambientes controlado e o que foi feito para mitigar riscos.

### Objetivo simular funcionamento do Ransomware e Keylogger.

### Parte 1 -Transferindo arquivo da maquina pessoal (Linux mint) para maquina virtual(Windows 7) utilizando ISO: 
#### Com os scripts prontos (desenvolvidos nas aulas) foi preciso tranferi-los eles para a maquina virtual (windows 7) de forma segura sem comprometer a maquina pessoal.

#### 1. Criar um pasta no Linux:
- Vamos começar por Ransomware.
  
- Abri o terminal:
- ```bash
  mkdir -p ~/test_ISO
  
- Colocar o caminho do arquivo que deseja tranferir:
- ```bash
  cp /caminho/do/seu/arquivo.py ~/test_ISO
  
#### 1.1 Gerar imagem ISO 
- Use o comando:
- ```bash
  mkisofs -o ~/test.iso ~/test_ISO
- Criará o arquivo:
  ```bash
   ~/test.iso
#### 1.2 Colocar ISO no VirtualBox (windows 7):
- Abrir o VitualBox > **selecionar a Maquina Virtual** > **Configurações** > **Armazenamento**
- Procurar por **Controlador: SATA** e ir no **ícone CD**: **1**
- Adicionar a imagem ISO: **2**

- ![ISOwin7](https://github.com/user-attachments/assets/0041250d-a88f-4950-a7d1-05eb4c11b504)

- Salvar as configurações e iniciar a maquina virtual.
- No windows 7:
- 1- abrir **Biblioteca** > 2- ao lado esquerdo **Computador** > 3- **Unidade de CD (E:) CDROM**

- ![diretoriopastas](https://github.com/user-attachments/assets/d1c23605-731a-4bf4-ab2a-4da2a061a200)

#### 1.3 Criar uma pasta e arquivos para teste: 
- A pasta criada vai ser usada para ter um diretorio para especificar pelo prompt de comando, os arquivos dentro 
- Após criação de pastas e arquivos que seram criptocrafados


- 

  

  
  
 




