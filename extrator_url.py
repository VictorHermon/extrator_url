import re


class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanetiza_url(url)
        self.valida_url()

    @staticmethod
    def sanetiza_url(url):
        if url:
            return url.strip()

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        # () para pegar o valor extato, [] para pegar as opções
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        # string para busca um padrao dentro de uma string
        # match para verificar se a string combina com determinado padrao
        match = padrao_url.match(url)
        if not match:
            raise ValueError('A URL não é valida')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        if not parametro_busca:
            raise ValueError('O parametro em get_valor_parametro, não pode ser 0 ou vazio')
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'URL: {self.url} \nBase: {self.get_url_base()} \nParâmetros: {self.get_url_parametros()}'

    def __eq__(self, other):
        return self.url == other.url


moeda_origem = input('Digite a moeda de origem (dolar ou real): ')
moeda_destino = input('Digite a moeda de destino (dolar ou real): ')
quantidade = input('Digite a quantidade de moedas: ')

url = f'bytebank.com/cambio?quantidade={quantidade}&moedaOrigem={moeda_origem}&moedaDestino={moeda_destino}'
extrator_url = ExtratorURL(url)
valor_dolar = 5.50  # U$1 dolar = R$5.50 reais

# extrator_url2 = ExtratorURL(url)
# print(f'O tamanho da URL é igual á: {len(extrator_url)}')
# print(extrator_url)
# print(f'Os objetos são iguais: {extrator_url == extrator_url2}')

moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
quantidade = extrator_url.get_valor_parametro('quantidade')

if moeda_origem == 'real' and moeda_destino == 'dolar':
    conversao = float(quantidade) / valor_dolar
    print(f'Cotação do dolar: U${valor_dolar}')
    print(f'Valor da conversão de {moeda_origem} para {moeda_destino} é: {conversao:.2f}')
elif moeda_origem == 'dolar' and moeda_destino == 'real':
    conversao = float(quantidade) * valor_dolar
    print(f'Cotação do dolar: U${valor_dolar}')
    print(f'Valor da conversão de {moeda_origem} para {moeda_destino} é: {conversao:.2f}')
else:
    print(f'O cambio de {moeda_origem} para {moeda_destino} não está disponivel')
