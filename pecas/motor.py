class Motor:
    """Representa o motor do carro."""

    OPCOES = ["1.0 Flex", "2.0 Turbo", "Elétrico", "Híbrido"]

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
    def __repr__(self) -> str: return f"Motor(tipo={self._tipo!r})"
