class Contato():
    id: int
    nome: str
    telefone: str
    endereco: str
    def __init__(self, nome: str, telefone: str, endereco: str):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
    