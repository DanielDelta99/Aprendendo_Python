import urllib
import urllib.request
try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('Erro Acesso!')
except:
    print('!ERRO!')
else:
    print('Tudo OK')
    site.read()
