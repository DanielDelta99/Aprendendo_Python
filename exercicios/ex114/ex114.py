import requests

url = 'https://www.pudim.com.br/'

try:
    # Faz uma requisição GET à página
    response = requests.get(url,verify=False)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        print("A página foi acessada com sucesso!")
    else:
        print(f"Erro: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Erro ao acessar a página: {e}")