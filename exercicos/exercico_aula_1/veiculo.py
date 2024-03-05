class Veiculo:
    def __init__(this, marca, modelo):
        this._marca = marca
        this._modelo = modelo
        this._ligado = False

    def __str__(this):
        return f'Marca: {this._marca} | Modelo: {this._modelo} | Estado: {'Ligado' if this._ligado else 'Desligado'} '