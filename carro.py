import random

from pecas import Chassi, Motor, Rodas, Cor, Pneu


class Carro:
    """Compõe as peças em um carro completo (composição de objetos)."""

    # ── Construtor ─────────────────────────────────────────────────────────────
    def __init__(self):
        self.chassi: Chassi = None
        self.motor:  Motor  = None
        self.rodas:  Rodas  = None
        self.cor:    Cor    = None
        self.pneu:   Pneu   = None

    # ── Setters (recebem objetos, não strings) ─────────────────────────────────
    def set_chassi(self, chassi: Chassi): self.chassi = chassi
    def set_motor(self, motor:   Motor):  self.motor  = motor
    def set_rodas(self, rodas:   Rodas):  self.rodas  = rodas
    def set_cor(self, cor:       Cor):    self.cor    = cor
    def set_pneu(self, pneu:     Pneu):   self.pneu   = pneu

    # ── Ação principal ─────────────────────────────────────────────────────────
    def montar(self) -> str:
        faltando = [k for k, v in self.__dict__.items() if v is None]
        if faltando:
            raise ValueError(f"Peças faltando: {faltando}")
        return (
            f"✅  {self.chassi}  •  {self.motor}  •  "
            f"{self.rodas}  •  {self.cor}  •  {self.pneu}"
        )

    # ── Representação em texto ─────────────────────────────────────────────────
    def __str__(self) -> str:
        return (
            f"Carro(chassi={self.chassi!r}, motor={self.motor!r}, "
            f"rodas={self.rodas!r}, cor={self.cor!r}, pneu={self.pneu!r})"
        )

    # ── Método de classe ───────────────────────────────────────────────────────
    @classmethod
    def aleatorio(cls) -> "Carro":
        """Cria um carro com peças sorteadas aleatoriamente."""
        c = cls()
        c.chassi = Chassi(random.choice(Chassi.OPCOES))
        c.motor  = Motor(random.choice(Motor.OPCOES))
        c.rodas  = Rodas(random.choice(Rodas.OPCOES))
        c.cor    = Cor(random.choice(Cor.OPCOES))
        c.pneu   = Pneu(random.choice(Pneu.OPCOES))
        return c

    # ── Gerador de código para o painel direito ────────────────────────────────
    def gerar_codigo(self, modo: str = None) -> str:
        """Retorna o código Python que representa o uso deste objeto."""

        # always show the imports block
        linhas = [
            "from pecas import Chassi, Motor, Rodas, Cor, Pneu",
            "from carro import Carro",
        ]

        # ── show parts being instantiated as objects ───────────────────────────
        has_any = any([self.chassi, self.motor, self.rodas, self.cor, self.pneu])
        if has_any:
            linhas.append("")
            linhas.append("# Instanciando cada peça como um objeto")
            if self.chassi: linhas.append(f"chassi = {self.chassi!r}")
            if self.motor:  linhas.append(f"motor  = {self.motor!r}")
            if self.rodas:  linhas.append(f"rodas  = {self.rodas!r}")
            if self.cor:    linhas.append(f"cor    = {self.cor!r}")
            if self.pneu:   linhas.append(f"pneu   = {self.pneu!r}")

        # ── montado: compose the car ───────────────────────────────────────────
        if modo == "montado":
            linhas += [
                "",
                "# Compondo o carro (composição de objetos!)",
                "meu_carro = Carro()",
            ]
            if self.chassi: linhas.append("meu_carro.set_chassi(chassi)")
            if self.motor:  linhas.append("meu_carro.set_motor(motor)")
            if self.rodas:  linhas.append("meu_carro.set_rodas(rodas)")
            if self.cor:    linhas.append("meu_carro.set_cor(cor)")
            if self.pneu:   linhas.append("meu_carro.set_pneu(pneu)")
            linhas += [
                "",
                "resultado = meu_carro.montar()",
                "print(resultado)",
                "print(meu_carro)    # chama __str__",
            ]

        # ── aleatorio: use the classmethod ────────────────────────────────────
        elif modo == "aleatorio":
            linhas += [
                "",
                "# @classmethod — chama diretamente na classe, sem instanciar antes",
                "meu_carro = Carro.aleatorio()",
                "print(meu_carro)",
                f"# => {str(self)}",
            ]

        return "\n".join(linhas)
