import streamlit as st
import time
import json
import random
from datetime import datetime
from questoes import QUESTOES_POR_ANO, MATERIAS
from esconder_selo import esconder_selo_streamlit

# ─── PAGE CONFIG ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Simulado ITA — Aeronáutica",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)
esconder_selo_streamlit()  # oculta os controles do Streamlit Cloud

# ─── CSS ────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@300;400;600;700&family=Source+Serif+4:ital,wght@0,300;0,400;1,300&display=swap');

:root {
    --navy:    #0A1628;
    --blue:    #1B3A6B;
    --sky:     #1E5799;
    --gold:    #C9A84C;
    --gold2:   #F0D080;
    --silver:  #A8B4C8;
    --white:   #EDF0F7;
    --red:     #8B1A1A;
    --green:   #1A5C2E;
    --bg:      #070F1E;
}

html, body, [data-testid="stAppViewContainer"] {
    background: var(--bg) !important;
    color: var(--white) !important;
    font-family: 'Source Serif 4', serif;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0A1628 0%, #070F1E 100%) !important;
    border-right: 1px solid var(--gold);
}
[data-testid="stSidebar"] * { color: var(--white) !important; }

/* Header ornamental */
.ita-header {
    background: linear-gradient(135deg, var(--navy) 0%, var(--blue) 50%, var(--navy) 100%);
    border: 1px solid var(--gold);
    border-radius: 4px;
    padding: 28px 40px;
    text-align: center;
    position: relative;
    margin-bottom: 24px;
    box-shadow: 0 8px 40px rgba(201,168,76,0.15), inset 0 0 60px rgba(0,0,0,0.4);
}
.ita-header::before, .ita-header::after {
    content: '✦';
    color: var(--gold);
    position: absolute;
    top: 50%; transform: translateY(-50%);
    font-size: 18px;
}
.ita-header::before { left: 20px; }
.ita-header::after  { right: 20px; }

.ita-header h1 {
    font-family: 'Oswald', sans-serif;
    font-weight: 700;
    font-size: 2.4rem;
    color: var(--gold2) !important;
    letter-spacing: 4px;
    text-transform: uppercase;
    margin: 0;
    text-shadow: 0 0 30px rgba(201,168,76,0.5);
}
.ita-header p {
    font-family: 'Oswald', sans-serif;
    color: var(--silver) !important;
    letter-spacing: 3px;
    font-size: 0.85rem;
    margin-top: 6px;
    text-transform: uppercase;
}

/* Questão card */
.questao-card {
    background: linear-gradient(135deg, #0D1F3C 0%, #0A1628 100%);
    border: 1px solid rgba(201,168,76,0.3);
    border-left: 4px solid var(--gold);
    border-radius: 4px;
    padding: 28px 32px;
    margin-bottom: 24px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.4);
}
.questao-numero {
    font-family: 'Oswald', sans-serif;
    color: var(--gold) !important;
    font-size: 0.75rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 12px;
}
.questao-enunciado {
    font-size: 1.05rem;
    line-height: 1.75;
    color: var(--white) !important;
}

/* Alternativas */
.stRadio > div { gap: 10px !important; }
.stRadio label {
    background: rgba(27,58,107,0.3) !important;
    border: 1px solid rgba(201,168,76,0.2) !important;
    border-radius: 3px !important;
    padding: 12px 18px !important;
    cursor: pointer !important;
    transition: all 0.2s !important;
    color: var(--white) !important;
}
.stRadio label:hover {
    background: rgba(201,168,76,0.1) !important;
    border-color: var(--gold) !important;
}

/* Botões */
.stButton > button {
    font-family: 'Oswald', sans-serif !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
    background: linear-gradient(135deg, var(--blue) 0%, var(--sky) 100%) !important;
    border: 1px solid var(--gold) !important;
    color: var(--gold2) !important;
    border-radius: 3px !important;
    padding: 12px 28px !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 16px rgba(201,168,76,0.1) !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, var(--gold) 0%, var(--gold2) 100%) !important;
    color: var(--navy) !important;
    box-shadow: 0 4px 24px rgba(201,168,76,0.4) !important;
    transform: translateY(-1px) !important;
}

