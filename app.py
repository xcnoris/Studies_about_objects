from modelos.restaurante import Restaurante
from exercicos.livro import Livro
from modelos.cadapio.prato import Prato
from modelos.cadapio.bebida import Bebida
from modelos.cadapio.sobremesa import Sobremessa


from exercicos.exercico_aula_1.veiculo import Veiculo
from exercicos.exercico_aula_1.carro import Carro
from exercicos.exercico_aula_1.moto import Moto




restaurante_campos = Restaurante('Campos', 'Pizzas')
restaurante_milkqshaq = Restaurante('Milk Shaq', 'Sorvetes')


prato_macarronada = Prato('Macarronada Italiana', 25.00, 'O melhor macarrão da cidade')
prato_macarronada.aplicar_desconto()


bebida_suco = Bebida('Suco', 5.0, 'Grande')
bebida_suco.aplicar_desconto()

sobremessa_pudim = Sobremessa('Pudim', 15, 'Gelado', '250ml')
sobremessa_pudim.aplicar_desconto()


restaurante_campos.adicionar_no_cardapio(bebida_suco)
restaurante_campos.adicionar_no_cardapio(prato_macarronada)
restaurante_campos.adicionar_no_cardapio(sobremessa_pudim)




livro_flash = Livro('The flash', 'dc', 1960)
livro_flash.alterar_disponibilidade()
livro_batman = Livro('The Batman', 'dc', 1952)

carro1 = Carro('Fiat', 'Uno', 4)
carro2 = Carro('Ford', 'Car', 2)
carro3 = Carro("Ford", "Fusion", 4)

moto1 = Moto("Harley-Davidson", "Street 750", "Esportiva")
moto2 = Moto("Honda", "CB 500", "Casual")
moto3 = Moto("Yamaha", "MT-09", "Esportiva")

def main():
    restaurante_campos.exibir_cardapio

    # Restaurante.listar_restaurantes()
    # listar_livros()
    # Livro.livros_por_ano(1952)
    # print(bebida_suco)
    # print(prato_macarronada)

    # print(carro1)
    # print(carro2)
    # print(carro3)
    
    # print(moto1)
    # print(moto2)
    # print(moto3)
    
if __name__ == '__main__':
    main()



    
