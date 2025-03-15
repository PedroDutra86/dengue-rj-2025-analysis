import streamlit as st
import pandas as pd

df = pd.read_csv("./dengue_2025_rj.csv")

st.title('Análise de Casos de Dengue no Rio de Janeiro (2025)')

st.markdown("""
    Esta aplicação exibe os dados relacionados aos casos de Dengue no Rio de Janeiro em 2025.
    O dataset contém informações sobre o município, quantidade de casos, e outras métricas importantes.
""")

st.subheader('Dados dos Casos de Dengue')
st.write(df)

municipio_filtro = st.selectbox('Selecione um município', df['ID_MUNICIP'].unique())

df_filtrado = df[df['ID_MUNICIP'] == municipio_filtro]

st.subheader(f'Dados para o município: {municipio_filtro}')
st.write(df_filtrado)

df_grouped = df.groupby('ID_MUNICIP').size().reset_index(name='casos_dengue')

st.subheader('Gráfico de Casos de Dengue por Município')
st.bar_chart(df_grouped.set_index('ID_MUNICIP')['casos_dengue']) 
st.write(df_grouped)

st.markdown("""
    Para mais informações sobre os códigos dos municípios, você pode acessar o 
    [site do IBGE](https://www.ibge.gov.br/explica/codigos-dos-municipios.php).
""")

st.sidebar.title("Informações das Variáveis")

