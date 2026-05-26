# Monte seu Carro — OOP em Python

<div align="center">
  <img src="https://www.python.org/static/community_logos/python-logo-generic.svg" width="220" alt="Python"/>
</div>

<br>

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigma-OOP-27ae60?style=for-the-badge)
![UNISC](https://img.shields.io/badge/UNISC-Hora%20do%20Discovery-2980b9?style=for-the-badge)

</div>

<br>

Interactive web application for learning Object-Oriented Programming in Python. Users build a car by selecting parts — chassis, engine, wheels, color, and tires — while the corresponding Python code is generated in real time on screen.

---

## Layout

The interface is divided into three columns:

```
┌─────────────────┬──────────────────────┬───────────────────────────┐
│    Oficina      │      Seu Carro       │      Codigo Python        │
│                 │                      │                           │
│  Chassi  v      │   ╭──────────────╮   │  from pecas import Motor  │
│  Motor   v      │   │   (svg car)  │   │                           │
│  Rodas   v      │   ╰──────────────╯   │  motor = Motor("2.0       │
│  Cor     v      │                      │           Turbo")         │
│  Pneu    v      │  [Esportivo][2.0]    │                           │
│                 │  [Aro 17][Vermelho]  │  meu_carro = Carro()      │
│  Montar         │                      │  meu_carro.set_motor(     │
│  Surpresa!      │  Carro montado!      │      motor)               │
└─────────────────┴──────────────────────┴───────────────────────────┘
```

The SVG car updates with each selection — chassis shape, body color, wheel size, and a motor indicator on the hood all change dynamically.

---

## OOP Concepts

| User action | Concept | Code |
|---|---|---|
| Each part has its own class | Class | `class Motor:`, `class Chassi:` |
| `self._tipo` accessed via getter | Encapsulation | `@property` in each `pecas/` file |
| `Carro` holds `Motor`, `Rodas`... objects | Composition | `carro.set_motor(motor)` |
| `from pecas import Motor` | Module imports | Top of generated code |
| `Carro.aleatorio()` | @classmethod | Surpresa! button |

---

## Project Structure

```
Python-OOP/
├── app.py              — Streamlit UI (3 columns, SVG rendering, state)
├── carro.py            — Carro class (composes all parts)
├── pecas/
│   ├── chassi.py       — Chassi class
│   ├── motor.py        — Motor class
│   ├── rodas.py        — Rodas class
│   ├── cor.py          — Cor class
│   └── pneu.py         — Pneu class
└── .streamlit/
    └── config.toml     — Dark theme
```

---

## Getting Started

Install dependencies:
```bash
python3 -m pip install streamlit
```

Run:
```bash
python3 -m streamlit run app.py
```

Opens at `http://localhost:8501`. Press `Ctrl + C` to stop.

---

## About

Developed for the **Hora do Discovery** activity in the Python course at **UNISC**. Presented live in class as a 10-minute interactive session on Object-Oriented Programming.
