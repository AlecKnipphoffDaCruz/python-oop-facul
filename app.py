import math
import inspect
import streamlit as st
from carro import Carro
from pecas import Chassi, Motor, Rodas, Cor, Pneu

st.set_page_config(
    page_title="Monte seu Carro — OOP em Python",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Data maps ──────────────────────────────────────────────────────────────────
PECAS = {
    "chassi": {"classe": Chassi, "label": "Chassi", "icon": "🚙", "opcoes": Chassi.OPCOES},
    "motor":  {"classe": Motor,  "label": "Motor",  "icon": "⚙️", "opcoes": Motor.OPCOES},
    "rodas":  {"classe": Rodas,  "label": "Rodas",  "icon": "🛞", "opcoes": Rodas.OPCOES},
    "cor":    {"classe": Cor,    "label": "Cor",    "icon": "🎨", "opcoes": Cor.OPCOES},
    "pneu":   {"classe": Pneu,   "label": "Pneu",   "icon": "🔘", "opcoes": Pneu.OPCOES},
}

COR_HEX = {
    "Vermelho": "#e74c3c",
    "Preto":    "#1c2233",
    "Branco":   "#dde3ec",
    "Azul":     "#2980b9",
    "Verde":    "#27ae60",
    "Amarelo":  "#f1c40f",
}

RODAS_RIM = {"Aro 15": 12, "Aro 17": 17, "Aro 19": 21, "Aro 21": 24}
PNEU_SPOKES = {"Michelin": 5, "Pirelli": 6, "Bridgestone": 4, "Continental": 3}
UNPAINTED = "#374151"

# ── SVG helpers ────────────────────────────────────────────────────────────────
def _wheel(cx, cy, rim_r=17, pneu=None):
    n = PNEU_SPOKES.get(pneu, 5)
    sw = 3 if n <= 4 else 2
    spokes = ""
    for i in range(n):
        angle = math.pi / 2 + (2 * math.pi / n) * i
        ex = cx + (rim_r - 2) * math.cos(angle)
        ey = cy + (rim_r - 2) * math.sin(angle)
        spokes += f'<line x1="{cx}" y1="{cy}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="#374151" stroke-width="{sw}"/>'
    return (
        f'<circle cx="{cx}" cy="{cy}" r="28" fill="#111827"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{rim_r}" fill="#1f2937"/>'
        f'{spokes}'
        f'<circle cx="{cx}" cy="{cy}" r="6" fill="#9ca3af"/>'
        f'<circle cx="{cx}" cy="{cy}" r="2.5" fill="#4b5563"/>'
    )

def _motor_icon(motor, x, y):
    if motor == "Elétrico":
        return (f'<path d="M {x+3},{y} L {x-2},{y+12} L {x+1},{y+12} '
                f'L {x-3},{y+24} L {x+7},{y+10} L {x+3},{y+10} Z" fill="#fbbf24" opacity="0.9"/>')
    elif motor == "2.0 Turbo":
        return (f'<ellipse cx="{x}" cy="{y+12}" rx="10" ry="7" fill="#ef4444" opacity="0.85"/>'
                f'<ellipse cx="{x}" cy="{y+12}" rx="6" ry="3.5" fill="#fca5a5" opacity="0.6"/>'
                f'<circle cx="{x}" cy="{y+12}" r="2.5" fill="#7f1d1d" opacity="0.9"/>')
    elif motor == "1.0 Flex":
        return (f'<circle cx="{x}" cy="{y+12}" r="9" fill="#22c55e" opacity="0.85"/>'
                f'<circle cx="{x}" cy="{y+12}" r="5" fill="#86efac" opacity="0.7"/>'
                f'<circle cx="{x}" cy="{y+12}" r="2" fill="#14532d" opacity="0.9"/>')
    elif motor == "Híbrido":
        r, cy2 = 9, y + 12
        return (f'<path d="M {x},{cy2-r} A {r},{r} 0 0,0 {x},{cy2+r} Z" fill="#22c55e" opacity="0.85"/>'
                f'<path d="M {x},{cy2-r} A {r},{r} 0 0,1 {x},{cy2+r} Z" fill="#fbbf24" opacity="0.85"/>'
                f'<circle cx="{x}" cy="{cy2}" r="3" fill="#f9fafb" opacity="0.8"/>')
    return ""

# ── Chassis body generators ────────────────────────────────────────────────────
def _body_esportivo(c):
    return f"""
  <rect x="18" y="108" width="364" height="50" rx="8" fill="{c}"/>
  <path d="M 76,108 L 108,61 L 268,55 L 312,106 L 312,108 Z" fill="{c}"/>
  <path d="M 76,108 L 108,61 L 268,55 L 312,106 L 312,108 Z" fill="rgba(0,0,0,0.09)"/>
  <path d="M 93,103 L 114,68 L 192,66 L 192,103 Z" fill="#bfdbfe" fill-opacity="0.82" stroke="rgba(0,0,0,0.18)" stroke-width="1.5"/>
  <path d="M 197,103 L 197,66 L 261,61 L 294,103 Z" fill="#bfdbfe" fill-opacity="0.82" stroke="rgba(0,0,0,0.18)" stroke-width="1.5"/>
  <rect x="18" y="126" width="364" height="2.5" rx="1" fill="rgba(255,255,255,0.17)"/>
  <line x1="194" y1="110" x2="192" y2="153" stroke="rgba(0,0,0,0.12)" stroke-width="2"/>
  <rect x="369" y="116" width="13" height="10" rx="4" fill="#fef3c7"/>
  <rect x="369" y="130" width="13" height="7"  rx="3" fill="#fcd34d" fill-opacity="0.65"/>
  <rect x="18"  y="116" width="11" height="10" rx="4" fill="#f87171"/>
  <rect x="18"  y="130" width="11" height="7"  rx="3" fill="#ef4444" fill-opacity="0.65"/>
  <rect x="371" y="140" width="11" height="18" rx="4" fill="rgba(0,0,0,0.25)"/>
  <rect x="313" y="76"  width="18" height="11" rx="3" fill="{c}" stroke="rgba(0,0,0,0.2)" stroke-width="1"/>"""

def _body_suv(c):
    return f"""
  <rect x="18" y="86" width="364" height="72" rx="8" fill="{c}"/>
  <path d="M 68,86 L 76,42 L 296,42 L 316,86 Z" fill="{c}"/>
  <path d="M 68,86 L 76,42 L 296,42 L 316,86 Z" fill="rgba(0,0,0,0.09)"/>
  <path d="M 84,80 L 90,50 L 192,50 L 192,80 Z" fill="#bfdbfe" fill-opacity="0.82" stroke="rgba(0,0,0,0.18)" stroke-width="1.5"/>
  <path d="M 197,80 L 197,50 L 298,50 L 306,80 Z" fill="#bfdbfe" fill-opacity="0.82" stroke="rgba(0,0,0,0.18)" stroke-width="1.5"/>
  <rect x="82"  y="40" width="206" height="3"   rx="1.5" fill="rgba(255,255,255,0.35)"/>
  <line x1="120" y1="40" x2="120" y2="46" stroke="rgba(255,255,255,0.35)" stroke-width="2"/>
  <line x1="180" y1="40" x2="180" y2="46" stroke="rgba(255,255,255,0.35)" stroke-width="2"/>
  <line x1="242" y1="40" x2="242" y2="46" stroke="rgba(255,255,255,0.35)" stroke-width="2"/>
  <rect x="18"  y="112" width="364" height="2.5" rx="1" fill="rgba(255,255,255,0.17)"/>
  <line x1="194" y1="88" x2="192" y2="153" stroke="rgba(0,0,0,0.12)" stroke-width="2"/>
  <rect x="369" y="96"  width="13" height="13" rx="4" fill="#fef3c7"/>
  <rect x="369" y="113" width="13" height="8"  rx="3" fill="#fcd34d" fill-opacity="0.65"/>
  <rect x="18"  y="96"  width="11" height="13" rx="4" fill="#f87171"/>
  <rect x="18"  y="113" width="11" height="8"  rx="3" fill="#ef4444" fill-opacity="0.65"/>
  <rect x="371" y="126" width="11" height="26" rx="4" fill="rgba(0,0,0,0.25)"/>
  <rect x="315" y="63"  width="18" height="11" rx="3" fill="{c}" stroke="rgba(0,0,0,0.2)" stroke-width="1"/>"""

def _body_seda(c):
    return f"""
  <rect x="18" y="100" width="364" height="58" rx="8" fill="{c}"/>
  <path d="M 88,100 L 113,60 L 274,55 L 304,100 Z" fill="{c}"/>
  <path d="M 88,100 L 113,60 L 274,55 L 304,100 Z" fill="rgba(0,0,0,0.09)"/>
  <line x1="88" y1="100" x2="88" y2="113" stroke="rgba(0,0,0,0.22)" stroke-width="2"/>
  <path d="M 101,95 L 120,68 L 192,66 L 192,95 Z" fill="#bfdbfe" fill-opacity="0.82" stroke="rgba(0,0,0,0.18)" stroke-width="1.5"/>
  <path d="M 197,95 L 197,66 L 268,62 L 289,95 Z" fill="#bfdbfe" fill-opacity="0.82" stroke="rgba(0,0,0,0.18)" stroke-width="1.5"/>
  <rect x="18"  y="118" width="364" height="2.5" rx="1" fill="rgba(255,255,255,0.17)"/>
  <line x1="194" y1="102" x2="192" y2="153" stroke="rgba(0,0,0,0.12)" stroke-width="2"/>
  <rect x="369" y="110" width="13" height="11" rx="4" fill="#fef3c7"/>
  <rect x="369" y="125" width="13" height="7"  rx="3" fill="#fcd34d" fill-opacity="0.65"/>
  <rect x="18"  y="110" width="11" height="11" rx="4" fill="#f87171"/>
  <rect x="18"  y="125" width="11" height="7"  rx="3" fill="#ef4444" fill-opacity="0.65"/>
  <rect x="371" y="136" width="11" height="22" rx="4" fill="rgba(0,0,0,0.25)"/>
  <rect x="303" y="74"  width="18" height="11" rx="3" fill="{c}" stroke="rgba(0,0,0,0.2)" stroke-width="1"/>"""

def _body_pickup(c):
    return f"""
  <rect x="16"  y="108" width="10" height="50" rx="3" fill="{c}"/>
  <rect x="16"  y="108" width="10" height="50" rx="3" fill="rgba(0,0,0,0.15)"/>
  <rect x="148" y="108" width="10" height="50" rx="3" fill="{c}"/>
  <rect x="148" y="108" width="10" height="50" rx="3" fill="rgba(0,0,0,0.3)"/>
  <rect x="26"  y="126" width="122" height="32" rx="3" fill="{c}"/>
  <rect x="26"  y="108" width="122" height="18" fill="rgba(0,0,0,0.5)"/>
  <rect x="150" y="93"  width="232" height="65" rx="8" fill="{c}"/>
  <path d="M 152,93 L 165,48 L 296,48 L 318,93 Z" fill="{c}"/>
  <path d="M 152,93 L 165,48 L 296,48 L 318,93 Z" fill="rgba(0,0,0,0.09)"/>
  <path d="M 167,88 L 174,56 L 236,55 L 236,88 Z" fill="#bfdbfe" fill-opacity="0.82" stroke="rgba(0,0,0,0.18)" stroke-width="1.5"/>
  <path d="M 241,88 L 241,55 L 300,55 L 312,88 Z" fill="#bfdbfe" fill-opacity="0.82" stroke="rgba(0,0,0,0.18)" stroke-width="1.5"/>
  <rect x="150" y="112" width="232" height="2.5" rx="1" fill="rgba(255,255,255,0.17)"/>
  <line x1="239" y1="95"  x2="237" y2="153" stroke="rgba(0,0,0,0.12)" stroke-width="2"/>
  <rect x="369" y="103" width="13" height="12" rx="4" fill="#fef3c7"/>
  <rect x="369" y="119" width="13" height="8"  rx="3" fill="#fcd34d" fill-opacity="0.65"/>
  <rect x="12"  y="116" width="10" height="10" rx="4" fill="#f87171"/>
  <rect x="12"  y="130" width="10" height="7"  rx="3" fill="#ef4444" fill-opacity="0.65"/>
  <rect x="371" y="132" width="11" height="26" rx="4" fill="rgba(0,0,0,0.25)"/>
  <rect x="317" y="67"  width="18" height="11" rx="3" fill="{c}" stroke="rgba(0,0,0,0.2)" stroke-width="1"/>"""

# chassis → (body_fn, wheel_front_x, wheel_rear_x, wheel_y, motor_icon_x, motor_icon_y)
CHASSIS_CFG = {
    "Esportivo": (_body_esportivo, 102, 295, 158, 340, 115),
    "SUV":       (_body_suv,       102, 298, 158, 340,  93),
    "Sedã":      (_body_seda,      102, 292, 158, 340, 107),
    "Pickup":    (_body_pickup,    280, 100, 158, 348, 100),
}

# ── Main SVG assembler ─────────────────────────────────────────────────────────
def car_svg(chassi=None, rodas=None, cor=None, motor=None, pneu=None) -> str:
    rim_r = RODAS_RIM.get(rodas, 17)

    if chassi is None:
        shadow  = '<ellipse cx="195" cy="183" rx="155" ry="5" fill="rgba(0,0,0,0.12)"/>'
        body    = """
  <path d="M 18,158 L 18,100 L 88,100 L 113,60 L 274,55 L 304,100 L 382,100 L 382,158 Z"
        fill="none" stroke="#30363d" stroke-width="2" stroke-dasharray="6 4"/>
  <path d="M 88,100 L 113,60 L 274,55 L 304,100 Z"
        fill="none" stroke="#30363d" stroke-width="2" stroke-dasharray="6 4"/>"""
        wr = '<circle cx="100" cy="158" r="28" fill="none" stroke="#30363d" stroke-width="2" stroke-dasharray="5 3"/>'
        wf = '<circle cx="292" cy="158" r="28" fill="none" stroke="#30363d" stroke-width="2" stroke-dasharray="5 3"/>'
        mi = ""
    else:
        color = COR_HEX.get(cor, UNPAINTED)
        fn, wfx, wrx, wy, mx, my = CHASSIS_CFG[chassi]
        shadow = '<ellipse cx="195" cy="183" rx="155" ry="7" fill="rgba(0,0,0,0.28)"/>'
        body   = fn(color)
        wr     = _wheel(wrx, wy, rim_r, pneu)
        wf     = _wheel(wfx, wy, rim_r, pneu)
        mi     = _motor_icon(motor, mx, my) if motor else ""

    return f"""
<div style="display:flex;justify-content:center;align-items:center;padding:20px 0 10px;">
<svg width="100%" viewBox="0 0 400 190" xmlns="http://www.w3.org/2000/svg">
  {shadow}
  {wr}
  {wf}
  {body}
  {mi}
</svg>
</div>"""


# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  .stApp { background: #0d1117; }
  #MainMenu, footer, header { visibility: hidden; }
  .block-container { padding-top: 1.8rem !important; padding-bottom: 0 !important; }
  .app-title {
    font-size: 1.75rem; font-weight: 800; color: #f0f6fc; letter-spacing: -0.5px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  }
  .app-sub {
    font-size: 0.82rem; color: #8b949e; margin-bottom: 1.6rem;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  }
  .col-label {
    font-size: 0.65rem; font-weight: 700; letter-spacing: 1.3px;
    text-transform: uppercase; color: #58a6ff; margin-bottom: 0.35rem;
  }
  .stSelectbox > label { color: #8b949e !important; font-size: 0.78rem !important; font-weight: 600 !important; }
  .spec-row { display: flex; flex-wrap: wrap; gap: 6px; justify-content: center; margin-top: 8px; }
  .spec-tag {
    background: #21262d; border: 1px solid #30363d; border-radius: 20px;
    padding: 3px 11px; font-size: 0.7rem; color: #c9d1d9;
    font-family: 'SF Mono', 'Fira Code', monospace;
  }
  .spec-empty { color: #484f58 !important; border-color: #21262d !important; }
  .result-box {
    margin-top: 12px; background: #0f2c0f; border: 1px solid #3fb950;
    border-radius: 8px; padding: 9px 14px; color: #3fb950;
    font-family: 'SF Mono', 'Fira Code', monospace; font-size: 0.82rem;
  }
  .warn-box {
    margin-top: 12px; background: #2d1b00; border: 1px solid #d29922;
    border-radius: 8px; padding: 9px 14px; color: #d29922;
    font-family: 'SF Mono', 'Fira Code', monospace; font-size: 0.82rem;
  }
</style>
""", unsafe_allow_html=True)


# ── Session state ──────────────────────────────────────────────────────────────
for k, v in {"_modo": None, "_trigger_aleatorio": False}.items():
    if k not in st.session_state:
        st.session_state[k] = v

if st.session_state._trigger_aleatorio:
    c_rand = Carro.aleatorio()
    for attr in PECAS:
        st.session_state[attr] = str(getattr(c_rand, attr))
    st.session_state._trigger_aleatorio = False

# ── Build current Carro ────────────────────────────────────────────────────────
carro = Carro()
for attr, meta in PECAS.items():
    val_str = st.session_state.get(attr)
    if val_str:
        getattr(carro, f"set_{attr}")(meta["classe"](val_str))

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="app-title">🚗  Monte seu Carro dos Sonhos</div>', unsafe_allow_html=True)
st.markdown('<div class="app-sub">Orientação a Objetos em Python — escolha as peças e veja o código sendo construído em tempo real</div>', unsafe_allow_html=True)

col_left, col_center, col_right = st.columns([1.1, 1.5, 1.65])

# ── LEFT ───────────────────────────────────────────────────────────────────────
with col_left:
    st.markdown('<div class="col-label">🔧  Oficina</div>', unsafe_allow_html=True)
    for attr, meta in PECAS.items():
        st.selectbox(f"{meta['icon']}  {meta['label']}", meta["opcoes"],
                     key=attr, index=None, placeholder=f"Selecione o {meta['label'].lower()}...")

    st.markdown("<br>", unsafe_allow_html=True)
    b1, b2 = st.columns(2)
    with b1:
        montar_clicked = st.button("🔧 Montar", type="primary", use_container_width=True)
    with b2:
        surp_clicked = st.button("🎲 Surpresa!", type="secondary", use_container_width=True)

    if montar_clicked:
        todos = all(st.session_state.get(a) for a in PECAS)
        if todos:
            st.session_state._modo = "montado"
        else:
            faltando = [PECAS[a]["label"] for a in PECAS if not st.session_state.get(a)]
            st.session_state._modo = None
            st.markdown(f'<div class="warn-box">⚠️ Faltam: {", ".join(faltando)}</div>', unsafe_allow_html=True)

    if surp_clicked:
        st.session_state._trigger_aleatorio = True
        st.session_state._modo = "aleatorio"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="border:1px solid #21262d;border-radius:8px;padding:12px;
                font-size:0.72rem;color:#8b949e;line-height:1.8;">
      <div style="color:#58a6ff;font-weight:700;margin-bottom:6px;
                  font-size:0.65rem;letter-spacing:1px;text-transform:uppercase;">Conceitos OOP</div>
      🔵 <b style="color:#c9d1d9">Classes</b> → Chassi, Motor, Rodas...<br>
      🟢 <b style="color:#c9d1d9">Encapsulamento</b> → _tipo, @property<br>
      🟡 <b style="color:#c9d1d9">Composição</b> → Carro tem Motor<br>
      🟠 <b style="color:#c9d1d9">Importação</b> → from pecas import ...<br>
      🔴 <b style="color:#c9d1d9">@classmethod</b> → Carro.aleatorio()
    </div>""", unsafe_allow_html=True)

# ── CENTER ─────────────────────────────────────────────────────────────────────
with col_center:
    st.markdown('<div class="col-label">🖼️  Seu Carro</div>', unsafe_allow_html=True)
    st.markdown(car_svg(
        chassi=st.session_state.get("chassi"),
        rodas=st.session_state.get("rodas"),
        cor=st.session_state.get("cor"),
        motor=st.session_state.get("motor"),
        pneu=st.session_state.get("pneu"),
    ), unsafe_allow_html=True)

    tags_html = '<div class="spec-row">'
    for attr, meta in PECAS.items():
        val = st.session_state.get(attr)
        tags_html += (f'<span class="spec-tag">{val}</span>' if val
                      else f'<span class="spec-tag spec-empty">{meta["label"]}</span>')
    tags_html += "</div>"
    st.markdown(tags_html, unsafe_allow_html=True)

    modo = st.session_state._modo
    if modo == "montado" and all(st.session_state.get(a) for a in PECAS):
        try:
            st.markdown(f'<div class="result-box">{carro.montar()}</div>', unsafe_allow_html=True)
        except ValueError:
            pass
    elif modo == "aleatorio":
        st.markdown('<div class="result-box">🎲  Carro gerado via <code>Carro.aleatorio()</code></div>', unsafe_allow_html=True)

# ── RIGHT ──────────────────────────────────────────────────────────────────────
with col_right:
    st.markdown('<div class="col-label">🐍  Código Python</div>', unsafe_allow_html=True)
    st.code(carro.gerar_codigo(modo=st.session_state._modo), language="python")

# ── Class viewer ───────────────────────────────────────────────────────────────
st.markdown("<br>", unsafe_allow_html=True)
with st.expander("🐍  Ver código das classes"):
    tabs = st.tabs(["Chassi", "Motor", "Rodas", "Cor", "Pneu", "Carro"])
    for tab, cls in zip(tabs, [Chassi, Motor, Rodas, Cor, Pneu, Carro]):
        with tab:
            st.code(inspect.getsource(cls), language="python")