informacoes = {
    "TP_NOT": "Tipo de notificação (se é suspeita, confirmação, etc.)",
    "ID_AGRAVO": "Código do agravo (doença)",
    "DT_NOTIFIC": "Data da notificação da doença",
    "SEM_NOT": "Semana epidemiológica da notificação",
    "NU_ANO": "Ano da notificação",
    "SG_UF_NOT": "Sigla da Unidade Federativa (Estado) da notificação",
    "ID_MUNICIP": "Código do município da notificação",
    "ID_REGIONA": "Código da região administrativa",
    "ID_UNIDADE": "Código da unidade de saúde que fez a notificação",
    "DT_SIN_PRI": "Data do início dos sintomas",
    "SEM_PRI": "Semana epidemiológica do início dos sintomas",
    "ANO_NASC": "Ano de nascimento do paciente",
    "NU_IDADE_N": "Idade do paciente",
    "CS_SEXO": "Sexo do paciente (Masculino ou Feminino)",
    "CS_GESTANT": "Código que indica se o paciente é gestante",
    "CS_RACA": "Código da raça/etnia do paciente",
    "CS_ESCOL_N": "Nível de escolaridade do paciente",
    "SG_UF": "Sigla do Estado de residência do paciente",
    "ID_MN_RESI": "Código do município de residência",
    "ID_RG_RESI": "Código da região de residência",
    "ID_PAIS": "Código do país de origem do paciente",
    "DT_INVEST": "Data do início da investigação",
    "ID_OCUPA_N": "Código de ocupação profissional do paciente",
    "FEBRE": "Indica presença de febre (sim/não)",
    "MIALGIA": "Indica presença de mialgia (dor muscular)",
    "CEFALEIA": "Indica presença de cefaleia (dor de cabeça)",
    "EXANTEMA": "Indica presença de exantema (erupção cutânea)",
    "VOMITO": "Indica presença de vômito",
    "NAUSEA": "Indica presença de náusea",
    "DOR_COSTAS": "Indica presença de dor nas costas",
    "CONJUNTVIT": "Indica presença de conjuntivite",
    "ARTRITE": "Indica presença de artrite",
    "ARTRALGIA": "Indica presença de dor nas articulações",
    "PETEQUIA_N": "Indica presença de petequias (pequenos pontos vermelhos na pele)",
    "LEUCOPENIA": "Indica presença de leucopenia (diminuição dos glóbulos brancos)",
    "LACO": "Relacionado ao diagnóstico ou sintomas (provavelmente algum fator específico relacionado à doença)",
    "DOR_RETRO": "Dor retro-orbital (atrás dos olhos)",
    "DIABETES": "Indica presença de diabetes",
    "HEMATOLOG": "Relacionado a exames hematológicos (sangue)",
    "HEPATOPAT": "Indica presença de hepatopatia (doenças do fígado)",
    "RENAL": "Indica presença de doença renal",
    "HIPERTENSA": "Indica presença de hipertensão (pressão alta)",
    "ACIDO_PEPT": "Pode se referir a alguma condição relacionada ao estômago (ex: ácido péptico)",
    "AUTO_IMUNE": "Indica doenças autoimunes",
    "DT_CHIK_S1": "Data do primeiro teste para Chikungunya",
    "DT_CHIK_S2": "Data do segundo teste para Chikungunya",
    "DT_PRNT": "Data de aplicação de algum teste específico (provavelmente para dengue)",
    "RES_CHIKS1": "Resultado do primeiro teste para Chikungunya",
    "RES_CHIKS2": "Resultado do segundo teste para Chikungunya",
    "RESUL_PRNT": "Resultado do teste específico (provavelmente para dengue)",
    "DT_SORO": "Data do teste sorológico",
    "RESUL_SORO": "Resultado do teste sorológico",
    "DT_NS1": "Data do teste NS1 (para detectar a presença do vírus)",
    "RESUL_NS1": "Resultado do teste NS1",
    "DT_VIRAL": "Data do teste viral",
    "RESUL_VI_N": "Resultado do teste viral",
    "DT_PCR": "Data do teste PCR (para detectar a presença do vírus)",
    "RESUL_PCR_": "Resultado do teste PCR",
    "SOROTIPO": "Sorotipo do vírus (ex: dengue tipo 1, tipo 2)",
    "HISTOPA_N": "Relacionado a histórico de patologias",
    "IMUNOH_N": "Imunização ou histórico de vacina",
    "HOSPITALIZ": "Indica se o paciente foi hospitalizado",
    "DT_INTERNA": "Data de internação hospitalar",
    "UF": "Unidade federativa (Estado) do paciente",
    "MUNICIPIO": "Município de residência do paciente",
    "TPAUTOCTO": "Tipo de autocontrole ou autocontaminação",
    "COUFINF": "Código para infecção relacionada à água, por exemplo",
    "COPAISINF": "Código para país de infecção",
    "COMUNINF": "Código para comunidade de infecção",
    "CLASSI_FIN": "Classificação final do caso (se é confirmado, suspeito, etc.)",
    "CRITERIO": "Critério utilizado para classificação final",
    "DOENCA_TRA": "Doença tratada (ou agravada por outro fator)",
    "CLINC_CHIK": "Clinicamente confirmado para Chikungunya",
    "EVOLUCAO": "Evolução do quadro de saúde do paciente",
    "DT_OBITO": "Data do óbito, se houver",
    "DT_ENCERRA": "Data de encerramento do caso",
    "ALRM_HIPOT": "Alarme para hipotensão (pressão baixa)",
    "ALRM_PLAQ": "Alarme para plaquetas baixas",
    "ALRM_VOM": "Alarme para vômito",
    "ALRM_SANG": "Alarme para sangramentos",
    "ALRM_HEMAT": "Alarme para hematomas (manchas roxas)",
    "ALRM_ABDOM": "Alarme para dor abdominal",
    "ALRM_LETAR": "Alarme para letargia (falta de energia)",
    "ALRM_HEPAT": "Alarme para hepatite",
    "ALRM_LIQ": "Alarme para distúrbios no líquido corporal",
    "DT_ALRM": "Data do alarme",
    "GRAV_PULSO": "Gravidade do pulso",
    "GRAV_CONV": "Gravidade das convulsões",
    "GRAV_ENCH": "Gravidade da encefalite (inflamação no cérebro)",
    "GRAV_INSUF": "Gravidade da insuficiência (ex: insuficiência renal)",
    "GRAV_TAQUI": "Gravidade da taquicardia (batimento cardíaco rápido)",
    "GRAV_EXTRE": "Gravidade da extremidade (doença grave nas extremidades)",
    "GRAV_HIPOT": "Gravidade da hipotensão (pressão baixa)",
    "GRAV_HEMAT": "Gravidade dos hematomas",
    "GRAV_MELEN": "Gravidade das melena (fezes escuras)",
    "GRAV_METRO": "Gravidade de metrorragia (sangramento uterino)",
    "GRAV_SANG": "Gravidade do sangramento",
    "GRAV_AST": "Gravidade de astemia (fraqueza geral)",
    "GRAV_MIOC": "Gravidade da miocárdio (relacionado ao coração)",
    "GRAV_CONSC": "Gravidade da consciência (estado de alerta do paciente)",
    "GRAV_ORGAO": "Gravidade da função dos órgãos",
    "DT_GRAV": "Data do evento grave",
    "MANI_HEMOR": "Manejo hemorrágico (tratamento de sangramentos)",
    "EPISTAXE": "Indica presença de epistaxe (sangramento nasal)",
    "GENGIVO": "Indica sangramento nas gengivas",
    "METRO": "Relacionado a metrorragia (sangramento uterino)",
    "PETEQUIAS": "Pequenos sangramentos na pele",
    "HEMATURA": "Sangue na urina",
    "SANGRAM": "Indica sangramento em algum local",
    "LACO_N": "Lacunas de dados ou informações faltantes",
    "PLASMATICO": "Indicativo de alteração plasmática (em exames de sangue)",
    "EVIDENCIA": "Evidências de complicações ou diagnósticos",
    "PLAQ_MENOR": "Plaquetas abaixo do normal",
    "CON_FHD": "Complicações com o estado de saúde",
    "COMPLICA": "Complicações durante o tratamento",
    "TP_SISTEMA": "Tipo de sistema de notificação",
    "NDUPLIC_N": "Indica duplicação de registros",
    "DT_DIGITA": "Data da digitalização ou entrada no sistema",
    "CS_FLXRET": "Código relacionado ao fluxo de retorno",
    "FLXRECEBI": "Indica o fluxo de recebimento de informações",
    "MIGRADO_W": "Indicativo de que os dados foram migrados para um novo sistema"
}

selecionadas = st.sidebar.multiselect(
    'Selecione as variáveis que deseja ver a descrição:',
    informacoes
)

if selecionadas:
    for var in selecionadas:
        if var in informacoes:
            st.write(f"**{var}:** {informacoes[var]}")
else:
    st.write("Nenhuma variável selecionada.")