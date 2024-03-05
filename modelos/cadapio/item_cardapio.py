from abc import ABC, abstractmethod
 
class ItemCardapio(ABC):
    def __init__(this, nome, preco):
        this._nome = nome
        this._preco = preco
    
    @abstractmethod
    def aplicar_desconto(this):
        pass