/* Gabarito correto/errado */
.correto {
    background: rgba(26,92,46,0.3) !important;
    border-color: #2ecc71 !important;
    padding: 12px 18px;
    border-radius: 3px;
    border-left: 4px solid #2ecc71;
    margin: 8px 0;
}
.errado {
    background: rgba(139,26,26,0.3) !important;
    border-color: #e74c3c !important;
    padding: 12px 18px;
    border-radius: 3px;
    border-left: 4px solid #e74c3c;
    margin: 8px 0;
}

/* Score card */
.score-card {
    background: linear-gradient(135deg, #0A1628 0%, #1B3A6B 100%);
    border: 2px solid var(--gold);
    border-radius: 6px;
    padding: 40px;
    text-align: center;
    box-shadow: 0 8px 40px rgba(201,168,76,0.2);
}
.score-number {
    font-family: 'Oswald', sans-serif;
    font-size: 5rem;
    font-weight: 700;
    color: var(--gold2) !important;
    text-shadow: 0 0 40px rgba(201,168,76,0.6);
    line-height: 1;
}
.score-label {
    font-family: 'Oswald', sans-serif;
    letter-spacing: 3px;
    color: var(--silver) !important;
    font-size: 0.85rem;
    text-transform: uppercase;
}

/* Timer */
.timer-display {
    font-family: 'Oswald', sans-serif;
    font-size: 1.8rem;
    color: var(--gold2);
    letter-spacing: 4px;
    text-align: center;
    padding: 12px;
    background: rgba(0,0,0,0.3);
    border: 1px solid rgba(201,168,76,0.3);
    border-radius: 3px;
    margin: 12px 0;
}

/* Divider ornamental */
.ornament {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 20px 0;
    color: var(--gold);
    font-size: 0.7rem;
    letter-spacing: 2px;
}
.ornament::before, .ornament::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--gold), transparent);
}

/* Métricas */
[data-testid="stMetricValue"] {
    font-family: 'Oswald', sans-serif !important;
    color: var(--gold2) !important;
    font-size: 2rem !important;
}
[data-testid="stMetricLabel"] {
    color: var(--silver) !important;
    letter-spacing: 1px !important;
}

/* Selectbox / slider */
.stSelectbox label, .stSlider label, .stMultiSelect label {
    font-family: 'Oswald', sans-serif !important;
    color: var(--silver) !important;
    letter-spacing: 1px !important;
    text-transform: uppercase !important;
    font-size: 0.8rem !important;
}

/* Watermark */
.brasao {
    font-size: 4rem;
    text-align: center;
    opacity: 0.08;
    position: fixed;
    bottom: 20px;
    right: 30px;
    pointer-events: none;
    z-index: 0;
}

/* Progress bar */
.stProgress > div > div > div {
    background: linear-gradient(90deg, var(--gold), var(--gold2)) !important;
}

/* Highlight matéria */
.materia-badge {
    display: inline-block;
    font-family: 'Oswald', sans-serif;
    font-size: 0.65rem;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 3px 10px;
    border: 1px solid var(--gold);
    border-radius: 2px;
    color: var(--gold);
    margin-bottom: 8px;
}

/* Expander */
.streamlit-expanderHeader {
    font-family: 'Oswald', sans-serif !important;
    color: var(--silver) !important;
    letter-spacing: 1px !important;
}
</style>

