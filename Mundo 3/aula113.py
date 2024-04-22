import urllib.request

def verifica_acessibilidade(url):
    try:
        urllib.request.urlopen(url)
        print(f"O site {url} está acessível!")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar acessar o site {url}: {e}")

url_pudim = "http://www.pudim.com.br"
verifica_acessibilidade(url_pudim)
