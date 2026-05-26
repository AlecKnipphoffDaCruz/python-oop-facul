class Rodas:
    """Representa as rodas do carro."""

    OPCOES = ["Aro 15", "Aro 17", "Aro 19", "Aro 21"]

    def __init__(self, aro: str):
        self._aro = aro

    # ── Getter ─────────────────────────────────────────────────────────────────
    @property
    def aro(self) -> str:
        return self._aro

    # ── Setter ─────────────────────────────────────────────────────────────────
    @aro.setter
    def aro(self, valor: str):
        self._aro = valor

    def __str__(self)  -> str: return self._aro
    def __repr__(self) -> str: return f"Rodas(aro={self._aro!r})"
