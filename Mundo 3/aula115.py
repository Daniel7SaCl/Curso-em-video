def escrever_arquivo(nome_arquivo, conteudo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            arquivo.write(conteudo)
        print(f"O conteúdo foi escrito no arquivo '{nome_arquivo}' com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao escrever no arquivo '{nome_arquivo}': {e}")

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
        print(f"Conteúdo do arquivo '{nome_arquivo}':")
        print(conteudo)
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo '{nome_arquivo}': {e}")

nome_do_arquivo = 'exemplo.txt'
conteudo_para_escrever = 'Olá! Este é um arquivo de exemplo.\nEle foi criado e modificado usando Python.'

escrever_arquivo(nome_do_arquivo, conteudo_para_escrever)
ler_arquivo(nome_do_arquivo)
