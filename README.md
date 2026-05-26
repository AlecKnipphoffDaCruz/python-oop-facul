<div align="center">
  <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" width="260" alt="Python"/>
</div>

<br>

# 🚗 Monte seu Carro
### _Uma forma diferente de aprender Orientação a Objetos em Python_

<br>

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigma-OOP-27ae60?style=for-the-badge)
![UNISC](https://img.shields.io/badge/UNISC-Hora%20do%20Discovery-2980b9?style=for-the-badge)

<br>

> **Escolha o chassi. Escolha o motor. Escolha as rodas.**
> Quando você terminar de montar seu carro, vai perceber que acabou de escrever uma classe Python inteira — sem nem notar.

<br>

---

## 🎬 Demo

<div align="center">
  <video src="demo.mov" controls width="100%"></video>
</div>

<br>

---

## ✨ A ideia

Aprender OOP costuma parecer abstrato. *"O que é uma classe? O que é um objeto?"* São perguntas difíceis de responder com teoria.

Esse app inverte a lógica: **você age primeiro, entende depois.**

Enquanto você monta um carro escolhendo peças, o código Python aparece sendo construído em tempo real na tela. No final, você olha pro lado e percebe que acabou de:

- Definir atributos com `self`
- Instanciar um objeto com `Carro()`
- Compor classes com `Motor`, `Chassi`, `Rodas`
- Chamar um `@classmethod` com `Carro.aleatorio()`

<br>

---

## 🖥️ O app

A tela é dividida em três colunas que trabalham juntas:

```
┌─────────────────┬──────────────────────┬───────────────────────────┐
│   🔧  Oficina   │    🖼️  Seu Carro      │    🐍  Código Python       │
│                 │                      │                           │
│  Chassi  ▾      │   ╭──────────────╮   │  from pecas import Motor  │
│  Motor   ▾      │   │   🚗  (svg)  │   │                           │
│  Rodas   ▾      │   ╰──────────────╯   │  motor = Motor("2.0       │
│  Cor     ▾      │                      │           Turbo")         │
│  Pneu    ▾      │  [Esportivo][2.0]    │                           │
│                 │  [Aro 17][Vermelho]  │  meu_carro = Carro()      │
│  🔧 Montar      │                      │  meu_carro.set_motor(     │
│  🎲 Surpresa!   │  ✅ Carro montado!   │      motor)               │
└─────────────────┴──────────────────────┴───────────────────────────┘
```

<br>

### O carro muda de verdade

Cada seleção altera visualmente o SVG no centro:

| O que você escolhe | O que muda no carro |
|---|---|
| **Chassi** | Silhueta inteira (Esportivo é baixo, SUV é alto, Pickup tem caçamba) |
| **Cor** | Pintura do carro |
| **Rodas** | Tamanho do aro e espessura do pneu |
| **Motor** | Ícone aparece no capô (⚡ elétrico, 🔴 turbo, 🟢 flex, 🟡 híbrido) |
| **Pneu** | Número e estilo dos raios do aro |

<br>

---

## 🧠 Conceitos OOP ensinados

| Ação no app | Conceito demonstrado | Onde aparece no código |
|---|---|---|
| Cada peça tem sua própria classe | **Classe** | `class Motor:`, `class Chassi:` |
| `self._tipo` só acessado via getter | **Encapsulamento** | `@property` em cada `pecas/` |
| `Carro` usa objetos `Motor`, `Rodas`... | **Composição** | `carro.set_motor(motor)` |
| `from pecas import Motor` | **Módulos e importação** | Topo do código gerado |
| `Carro.aleatorio()` | **@classmethod** | Botão 🎲 Surpresa! |

<br>

---

## 🗂️ Estrutura do projeto

```
Python-OOP/
│
├── app.py              ← Interface Streamlit (3 colunas, SVG, estado)
├── carro.py            ← Classe Carro — composição de objetos
│
├── pecas/              ← Um arquivo por parte do carro
│   ├── chassi.py       ← class Chassi  (tipo: Esportivo, SUV...)
│   ├── motor.py        ← class Motor   (tipo: 1.0 Flex, Elétrico...)
│   ├── rodas.py        ← class Rodas   (aro: Aro 15, Aro 21...)
│   ├── cor.py          ← class Cor     (nome: Vermelho, Azul...)
│   └── pneu.py         ← class Pneu   (marca: Michelin, Pirelli...)
│
└── .streamlit/
    └── config.toml     ← Tema escuro
```

<br>

---

## 🚀 Como rodar

**1. Instale o Streamlit** (apenas uma vez):
```bash
python3 -m pip install streamlit
```

**2. Rode o app:**
```bash
python3 -m streamlit run app.py
```

Abre automaticamente em **http://localhost:8501** — melhor em tela cheia.

Para fechar: `Ctrl + C` no terminal.

<br>

---

## 👥 Sobre o projeto

Desenvolvido para a atividade **"Hora do Discovery"** da disciplina de Python na **UNISC**.

O objetivo é apresentar Orientação a Objetos de forma interativa — projetado na tela durante uma apresentação de 10 minutos, onde a turma monta carros ao vivo e percebe, quase sem querer, que está aprendendo OOP.

<br>

---

<div align="center">
  <sub>Feito com Python 🐍 + Streamlit ❤️</sub>
</div>
