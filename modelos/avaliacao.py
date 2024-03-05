class Avaliacao:
    def __init__(this, cliente, nota ):
         if nota < 0 or nota > 5:
              raise ValueError("[ERROR] A nota deve ser entre 0 a 5.")
         this._cliente = cliente
         this._nota = nota