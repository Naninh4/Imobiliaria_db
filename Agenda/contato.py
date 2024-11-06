class Contato():
    id: int
    nome: str
    telefone: str
    endereco: str
    def __init__(self, id: int | None, nome: str, telefone: str, endereco: str):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco

