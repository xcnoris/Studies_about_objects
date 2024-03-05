class Livro:
    livros = []

    def __init__(this, titulo, autor, ano_publicacao):
        this._titulo = titulo
        this._autor = autor
        this._ano_publicacao = ano_publicacao
        this._disponivel = True
        Livro.livros.append(this)


    @classmethod
    def listar_livros(cls):
        print(f'{'Titulo'.ljust(25)} | {'Autor'.ljust(25)} | {'Ano de Publicação'.ljust(25)} | {'Disponivel'}')
        for livro in cls.livros:
            print(f'{livro._titulo.ljust(25)} | {livro._autor.ljust(25)} | {str(livro._ano_publicacao).ljust(25)} | {livro.disponivel}')


    @classmethod
    def livros_por_ano(cls, ano):
        livros_ano = []
        for livro in cls.livros:
            if livro._ano_publicacao == ano:
                livros_ano.append(livro)
                print(f'{'Titulo'.ljust(25)} | {'Autor'.ljust(25)} | {'Ano de Publicação'.ljust(25)} | {'Disponivel'}')
        for livro in livros_ano:
            print(f'{livro._titulo.ljust(25)} | {livro._autor.ljust(25)} | {str(livro._ano_publicacao).ljust(25)} | {livro.disponivel}')




    def __str__(this) -> str:
        return f'{this._titulo} | {this._autor} | {this._ano_publicacao} '
    

    @property
    def disponivel(this):
        return '☑' if this._disponivel else '☐'
        
    def alterar_disponibilidade(this):
        this._disponivel = not this._disponivel