<div class="brasao">✈️</div>
""", unsafe_allow_html=True)


# ─── SESSION STATE ───────────────────────────────────────────────────────────────
def init_state():
    defaults = {
        "pagina": "home",
        "questoes_simulado": [],
        "respostas": {},
        "inicio": None,
        "idx": 0,
        "finalizado": False,
        "historico": [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()


# ─── HELPER ──────────────────────────────────────────────────────────────────────
def header(titulo, subtitulo=""):
    st.markdown(f"""
    <div class="ita-header">
        <h1>✈ {titulo}</h1>
        <p>{subtitulo}</p>
    </div>
    """, unsafe_allow_html=True)

def ornament(txt=""):
    st.markdown(f'<div class="ornament">{txt}</div>', unsafe_allow_html=True)

def formatar_tempo(segundos):
    h = int(segundos // 3600)
    m = int((segundos % 3600) // 60)
    s = int(segundos % 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


# ─── SIDEBAR ─────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 20px 0 10px;'>
        <div style='font-size:3rem;'>✈️</div>
        <div style='font-family:Oswald,sans-serif; font-size:1.1rem; letter-spacing:3px;
                    color:#C9A84C; text-transform:uppercase; margin-top:8px;'>
            Simulado ITA
        </div>
        <div style='font-family:Oswald,sans-serif; font-size:0.65rem; letter-spacing:2px;
                    color:#A8B4C8; margin-top:4px;'>
            Instituto Tecnológico de Aeronáutica
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    pages = {
        "🏠  Início": "home",
        "📝  Simulado": "simulado",
        "📊  Resultado": "resultado",
        "📚  Banco de Questões": "banco",
        "🏆  Histórico": "historico",
    }
    for label, page in pages.items():
        if st.button(label, use_container_width=True, key=f"nav_{page}"):
            st.session_state.pagina = page
            st.rerun()

    st.divider()

    # Progresso se simulado ativo
    if st.session_state.questoes_simulado and not st.session_state.finalizado:
        total = len(st.session_state.questoes_simulado)
        resp  = len(st.session_state.respostas)
        st.markdown(f"""
        <div style='font-family:Oswald,sans-serif; font-size:0.7rem; letter-spacing:2px;
                    color:#A8B4C8; text-align:center; text-transform:uppercase; margin-bottom:8px;'>
            Progresso
        </div>
        """, unsafe_allow_html=True)
        st.progress(resp / total if total else 0)
        st.markdown(f"<div style='text-align:center; color:#C9A84C; font-family:Oswald,sans-serif;'>{resp}/{total} questões</div>", unsafe_allow_html=True)

        if st.session_state.inicio:
            decorrido = time.time() - st.session_state.inicio
            st.markdown(f"<div class='timer-display'>{formatar_tempo(decorrido)}</div>", unsafe_allow_html=True)


# ─── HOME ─────────────────────────────────────────────────────────────────────────
def pagina_home():
    header("SIMULADO ITA", "Instituto Tecnológico de Aeronáutica • Vestibular")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class='questao-card' style='text-align:center;'>
            <div style='font-size:2.5rem;'>📐</div>
            <div style='font-family:Oswald,sans-serif; font-size:1.2rem; letter-spacing:2px; color:#C9A84C; margin-top:10px;'>Exatas</div>
            <div style='color:#A8B4C8; font-size:0.9rem; margin-top:8px;'>Matemática, Física<br>e Química</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class='questao-card' style='text-align:center;'>
            <div style='font-size:2.5rem;'>🌎</div>
            <div style='font-family:Oswald,sans-serif; font-size:1.2rem; letter-spacing:2px; color:#C9A84C; margin-top:10px;'>Humanas</div>
            <div style='color:#A8B4C8; font-size:0.9rem; margin-top:8px;'>Português e<br>Redação</div>
        </div>""", unsafe_allow_html=True)
    with col3:
        st.markdown("""
        <div class='questao-card' style='text-align:center;'>
            <div style='font-size:2.5rem;'>🔬</div>
            <div style='font-family:Oswald,sans-serif; font-size:1.2rem; letter-spacing:2px; color:#C9A84C; margin-top:10px;'>Ciências</div>
            <div style='color:#A8B4C8; font-size:0.9rem; margin-top:8px;'>Questões dos<br>últimos 4 anos</div>
        </div>""", unsafe_allow_html=True)

    ornament("CONFIGURE SEU SIMULADO")

    col_a, col_b = st.columns(2)
    with col_a:
        anos_disp = list(QUESTOES_POR_ANO.keys())
        anos_sel = st.multiselect("📅 Anos", anos_disp, default=anos_disp, key="anos_sel_home")

    with col_b:
        materias_disp = list(MATERIAS)
        mat_sel = st.multiselect("📚 Matérias", materias_disp, default=materias_disp, key="mat_sel_home")

    col_c, col_d = st.columns(2)
    with col_c:
        n_questoes = st.slider("🎯 Número de questões", 5, 60, 20, key="n_q_home")
    with col_d:
        modo = st.selectbox("⚙️ Modo", ["Cronometrado", "Livre", "Revisão imediata"], key="modo_home")

    ornament()

    if st.button("🚀  INICIAR SIMULADO", use_container_width=True):
        # Montar pool de questões
        pool = []
        for ano in (anos_sel or anos_disp):
            for q in QUESTOES_POR_ANO.get(ano, []):
                if not mat_sel or q["materia"] in mat_sel:
                    pool.append(q)

        if not pool:
            st.error("Nenhuma questão encontrada com esses filtros.")
            return

        random.shuffle(pool)
        st.session_state.questoes_simulado = pool[:n_questoes]
        st.session_state.respostas = {}
        st.session_state.idx = 0
        st.session_state.finalizado = False
        st.session_state.inicio = time.time()
        st.session_state.modo = modo
        st.session_state.pagina = "simulado"
        st.rerun()

    ornament()

    # Stats
    total_q = sum(len(v) for v in QUESTOES_POR_ANO.values())
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("📋 Total de Questões", total_q)
    c2.metric("📅 Anos Cobertos", len(QUESTOES_POR_ANO))
    c3.metric("📚 Matérias", len(MATERIAS))
    c4.metric("🏆 Simulados Feitos", len(st.session_state.historico))


