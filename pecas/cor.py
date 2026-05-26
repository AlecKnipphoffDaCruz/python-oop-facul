class Cor:
    """Representa a cor da pintura do carro."""

    OPCOES = ["Vermelho", "Preto", "Branco", "Azul", "Verde", "Amarelo"]

    def __init__(self, nome: str):
        self._nome = nome

    # ── Getter ─────────────────────────────────────────────────────────────────
    @property
    def nome(self) -> str:
        return self._nome

    # ── Setter ─────────────────────────────────────────────────────────────────
    @nome.setter
    def nome(self, valor: str):
        self._nome = valor

    def __str__(self)  -> str: return self._nome
    def __repr__(self) -> str: return f"Cor(nome={self._nome!r})"
