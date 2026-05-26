class Pneu:
    """Representa os pneus do carro."""

    OPCOES = ["Michelin", "Pirelli", "Bridgestone", "Continental"]

    def __init__(self, marca: str):
        self._marca = marca

    # ── Getter ─────────────────────────────────────────────────────────────────
    @property
    def marca(self) -> str:
        return self._marca

    # ── Setter ─────────────────────────────────────────────────────────────────
    @marca.setter
    def marca(self, valor: str):
        self._marca = valor

    def __str__(self)  -> str: return self._marca
    def __repr__(self) -> str: return f"Pneu(marca={self._marca!r})"
