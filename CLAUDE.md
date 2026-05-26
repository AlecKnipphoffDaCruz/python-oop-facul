# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the app

```bash
python3 -m pip install streamlit      # one-time install
python3 -m streamlit run app.py       # starts at http://localhost:8501
```

## Architecture

This is a single-page Streamlit app that teaches OOP concepts interactively. The core logic is intentionally split across multiple files to demonstrate Python module structure to students.

**Data flow:**
1. `app.py` reads `st.session_state` for the 5 selections (chassi, motor, rodas, cor, pneu)
2. Builds a `Carro` object by instantiating each `pecas/` class and calling the corresponding setter
3. Calls `carro.gerar_codigo(modo)` to produce the Python code shown in the right panel
4. Calls `car_svg(...)` to produce the SVG shown in the center panel

**OOP model (`carro.py` + `pecas/`):**
- Each car part is its own class in `pecas/` with a `OPCOES` list, a private attribute (`_tipo`/`_aro`/`_nome`/`_marca`), a `@property` getter/setter, `__str__`, and `__repr__`
- `Carro` composes these via typed setters (`set_chassi(chassi: Chassi)`, etc.)
- `Carro.aleatorio()` is a `@classmethod` that instantiates all 5 part classes from their respective `OPCOES`
- `Carro.gerar_codigo(modo)` returns a Python code string for the UI panel; `modo` is `None`, `"montado"`, or `"aleatorio"`

**SVG rendering (`app.py`):**
- `car_svg(chassi, rodas, cor, motor, pneu)` assembles SVG from helpers
- `_body_esportivo/suv/seda/pickup(color)` — one function per chassis shape, returns raw SVG string
- `CHASSIS_CFG` dict maps chassis name → `(body_fn, wheel_front_x, wheel_rear_x, wheel_y, motor_icon_x, motor_icon_y)`
- `_wheel(cx, cy, rim_r, pneu)` — rim radius from `RODAS_RIM`, spoke count from `PNEU_SPOKES`
- `_motor_icon(motor, x, y)` — small SVG icon placed on the hood
- No chassis selected → dashed ghost outline

**Streamlit state:**
- Selectbox values are stored in `st.session_state` under their attribute name (`"chassi"`, `"motor"`, etc.)
- `st.session_state._modo` — `None | "montado" | "aleatorio"` — controls which code section appears
- `st.session_state._trigger_aleatorio` — transient bool; set to `True` before `st.rerun()`, handled at the top of the next render cycle before widgets are drawn

## Adding a new chassis type

1. Add the string to `Chassi.OPCOES` in `pecas/chassi.py`
2. Write a `_body_<name>(color)` function in `app.py` returning SVG elements
3. Add an entry to `CHASSIS_CFG` in `app.py`

## Adding a new color

Add to `COR_HEX` in `app.py` and to `Cor.OPCOES` in `pecas/cor.py`.
