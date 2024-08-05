import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def graficas(df,grupo):
    df = df.sort_values('Puntaje_Liderazgo', ascending=True)
    df = df[df['Grupo']==grupo]
    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "bar"}, {"type": "pie"}]],
                    column_widths=[0.5, 0.5])
    # colors = px.colors.sequential.Viridis
    # colors = px.colors.sequential.Viridis_r[:len(df)]
    colors = px.colors.sequential.Inferno_r[:len(df)]

    # Destacar el mayor valor en la gráfica de pastel
    max_value_index = df['Puntaje_Liderazgo'].idxmax()
    pull_values = [0.1 if i == max_value_index else 0 for i in df.index]

    # Bar chart
    fig.add_trace(
        go.Bar(
            y=df['Nombre'],
            x=df['Puntaje_Liderazgo'],
            orientation='h',
            name='Puntuación',
            marker_color=colors,
            text=df['Puntaje_Liderazgo'].round(2),
            textposition='inside',
            insidetextanchor='end',
            textfont=dict(size=14, family='Arial Black'),
        ),
        row=1, col=1
    )

    # Pie chart
    fig.add_trace(
        go.Pie(
            labels=df['Nombre'],
            values=df['Puntaje_Liderazgo'].round(2),
            hole=0.3,
            name='Distribución',
            title=f'Grupo {grupo}',
            marker_colors=colors,
            textinfo='label+percent+value',
            textfont=dict(size=12, family='Arial Black'),
            insidetextorientation='radial',
            pull=pull_values

        ),
        row=1, col=2
    )

    fig.update_layout(
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=400,
    )

    fig.update_xaxes(showticklabels=False, row=1, col=1)
    fig.update_yaxes(showticklabels=True, tickfont=dict(size=16, family='Arial Black'), showgrid=False, row=1, col=1)
    st.plotly_chart(fig, use_container_width=True)