# ─── SIMULADO ─────────────────────────────────────────────────────────────────────
def pagina_simulado():
    qs = st.session_state.questoes_simulado
    if not qs:
        st.warning("Nenhum simulado configurado. Volte ao Início.")
        return

    total = len(qs)

    # Timer no topo (se cronometrado)
    if st.session_state.get("modo") == "Cronometrado" and st.session_state.inicio:
        decorrido = time.time() - st.session_state.inicio
        col_t1, col_t2, col_t3 = st.columns([1, 1, 1])
        with col_t2:
            st.markdown(f"<div class='timer-display'>⏱ {formatar_tempo(decorrido)}</div>", unsafe_allow_html=True)

    header("SIMULADO ITA", f"Questão {st.session_state.idx + 1} de {total}")

    # Navegação rápida
    st.markdown("<div style='font-family:Oswald,sans-serif; font-size:0.7rem; letter-spacing:2px; color:#A8B4C8; text-transform:uppercase; margin-bottom:10px;'>Navegação rápida</div>", unsafe_allow_html=True)

    cols = st.columns(min(total, 15))
    for i, col in enumerate(cols[:total]):
        with col:
            if i in st.session_state.respostas:
                label = f"✓{i+1}"
            else:
                label = str(i + 1)
            if st.button(label, key=f"nav_q_{i}", use_container_width=True):
                st.session_state.idx = i
                st.rerun()

    ornament()

    q = qs[st.session_state.idx]

    st.markdown(f"""
    <div class='questao-card'>
        <div class='materia-badge'>{q['materia']} • ITA {q['ano']}</div>
        <div class='questao-numero'>QUESTÃO {st.session_state.idx + 1}</div>
        <div class='questao-enunciado'>{q['enunciado']}</div>
    </div>
    """, unsafe_allow_html=True)

    opcoes = q["alternativas"]
    resp_atual = st.session_state.respostas.get(st.session_state.idx)

    # Modo revisão imediata
    if st.session_state.get("modo") == "Revisão imediata" and resp_atual is not None:
        for letra, texto in opcoes.items():
            if letra == q["gabarito"]:
                st.markdown(f"<div class='correto'>✅ <b>{letra})</b> {texto}</div>", unsafe_allow_html=True)
            elif letra == resp_atual:
                st.markdown(f"<div class='errado'>❌ <b>{letra})</b> {texto}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='padding:12px 18px; color:#A8B4C8;'>{letra}) {texto}</div>", unsafe_allow_html=True)

        if q.get("solucao"):
            with st.expander("📖 Ver resolução"):
                st.markdown(q["solucao"])
    else:
        escolha = st.radio(
            "Escolha a alternativa:",
            options=list(opcoes.keys()),
            format_func=lambda x: f"{x})  {opcoes[x]}",
            index=list(opcoes.keys()).index(resp_atual) if resp_atual else 0,
            key=f"radio_{st.session_state.idx}",
            label_visibility="collapsed"
        )

        if st.button("💾  Confirmar Resposta", key="confirmar"):
            st.session_state.respostas[st.session_state.idx] = escolha
            if st.session_state.idx < total - 1:
                st.session_state.idx += 1
            st.rerun()

    ornament()

    col_prev, col_fin, col_next = st.columns([1, 1, 1])
    with col_prev:
        if st.session_state.idx > 0:
            if st.button("◀  Anterior", use_container_width=True):
                st.session_state.idx -= 1
                st.rerun()
    with col_fin:
        resp_count = len(st.session_state.respostas)
        if st.button(f"🏁  Finalizar ({resp_count}/{total})", use_container_width=True):
            # Salvar no histórico
            acertos = sum(
                1 for i, r in st.session_state.respostas.items()
                if r == qs[i]["gabarito"]
            )
            tempo = time.time() - st.session_state.inicio if st.session_state.inicio else 0
            st.session_state.historico.append({
                "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "total": total,
                "respondidas": resp_count,
                "acertos": acertos,
                "tempo": formatar_tempo(tempo),
            })
            st.session_state.finalizado = True
            st.session_state.pagina = "resultado"
            st.rerun()
    with col_next:
        if st.session_state.idx < total - 1:
            if st.button("Próxima  ▶", use_container_width=True):
                st.session_state.idx += 1
                st.rerun()


