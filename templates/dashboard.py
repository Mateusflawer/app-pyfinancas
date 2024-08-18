from streamlit_extras.metric_cards import style_metric_cards
import plotly.graph_objects as go
from utils import calculations
import plotly.express as px
from data import controller
import streamlit as st

ENTRADA = controller.TIPOS[0] # Entrada
DESPESAS = controller.TIPOS[1] # Despesas

def metrics(df):
    """Metricas"""
    saldo, entradas, despesas = calculations.dashboard_metrics(df)

    # Metricas
    col_saldo, col_entradas, col_despesas = st.columns(3)

    with col_saldo:
        st.metric("Saldo", saldo)

    with col_entradas:
        st.metric("Entradas", entradas)

    with col_despesas:
        st.metric("Despesas", despesas)

    style_metric_cards(background_color='auto')


def entries_by_categories(df):
    """Entradas por categorias"""
    with st.container(border=True):
        # Gráfico de entradas por categoria
        fig_entradas = px.bar(df[df['Tipo'] == ENTRADA], x='Categoria', y='Valor', title='Entradas por Categoria',
                        labels={'Valor': 'Valor (R$)'}, color='Categoria',
                        color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_entradas)


def monthly_evolution(df):
    """Evolução mensal"""
    with st.container(border=True):
        # Agrupando os dados para o gráfico de evolução mensal
        df_entradas = df[df['Tipo'] == ENTRADA].groupby('Data').sum().reset_index()
        df_despesas = df[df['Tipo'] == DESPESAS].groupby('Data').sum().reset_index()
        df_entradas['Saldo Acumulado'] = df_entradas['Valor'].cumsum() - df_despesas['Valor'].cumsum()
        fig = go.Figure()

        # Adicionando barras para Entradas
        fig.add_trace(go.Bar(
            x=df_entradas['Data'],
            y=df_entradas['Valor'],
            name=ENTRADA,
            marker_color='rgb(55, 83, 109)'
        ))

        # Adicionando barras para Despesas
        fig.add_trace(go.Bar(
            x=df_despesas['Data'],
            y=df_despesas['Valor'],
            name=DESPESAS,
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


def expenses_by_categories(df):
    """Despesas por categoria"""
    with st.container(border=True):
        # Gráfico de despesas por categoria
        fig_despesas = px.pie(df[df['Tipo'] == DESPESAS], names='Categoria', values='Valor', title='Despesas por Categoria',
                        color_discrete_sequence=px.colors.qualitative.Pastel)
        fig_despesas.update_traces(textinfo='percent+label')
        st.plotly_chart(fig_despesas)


def indicador():

    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 270,
        title = {'text': "Progresso"},
        gauge = {
            'axis': {'range': [0, 500]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 250], 'color': "lightgray"},
                {'range': [250, 400], 'color': "gray"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 490
            }
        }
    ))

    st.plotly_chart(fig)