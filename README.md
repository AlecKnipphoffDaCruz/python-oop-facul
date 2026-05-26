# 🚗 Monte seu Carro — OOP em Python

Aplicativo interativo para aprender **Orientação a Objetos em Python** montando um carro.

---

## Pré-requisitos

- Python 3.9 ou superior
- Verifique com: `python3 --version`

---

## Instalação

```bash
python3 -m pip install streamlit
```

---

## Como rodar

```bash
cd ~/Desktop/facul/Python-OOP
python3 -m streamlit run app.py
```

O navegador abre automaticamente em `http://localhost:8501`.

---

## Estrutura do projeto

```
Python-OOP/
├── app.py          → interface (Streamlit)
├── carro.py        → classe Carro (composição)
├── pecas/
│   ├── chassi.py   → classe Chassi
│   ├── motor.py    → classe Motor
│   ├── rodas.py    → classe Rodas
│   ├── cor.py      → classe Cor
│   └── pneu.py     → classe Pneu
└── requirements.txt
```

---

## Conceitos OOP demonstrados

| Ação no app | Conceito |
|---|---|
| Cada peça tem sua própria classe | **Classe** |
| `self._tipo` com `@property` | **Encapsulamento** |
| `Carro` usa objetos `Motor`, `Rodas`... | **Composição** |
| `from pecas import Motor` | **Importação de módulos** |
| `Carro.aleatorio()` | **@classmethod** |
