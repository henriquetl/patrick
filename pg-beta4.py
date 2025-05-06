import streamlit as st
from datetime import datetime, timedelta
from PIL import Image

def calcular_periodo_fertil(data_menstruacao, ciclo_medio):
    dia_ovulacao = data_menstruacao + timedelta(days=ciclo_medio // 2)
    inicio_fertil = dia_ovulacao - timedelta(days=5)
    fim_fertil = dia_ovulacao + timedelta(days=1)
    return inicio_fertil, fim_fertil

# --- EXIBIR IMAGEM ACIMA DO TÍTULO (centralizado com markdown) ---
imagem_topo = Image.open("logo-topo.jpeg")
nova_largura = 200
largura, altura = imagem_topo.size
nova_altura = int((nova_largura / largura) * altura)
imagem_topo = imagem_topo.resize((nova_largura, nova_altura))

# Converter a imagem para exibição centralizada com HTML
import base64
from io import BytesIO
buffered = BytesIO()
imagem_topo.save(buffered, format="PNG")
img_b64 = base64.b64encode(buffered.getvalue()).decode()

st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{img_b64}' width='{nova_largura}'/>
    </div>
    """,
    unsafe_allow_html=True
)

# --- TÍTULO CENTRALIZADO ---
st.markdown(
    "<h3 style='text-align: center;'>Patiguiquinho não quer ser (nem que você seja) papai, verifica a tabelinha! - Beta-0.4</h3>",
    unsafe_allow_html=True
)

# --- CENTRALIZAR DATA INPUT ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    data_menstruacao = st.date_input("Selecione a data do primeiro dia da última menstruação da nega a ser torada:")

# --- CENTRALIZAR SELECTBOX ---
with col2:
    ciclo_medio = st.selectbox("Quantos dias levam pra ela de um boi pra outro?", list(range(24, 35)), index=4)

# --- CENTRALIZAR BOTÃO PRINCIPAL ---
with col2:
    if st.button("Verificar os dias seguros pra torar a nega"):
        inicio_fertil, fim_fertil = calcular_periodo_fertil(data_menstruacao, ciclo_medio)

        dias_seguro = []
        hoje = datetime.today().date()
        for i in range(1, 6):
            dia_teste = hoje + timedelta(days=i)
            if not (inicio_fertil <= dia_teste <= fim_fertil):
                dias_seguro.append(dia_teste.strftime("%d/%m/%Y"))

        if dias_seguro:
            resultado_texto = "Pode gozar na caçapa da nega em:<br>" + "<br>".join(dias_seguro)
            imagem_resultado = Image.open("logo-patick.jpeg")
            nova_largura2 = 150
            largura2, altura2 = imagem_resultado.size
            nova_altura2 = int((nova_largura2 / largura2) * altura2)
            imagem_resultado = imagem_resultado.resize((nova_largura2, nova_altura2))
            buffered2 = BytesIO()
            imagem_resultado.save(buffered2, format="PNG")
            img_b64_2 = base64.b64encode(buffered2.getvalue()).decode()

            st.markdown(
                f"""
                <div style='text-align: center;'>
                    <img src='data:image/png;base64,{img_b64_2}' width='{nova_largura2}'/>
                    <div style='color: green; font-weight: bold;'>{resultado_texto}</div>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            resultado_texto = "Não há dias seguros para gozar na caçapa da nega, não jogue descalço!"
            imagem_alerta = Image.open("logo-alerta.jpeg")
            nova_largura2 = 150
            largura2, altura2 = imagem_alerta.size
            nova_altura2 = int((nova_largura2 / largura2) * altura2)
            imagem_alerta = imagem_alerta.resize((nova_largura2, nova_altura2))
            buffered2 = BytesIO()
            imagem_alerta.save(buffered2, format="PNG")
            img_b64_2 = base64.b64encode(buffered2.getvalue()).decode()

            st.markdown(
                f"""
                <div style='text-align: center;'>
                    <img src='data:image/png;base64,{img_b64_2}' width='{nova_largura2}'/>
                    <div style='color: red; font-weight: bold;'>{resultado_texto}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

# --- BOTÕES ADICIONAIS CENTRALIZADOS ---
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Instruções"):
        st.markdown(
            """
            <div style='text-align: center;'>
            • O ciclo menstrual é o período do primeiro dia de uma menstruação até o primeiro dia da próxima.<br>
            • A duração do ciclo varia de 24 a 34 dias para a maioria das mulheres.<br>
            • O aplicativo calcula o período fértil considerando ovulação por volta do meio do ciclo.<br>
            • Dias seguros são estimados fora do período fértil.
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button("A responsabilidade é tua carai!"):
        st.markdown(
            """
            <div style='text-align: center; color: orange;'>
            Este aplicativo é apenas para fins informativos.<br>
            Não garantimos a prevenção de gravidez.<br>
            Use métodos contraceptivos adequados e consulte um profissional de saúde.
            </div>
            """,
            unsafe_allow_html=True
        )

    if st.button("Créditos"):
        st.markdown(
            """
            <div style='text-align: center; color: purple;'>
            Esse app foi desenvolvido apenas para fins de entretenimento, use camisinha.<br>
            Desenvolvido por HL.
            </div>
            """,
            unsafe_allow_html=True
        )
