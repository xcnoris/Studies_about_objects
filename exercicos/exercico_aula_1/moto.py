from exercicos.exercico_aula_1.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(this, marca, modelo, tipo):
        super().__init__(marca, modelo)
        this._tipo = tipo
    
    
    def __str__(this):
        estado = 'Ligado' if this._ligado else 'Desligado'
        return f'Marca: {this._marca} | Modelo: {this._modelo} | Estado: {estado} | Tipo: {this._tipo}'