# ─── RESULTADO ────────────────────────────────────────────────────────────────────
def pagina_resultado():
    qs = st.session_state.questoes_simulado
    respostas = st.session_state.respostas

    if not qs:
        st.warning("Nenhum simulado para mostrar resultado.")
        return

    total = len(qs)
    respondidas = len(respostas)
    acertos = sum(1 for i, r in respostas.items() if r == qs[i]["gabarito"])
    erros = respondidas - acertos
    pct = (acertos / total * 100) if total else 0

    header("RESULTADO FINAL", "Desempenho no Simulado ITA")

    # Score card principal
    cor = "#2ecc71" if pct >= 60 else "#e67e22" if pct >= 40 else "#e74c3c"
    conceito = "APROVADO" if pct >= 60 else "ATENÇÃO" if pct >= 40 else "REPROVADO"

    st.markdown(f"""
    <div class='score-card'>
        <div style='font-family:Oswald,sans-serif; font-size:0.75rem; letter-spacing:4px; color:#A8B4C8;
                    text-transform:uppercase; margin-bottom:16px;'>Aproveitamento Geral</div>
        <div class='score-number' style='color:{cor} !important; text-shadow: 0 0 40px {cor}80;'>
            {pct:.1f}%
        </div>
        <div style='font-family:Oswald,sans-serif; font-size:1.5rem; color:{cor}; letter-spacing:4px;
                    margin-top:12px; text-transform:uppercase;'>{conceito}</div>
        <div class='score-label' style='margin-top:8px;'>
            {acertos} acertos de {total} questões
        </div>
    </div>
    """, unsafe_allow_html=True)

    ornament("DETALHAMENTO")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("✅ Acertos", acertos)
    c2.metric("❌ Erros", erros)
    c3.metric("⬜ Em branco", total - respondidas)
    c4.metric("📊 Aproveitamento", f"{pct:.1f}%")

    ornament("GABARITO COMPLETO")

    # Por matéria
    por_materia = {}
    for i, q in enumerate(qs):
        m = q["materia"]
        if m not in por_materia:
            por_materia[m] = {"acertos": 0, "total": 0}
        por_materia[m]["total"] += 1
        if i in respostas and respostas[i] == q["gabarito"]:
            por_materia[m]["acertos"] += 1

    col_stat = st.columns(len(por_materia)) if len(por_materia) <= 5 else st.columns(5)
    for idx, (mat, dados) in enumerate(por_materia.items()):
        col = col_stat[idx % len(col_stat)]
        pct_m = dados["acertos"] / dados["total"] * 100 if dados["total"] else 0
        col.metric(mat, f"{dados['acertos']}/{dados['total']}", f"{pct_m:.0f}%")

    ornament()

    # Questão a questão
    for i, q in enumerate(qs):
        resp = respostas.get(i)
        correto = resp == q["gabarito"]
        icone = "✅" if correto else ("❌" if resp else "⬜")
        cor_borda = "#2ecc71" if correto else ("#e74c3c" if resp else "#888")

        with st.expander(f"{icone}  Questão {i+1} — {q['materia']} (ITA {q['ano']})"):
            st.markdown(f"**Enunciado:** {q['enunciado']}")
            for letra, texto in q["alternativas"].items():
                if letra == q["gabarito"] and letra == resp:
                    st.markdown(f"<div class='correto'>✅ **{letra})** {texto} ← Sua resposta (correta)</div>", unsafe_allow_html=True)
                elif letra == q["gabarito"]:
                    st.markdown(f"<div class='correto'>✅ **{letra})** {texto} ← Gabarito</div>", unsafe_allow_html=True)
                elif letra == resp:
                    st.markdown(f"<div class='errado'>❌ **{letra})** {texto} ← Sua resposta</div>", unsafe_allow_html=True)
                else:
                    st.write(f"{letra}) {texto}")
            if q.get("solucao"):
                st.markdown(f"**📖 Resolução:** {q['solucao']}")

    ornament()

    if st.button("🔄  Novo Simulado", use_container_width=True):
        st.session_state.pagina = "home"
        st.session_state.questoes_simulado = []
        st.session_state.respostas = {}
        st.session_state.finalizado = False
        st.rerun()


