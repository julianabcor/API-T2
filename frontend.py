
import streamlit as st
from consumidor_api import obter_dados

st.set_page_config(
    page_title="Monitoramento Meteorológico",
    page_icon="🌦️",
    layout="wide"
)

st.title("🌦️ Monitoramento Meteorológico")
st.caption("Estação meteorológica — Jaraguá do Sul/SC")

st.divider()

if st.button("🔄 Atualizar dados"):
    st.rerun()

try:
    with st.spinner("Consultando a API meteorológica..."):
        dados = obter_dados()

    st.success("Dados meteorológicos carregados.")

    st.subheader("Condições atuais")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "A temperatura é:",
        f"{dados["current"]['temperature_2m']:.1f} °C"
    )

    col2.metric(
        "A umidade é:",
        f"{dados["current"]['relative_humidity_2m']:.0f} %"
    )

    col3.metric(
        "A sensação térmica é:",
        f"{dados["current"]['apparent_temperature']:.1f} °C"
    )

    col4, col5 = st.columns(2)

    col4.metric(
        "A precipitação de chuva é:",
        f"{dados["current"]['precipitation']:.1f} mm"
    )

    col5.metric(
        "A velocidade do vento é:",
        f"{dados["current"]['wind_speed_10m']:.1f} km/h"
    )

    st.divider()

    st.caption(f"Data/hora: {dados["current"]['time']}")

except Exception as erro:
    st.error(f"Não foi possível consultar os dados: {erro}")


