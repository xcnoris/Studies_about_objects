from modelos.cadapio.item_cardapio import ItemCardapio

class Sobremessa(ItemCardapio):
    def __init__(this, nome, preco, tipo, tamanho):
        super().__init__(nome, preco)
        this._tipo = tipo
        this._tamanho = tamanho

    def __str__(this):
        return this._nome
    
    def aplicar_desconto(this):
        this._preco -= (this._preco * 0.10) 