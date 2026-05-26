class Chassi:
    """Representa o chassi (estrutura base) do carro."""

    OPCOES = ["Esportivo", "SUV", "Sedã", "Pickup"]

    def __init__(self, tipo: str):
        self._tipo = tipo

    # ── Getter ─────────────────────────────────────────────────────────────────
    @property
    def tipo(self) -> str:
        return self._tipo

    # ── Setter ─────────────────────────────────────────────────────────────────
    @tipo.setter
    def tipo(self, valor: str):
        self._tipo = valor

    def __str__(self)  -> str: return self._tipo
    def __repr__(self) -> str: return f"Chassi(tipo={self._tipo!r})"
