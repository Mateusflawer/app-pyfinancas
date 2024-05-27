import streamlit as st
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
)

# Gerando dados fictícios para entradas e despesas mensais
categorias = ['Salário', 'Freelance', 'Investimentos', 'Presentes', 'Outros']
entradas = [4000, 1500, 800, 200, 300]
despesas = [1000, 500, 200, 150, 100]

# Expandindo os dados para múltiplos meses
datas = pd.date_range(start='2023-01-01', periods=6, freq='M')
data_expanded = {
    'Data': [],
    'Categoria': [],
    'Tipo': [],
    'Valor': []
}

for data in datas:
    for i, categoria in enumerate(categorias):
        data_expanded['Data'].append(data)
        data_expanded['Categoria'].append(categoria)
        data_expanded['Tipo'].append('Entradas')
        data_expanded['Valor'].append(entradas[i])
        data_expanded['Data'].append(data)
        data_expanded['Categoria'].append(categoria)
        data_expanded['Tipo'].append('Despesas')
        data_expanded['Valor'].append(despesas[i])

# Criação do DataFrame
df = pd.DataFrame(data_expanded)

ENTRADAS = 1000
DESPESAS = 500
SALDO = ENTRADAS - DESPESAS

# Metricas
col_saldo, col_entradas, col_despesas = st.columns(3)

with col_saldo.container(border=True):
    st.metric("Saldo", SALDO)

with col_entradas.container(border=True):
    st.metric("Entradas", ENTRADAS)

with col_despesas.container(border=True):
    st.metric("Despesas", DESPESAS)

##################

# Graficos categoria
coluna_1, coluna_2 = st.columns(2)

with coluna_1:
    with st.container(border=True):
        # Gráfico de entradas por categoria
        fig_entradas = px.bar(df[df['Tipo'] == 'Entradas'], x='Categoria', y='Valor', title='Entradas por Categoria',
                        labels={'Valor': 'Valor (R$)'}, color='Categoria',
                        color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_entradas)

    with st.container(border=True):
        # Agrupando os dados para o gráfico de evolução mensal
        df_entradas = df[df['Tipo'] == 'Entradas'].groupby('Data').sum().reset_index()
        df_despesas = df[df['Tipo'] == 'Despesas'].groupby('Data').sum().reset_index()
        df_entradas['Saldo Acumulado'] = df_entradas['Valor'].cumsum() - df_despesas['Valor'].cumsum()
        fig = go.Figure()

        # Adicionando barras para Entradas
        fig.add_trace(go.Bar(
            x=df_entradas['Data'],
            y=df_entradas['Valor'],
            name='Entradas',
            marker_color='rgb(55, 83, 109)'
        ))

        # Adicionando barras para Despesas
        fig.add_trace(go.Bar(
            x=df_despesas['Data'],
            y=df_despesas['Valor'],
            name='Despesas',
            marker_color='rgb(26, 118, 255)'
        ))

        # Adicionando linha para Saldo Acumulado
        fig.add_trace(go.Scatter(
            x=df_entradas['Data'],
            y=df_entradas['Saldo Acumulado'],
            mode='lines+markers',
            name='Saldo Acumulado',
            line=dict(color='rgb(255, 153, 51)', width=4, dash='dot')
        ))

        # Atualizando layout do gráfico
        fig.update_layout(
            title='Evolução Mensal de Entradas vs Despesas',
            xaxis_tickfont_size=14,
            yaxis=dict(
                title='Valor (R$)',
                titlefont_size=16,
                tickfont_size=14,
            ),
            legend=dict(
                x=0,
                y=1.0,
                bgcolor='rgba(255, 255, 255, 0)',
                bordercolor='rgba(255, 255, 255, 0)'
            ),
            barmode='group',
            bargap=0.15,
            bargroupgap=0.1
        )

        st.plotly_chart(fig)


with coluna_2:
    with st.container(border=True):
        # Gráfico de despesas por categoria
        fig_despesas = px.pie(df[df['Tipo'] == 'Despesas'], names='Categoria', values='Valor', title='Despesas por Categoria',
                        color_discrete_sequence=px.colors.qualitative.Pastel)
        fig_despesas.update_traces(textinfo='percent+label')
        st.plotly_chart(fig_despesas)

    with st.container(border=True):
        # Tabela de dados
        st.subheader("Tabela de dados")
        st.dataframe(df, use_container_width=True)
