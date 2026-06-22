class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __repr__(self):
        # formatação pra testes
        return f"Contato(nome='{self.nome}, telefone='{self.telefone}')"