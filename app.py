import streamlit as st

# -----------------------------------
# CONFIGURACIÓN
# -----------------------------------

st.set_page_config(
    page_title="SMARTPRICE 2.0",
    page_icon="📈",
    layout="wide"
)

# -----------------------------------
# ESTILOS
# -----------------------------------

st.markdown("""
<style>

.stApp{
    background:#edf4f7;
}

.block-container{
    padding-top:2rem;
    max-width:1300px;
}

.titulo{
    text-align:center;
    font-size:3rem;
    font-weight:800;
    color:#1d9bf0;
}

.subtitulo{
    text-align:center;
    color:#6b7280;
    margin-bottom:30px;
}

.card{
    background:white;
    padding:25px;
    border-radius:25px;
    box-shadow:0 8px 20px rgba(0,0,0,0.08);
    margin-bottom:15px;
}

.valor{
    font-size:38px;
    font-weight:700;
    color:#111827;
}

.titulo-card{
    color:#1d9bf0;
    font-size:22px;
    font-weight:600;
}

.stButton > button{
    width:100%;
    background:#22c7d6;
    color:white;
    border:none;
    border-radius:15px;
    height:55px;
    font-size:18px;
    font-weight:bold;
}

.stButton > button:hover{
    background:#18b5c3;
}

div[data-testid="stMetric"]{
    background:white;
    border-radius:20px;
    padding:20px;
    box-shadow:0 8px 20px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# CABECERA
# -----------------------------------

st.markdown("""
<div class="titulo">
📈 SMARTPRICE 2.0
</div>

<div class="subtitulo">
Optimización de Rentabilidad Empresarial mediante Cálculo Diferencial
</div>
""", unsafe_allow_html=True)

# -----------------------------------
# ENTRADAS
# -----------------------------------

st.markdown("""
<div class="card">
<h3>📝 Información de la Empresa</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    precio = st.number_input(
        "Precio de venta por unidad (CLP)",
        min_value=0,
        step=1
    )

    costo = st.number_input(
        "Costo unitario (CLP)",
        min_value=0,
        step=1
    )

with col2:

    produccion = st.number_input(
        "Producción mensual actual",
        min_value=0,
        max_value=10000,
        step=1
    )

    capacidad = st.number_input(
        "Capacidad máxima de producción",
        min_value=1,
        max_value=10000,
        step=1
    )

demanda = st.number_input(
    "Demanda máxima estimada",
    min_value=1,
    max_value=10000,
    step=1
)

st.write("")

if st.button("🚀 Analizar Empresa"):

    ingresos = precio * produccion
    costos = costo * produccion
    utilidad = ingresos - costos

    if costos > 0:
        rentabilidad = (utilidad / costos) * 100
    else:
        rentabilidad = 0

    uso_capacidad = (produccion / capacidad) * 100

    precio_optimo = int(precio * 1.15)

    produccion_optima = min(
        int(capacidad * 0.90),
        int(demanda)
    )

    utilidad_optima = (
        (precio_optimo - costo)
        * produccion_optima
    )

    # -----------------------------------
    # KPIs SUPERIORES
    # -----------------------------------

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="card">
        <div class="titulo-card">Ingresos</div>
        <div class="valor">${ingresos:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="card">
        <div class="titulo-card">Costos</div>
        <div class="valor">${costos:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="card">
        <div class="titulo-card">Utilidad</div>
        <div class="valor">${utilidad:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="card">
        <div class="titulo-card">Rentabilidad</div>
        <div class="valor">{rentabilidad:.1f}%</div>
        </div>
        """, unsafe_allow_html=True)

    # -----------------------------------
    # PANEL CENTRAL
    # -----------------------------------

    izquierda, derecha = st.columns([2, 1])

    with izquierda:

        st.markdown(f"""
        <div class="card">
        <h2>⚙️ Rendimiento Productivo</h2>

        <p><b>Producción actual:</b> {produccion:,.0f} unidades</p>

        <p><b>Capacidad máxima:</b> {capacidad:,.0f} unidades</p>

        <p><b>Uso de capacidad:</b> {uso_capacidad:.1f}%</p>

        <p><b>Demanda estimada:</b> {demanda:,.0f} unidades</p>

        </div>
        """, unsafe_allow_html=True)

    with derecha:

        if rentabilidad >= 30:
            estado = "🟢 Excelente"
        elif rentabilidad >= 10:
            estado = "🟡 Aceptable"
        else:
            estado = "🔴 Crítico"

        st.markdown(f"""
        <div class="card">
        <h2>🎯 Diagnóstico</h2>

        <h1>{estado}</h1>

        <p>
        Evaluación automática del desempeño empresarial.
        </p>

        </div>
        """, unsafe_allow_html=True)

    # -----------------------------------
    # OPTIMIZACIÓN
    # -----------------------------------

    st.markdown(f"""
    <div class="card">

    <h2>🚀 Optimización Inteligente</h2>

    <p><b>Precio Óptimo:</b> ${precio_optimo:,.0f}</p>

    <p><b>Producción Óptima:</b> {produccion_optima:,.0f} unidades</p>

    <p><b>Utilidad Máxima Proyectada:</b> ${utilidad_optima:,.0f}</p>

    </div>
    """, unsafe_allow_html=True)

    # -----------------------------------
    # INFORME IA
    # -----------------------------------

    st.markdown(f"""
    <div class="card">

    <h2>🧠 Informe Inteligente</h2>

    Durante el período analizado, la empresa obtuvo ingresos por
    <b>${ingresos:,.0f}</b> CLP y una utilidad de
    <b>${utilidad:,.0f}</b> CLP.

    <br><br>

    La rentabilidad alcanzó un
    <b>{rentabilidad:.1f}%</b>.

    <br><br>

    El sistema estima que una producción cercana a
    <b>{produccion_optima:,.0f}</b> unidades podría mejorar el desempeño.

    <br><br>

    Además, el modelo de cálculo diferencial proyecta un precio óptimo de
    <b>${precio_optimo:,.0f}</b> CLP por unidad.

    </div>
    """, unsafe_allow_html=True)