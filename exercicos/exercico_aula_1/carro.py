from exercicos.exercico_aula_1.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(this, marca, modelo, portas):
        super().__init__(marca, modelo)
        this._portas = portas

    def __str__(this):
        estado = 'Ligado' if this._ligado else 'Desligado'
        return f'Marca: {this._marca} | Modelo: {this._modelo} | Estado: {estado} | Portas: {this._portas}'