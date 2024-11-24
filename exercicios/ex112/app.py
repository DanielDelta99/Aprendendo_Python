from util import moeda,dado

num = dado.leiadin('Digite o preço: R$ ')
moeda.resumo(num,int(input('Quanto quer almentar: ')),int(input('Quanto quer diminuir: ')))