# ─── BANCO DE QUESTÕES ────────────────────────────────────────────────────────────
def pagina_banco():
    header("BANCO DE QUESTÕES", "Acervo Completo ITA 2021–2024")

    col_f1, col_f2 = st.columns(2)
    with col_f1:
        filtro_ano = st.selectbox("Filtrar por ano", ["Todos"] + list(QUESTOES_POR_ANO.keys()))
    with col_f2:
        filtro_mat = st.selectbox("Filtrar por matéria", ["Todas"] + list(MATERIAS))

    todas = []
    for ano, qs in QUESTOES_POR_ANO.items():
        for q in qs:
            q_copy = q.copy()
            q_copy["ano"] = ano
            todas.append(q_copy)

    if filtro_ano != "Todos":
        todas = [q for q in todas if q["ano"] == filtro_ano]
    if filtro_mat != "Todas":
        todas = [q for q in todas if q["materia"] == filtro_mat]

    st.markdown(f"<div style='font-family:Oswald,sans-serif; color:#A8B4C8; letter-spacing:2px; font-size:0.8rem; margin-bottom:16px;'>{len(todas)} QUESTÃO(ÕES) ENCONTRADA(S)</div>", unsafe_allow_html=True)

    for i, q in enumerate(todas):
        with st.expander(f"[{q['ano']}] {q['materia']} — Questão {i+1}"):
            st.markdown(f"<div class='questao-enunciado'>{q['enunciado']}</div>", unsafe_allow_html=True)
            for letra, texto in q["alternativas"].items():
                if letra == q["gabarito"]:
                    st.markdown(f"**✅ {letra})** {texto}")
                else:
                    st.write(f"{letra}) {texto}")
            if q.get("solucao"):
                st.info(f"📖 Resolução: {q['solucao']}")


# ─── HISTÓRICO ────────────────────────────────────────────────────────────────────
def pagina_historico():
    header("HISTÓRICO DE SIMULADOS", "Seus resultados anteriores")

    if not st.session_state.historico:
        st.markdown("""
        <div class='questao-card' style='text-align:center; padding:60px;'>
            <div style='font-size:3rem;'>📊</div>
            <div style='font-family:Oswald,sans-serif; color:#A8B4C8; letter-spacing:2px; margin-top:16px;'>
                Nenhum simulado realizado ainda
            </div>
        </div>
        """, unsafe_allow_html=True)
        return

    for idx, h in enumerate(reversed(st.session_state.historico)):
        pct = (h["acertos"] / h["total"] * 100) if h["total"] else 0
        cor = "#2ecc71" if pct >= 60 else "#e67e22" if pct >= 40 else "#e74c3c"
        st.markdown(f"""
        <div class='questao-card'>
            <div style='display:flex; justify-content:space-between; align-items:center;'>
                <div>
                    <div class='questao-numero'>{h['data']}</div>
                    <div style='font-family:Oswald,sans-serif; font-size:1.1rem; color:#EDF0F7;'>
                        Simulado #{len(st.session_state.historico) - idx}
                    </div>
                    <div style='color:#A8B4C8; font-size:0.9rem; margin-top:6px;'>
                        {h['acertos']} acertos • {h['respondidas']}/{h['total']} respondidas • ⏱ {h['tempo']}
                    </div>
                </div>
                <div style='font-family:Oswald,sans-serif; font-size:2.5rem; color:{cor}; font-weight:700;'>
                    {pct:.0f}%
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─── ROUTER ───────────────────────────────────────────────────────────────────────
PAGE_MAP = {
    "home":      pagina_home,
    "simulado":  pagina_simulado,
    "resultado": pagina_resultado,
    "banco":     pagina_banco,
    "historico": pagina_historico,
}

PAGE_MAP.get(st.session_state.pagina, pagina_home)()
