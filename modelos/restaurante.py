from modelos.avaliacao import Avaliacao
from modelos.cadapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(this, _nome, categoria):
        this._nome = _nome.title()
        this.categoria = categoria.upper()
        this._ativo = False
        this._avaliacao = []
        this._cardapio = []
        Restaurante.restaurantes.append(this)

    def __str__(this):
        return f'{this._nome.ljust(25)} | {this.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}' )
    
    @property  
    def ativo(this):
        return '☑' if this._ativo else '☐'
    
    def alternar_estado(this):
         this._ativo = not this._ativo

    def receber_avaliacao(this, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        this._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(this):
          if not this._avaliacao:
               return 'Não avaliado'
          soma_das_notas = sum(avaliacao._nota for avaliacao in this._avaliacao)
          quatidade_de_notas = len(this._avaliacao)
          media = round(soma_das_notas / quatidade_de_notas, 1)
          return media  
    

    def adicionar_no_cardapio(this, item):
        if isinstance(item,ItemCardapio):
            this._cardapio.append(item)

    @property
    def exibir_cardapio(this):
        print (f'\nCardapio do restaurante {this._nome}\n')
        for i,item in enumerate(this._cardapio, start=1):
            if hasattr(item, '_descricao'):
                mensagem_prato = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Descrição: {item._descricao}'
                print(mensagem_prato)
            elif hasattr(item, '_tipo'):
                mensagem_sobremessa = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tipo: {item._tipo} | Tamanho: {item._tamanho}'
                print(mensagem_sobremessa)
            else:
                mensagem_bebida = f'{i}. Nome:{item._nome} | Preço: R${item._preco} | Tamanho: {item._tamanho}'
                print(mensagem_bebida)
