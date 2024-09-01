from database import controller
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from utils import dataframe_helpers

ENTRADA = controller.ENTRADA
DESPESA = controller.DESPESA

def entries_by_categories_dashboard(df):
    """Entradas por categorias"""
    
    with st.container(border=True):
        # Gráfico de entradas por categoria
        fig_entradas = px.bar(df[df['tipo'] == ENTRADA], x='categoria', y='valor', title='Entradas por categoria',
                        labels={'valor': 'valor (R$)'}, color='categoria',
                        color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig_entradas)


def monthly_evolution_dashboard(df):
    """Evolução mensal"""

    if dataframe_helpers.check_empty_df(df):
        st.toast("Sem metrica para analisar", icon="📓")
        return

    with st.container(border=True):
        # Agrupando os dados para o gráfico de evolução mensal
        df_entradas = df[df['tipo'] == ENTRADA].groupby('data').sum().reset_index()
        df_despesas = df[df['tipo'] == DESPESA].groupby('data').sum().reset_index()
        df_entradas['Saldo Acumulado'] = df_entradas['valor'].cumsum() - df_despesas['valor'].cumsum()
        fig = go.Figure()

        # Adicionando barras para Entradas
        fig.add_trace(go.Bar(
            x=df_entradas['data'],
            y=df_entradas['valor'],
            name=ENTRADA,
            marker_color='rgb(55, 83, 109)'
        ))

        # Adicionando barras para Despesas
        fig.add_trace(go.Bar(
            x=df_despesas['data'],
            y=df_despesas['valor'],
            name=DESPESA,
            marker_color='rgb(26, 118, 255)'
        ))

        # Adicionando linha para Saldo Acumulado
        fig.add_trace(go.Scatter(
            x=df_entradas['data'],
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
                title='valor (R$)',
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


def expenses_by_categories_dashboard(df):
    """Despesas por categoria"""

    if dataframe_helpers.check_empty_df(df):
        st.toast("Sem metrica para analisar", icon="📓")
        return
    
    with st.container(border=True):
        # Gráfico de despesas por categoria
        fig_despesas = px.pie(df[df['tipo'] == DESPESA], names='categoria', values='valor', title='Despesas por categoria',
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