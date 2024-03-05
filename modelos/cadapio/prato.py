from modelos.cadapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(this, nome, preco, descricao):
        super().__init__(nome, preco)
        this._descricao = descricao

    def __str__(this):
        return this._nome
    
    def aplicar_desconto(this):
        this._preco -= (this._preco * 0.08) 