# Santander-Cybersecurity

## Simulando Malware Ransomware Simples em Python e Aprendendo a se Proteger. O projeto é educacional em ambientes controlado e o que foi feito para mitigar riscos.

### Objetivo simular funcionamento do Ransomware.

### Parte 1: Transferindo arquivo da maquina pessoal (Linux mint) para maquina virtual(Windows 7) utilizando ISO: 
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
- A criação das pastas para os testes ficou > **"\malware"** > dentro dela a pasta que será criptografada com arquivos .png, .txt, .img, etc. **"\test_files"** e os scripts **ransonware.py**, **descriptografar.py**.

- ![pastasmalware](https://github.com/user-attachments/assets/fff46e24-9bd5-4fde-9b9a-574408ca688c)

### Parte 2: Executando o Ransomware na VM.

- Ao dar dois click para abrir o ransonware todos os arquivos da pasta **test_files** é criptografados.
- (para maior segurança foi expecificado no script o nome da pasta para ser criptografada)
- Abaixo imagem do antes e depois de executar o ransomware:
- **ANTES**
- ![antes](https://github.com/user-attachments/assets/c107a3c1-8d43-4b47-84fa-301de4ce6ef2)
- **DEPOIS**
- ![depois](https://github.com/user-attachments/assets/68ac38b1-0f85-4acd-ab5c-a8389b5b6721)

- Só é possivel descriptografar a pasta se obter a chave certa, nesse caso como é de teste nos mesmo recebemos a chave.
- Para descriptografar a pasta é so rodar o script **descriptografar.py**.
- Depois de concluido seus arquivos volta ao normal como na imagem acima.

### Parte 3: Mitigação de riscos.
- **Backups Corretos**, offline, snapshots imutáveis, não deixar o backup conectado 24h, ransomware critografa unidades externas.
- **Atualização e correções** portas de entrada comuns são:
- Vunerabilidade SMB
- Falhas em RDP
- Sistemas desatualizados
- **Bloquear vetores de ataque**
- Desabilitar RDP para internet, usar autentificação de duas etapas.
- Bloquear macros, desativas macros no Office, permitir documentos assinados.
- Controlar email, filtros de spam, anti-phishing e cuidados com anexos executaveis.
- **Windows**
- Desativar SMBv1
- Ativar controled folder access (windows security)
- Ativar AST rules.
- **Linux**
- SElinux ou AppArmor ativo
- Montagens com 'noexec', 'nosuid', 'nodev'
- Fail2ban para SSH
- Limitar sudo e logs de auditoria.
#### 3.1 mitigação durante o ataque (resposta imediata)
- Se perceber ataque em andamento:
- Desconectar da rede imediatamente
- Desligar Wi-Fi e cabo
- Isolar máquinas do domínio
- Parar processos suspeitos
- Preservar logs (para investigação)
- Não reiniciar (pode completar criptografia)
#### 3.2 Depois do ataque 
- **Não pagar o resgate (não garante recuperação)**
- Tentar ferramentas de decriptação oficiais:
NoMoreRansom.org
- Restaurar do backup sem reconectar à rede infectada.
- Revisar logs para entender o vetor de entrada.
- Reforçar segurança antes da volta à operação.

### Parte 4: Ferramentas utilizadas.
- **VScode** - criação dos scripts em aula.
- **VirtualBox** - software de maquina virtual.
- **python** - linguagem de programação usada.
- **windows 7** - sistema operacional que utilizamos para realizar o teste em maquina isolada.
  

 




