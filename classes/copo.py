from classes import Recipiente

class Copo(Recipiente):
    def __init__(self, tamanho: float, conteudo: float = 0, limpo: bool = True) -> None:
        super().__init__(tamanho, conteudo, limpo)
        
    def encher(self, bebida : str = "água"):
        if self.estado() == "sujo":
            return "Não se pode encher um copo sujo"
        self.limpo = False
        self.conteudo = self.tamanho
        self.bebida = bebida

    def beber(self, quantidade : float):
        if quantidade < 0:
            return "Quantidade deve ser positiva"
        elif quantidade > self.conteudo:
            return "Não há bebida suficiente no copo"
        self.conteudo -= quantidade

    def lavar(self):
        self.bebida = None
        self.conteudo = 0
        self.limpo = True

    def __repr__(self):
        if self.esta_vazio():
            return f"Um copo vazio de {self.tamanho:.1f}ml"
        return f"Um copo de {self.tamanho:.1f}ml contendo {self.conteudo:.1f}ml de {self.bebida}"

    def __str__(self):
        if self.esta_vazio():
            return f"Um copo vazio de {self.tamanho:.1f}ml"
        return f"Um copo de {self.tamanho:.1f}ml contendo {self.conteudo:.1f}ml de {self.bebida}"
