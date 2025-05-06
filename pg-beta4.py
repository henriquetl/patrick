import streamlit as st
from datetime import datetime, timedelta
from PIL import Image

def calcular_periodo_fertil(data_menstruacao, ciclo_medio):
    dia_ovulacao = data_menstruacao + timedelta(days=ciclo_medio // 2)
    inicio_fertil = dia_ovulacao - timedelta(days=5)
    fim_fertil = dia_ovulacao + timedelta(days=1)
    return inicio_fertil, fim_fertil

# ---- EXIBIR IMAGEM ACIMA DO TÍTULO ----
imagem_topo = Image.open("logo-topo.jpeg")  # Nome da sua nova imagem
st.image(imagem_topo, use_column_width=True)

st.title("Calculadora Patiguiquinho não quer ser papai - Versão Beta-0.1")

# Seletor de data
data_menstruacao = st.date_input("Selecione a data do primeiro dia da última menstruação da nega que eu vou torar:")

# Seletor de ciclo
ciclo_medio = st.selectbox("Quantos dias levam pra ela de um boi pra outro?", list(range(24, 35)), index=4)

# Botão para calcular
if st.button("Verificar os dias seguros pra torar a nega"):
    inicio_fertil, fim_fertil = calcular_periodo_fertil(data_menstruacao, ciclo_medio)

    dias_seguro = []
    hoje = datetime.today().date()
    for i in range(1, 6):
        dia_teste = hoje + timedelta(days=i)
        if not (inicio_fertil <= dia_teste <= fim_fertil):
            dias_seguro.append(dia_teste.strftime("%d/%m/%Y"))

    if dias_seguro:
        resultado_texto = "Pode gozar na caçapa da nega em:\n" + "\n".join(dias_seguro)
        imagem_resultado = Image.open("logo-patick.jpeg")
        st.image(imagem_resultado, width=150)
        st.success(resultado_texto)
    else:
        resultado_texto = "Não há dias seguros para gozar na caçapa da nega, não jogue descalço!"
        imagem_alerta = Image.open("logo-alerta.jpeg")  # nova imagem de alerta
        st.image(imagem_alerta, width=150)
        st.error(resultado_texto)

# Botões adicionais
if st.button("Instruções"):
    st.info("""
    • O ciclo menstrual é o período do primeiro dia de uma menstruação até o primeiro dia da próxima.
    • A duração do ciclo varia de 24 a 34 dias para a maioria das mulheres.
    • O aplicativo calcula o período fértil considerando ovulação por volta do meio do ciclo.
    • Dias seguros são estimados fora do período fértil.
    """)

if st.button("A responsabilidade é tua carai!"):
    st.warning("""
    Este aplicativo é apenas para fins informativos.
    Não garantimos a prevenção de gravidez.
    Use métodos contraceptivos adequados e consulte um profissional de saúde.
    """)

if st.button("Creditos"):
    disclaimer_texto = (
        "Esse app foi desenvolvido apenas para fins de entretenimento, use camisinha. Desenvolvido por HL."
    )
    st.warning(disclaimer_texto)