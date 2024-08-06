import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

height= 450
def grafica_bar_00(df, grupo):
    df = df.sort_values('Puntaje_Liderazgo', ascending=True)
    df = df[df['Grupo'] == grupo]

    # Normalizar los colores en función del rango de valores
    norm = (df['Puntaje_Liderazgo'] - df['Puntaje_Liderazgo'].min()) / (df['Puntaje_Liderazgo'].max() - df['Puntaje_Liderazgo'].min())
    colors = [px.colors.sequential.Viridis_r[int(i * (len(px.colors.sequential.Inferno_r) - 1))] for i in norm]

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            y=df['Nombre'],
            x=df['Puntaje_Liderazgo'],
            orientation='h',
            name='Puntuación',
            marker_color=colors,
            text=df['Puntaje_Liderazgo'].round(2),
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(size=14, family='Arial Black'),
        ))

    fig.update_layout(
         title={
         'text': f"Puntajes de Liderazgo",
         'font': {'size': 18, 'color': 'skyblue', 'family': 'Arial, sans-serif'},
         'x': 0.5,  # Centrar el título
         'xanchor': 'center'
            },
         showlegend=False,
         height=height,
         paper_bgcolor='black',
         plot_bgcolor='black',
         bargap=0.2,
         margin=dict(l=10, r=10, t=50, b=10))

    fig.update_xaxes(showticklabels=False)
    fig.update_yaxes(showticklabels=True, tickfont=dict(size=12, family='Arial Black'), showgrid=False)
    st.plotly_chart(fig, use_container_width=True)

def grafica_pie(df, grupo):
    df = df.sort_values('Puntaje_Liderazgo', ascending=True)
    df = df[df['Grupo'] == grupo]

    # Normalizar los colores en función del rango de valores
    norm = (df['Puntaje_Liderazgo'] - df['Puntaje_Liderazgo'].min()) / (df['Puntaje_Liderazgo'].max() - df['Puntaje_Liderazgo'].min())
    colors = [px.colors.sequential.Viridis_r[int(i * (len(px.colors.sequential.Inferno_r) - 1))] for i in norm]

    # Destacar el mayor valor en la gráfica de pastel
    max_value_index = df['Puntaje_Liderazgo'].idxmax()
    pull_values = [0.1 if i == max_value_index else 0 for i in df.index]

    fig = go.Figure()

    fig.add_trace(
        go.Pie(
            labels=df['Nombre'],
            values=df['Puntaje_Liderazgo'].round(2),
            hole=0.35,
            rotation=45,
            name='Distribución',
            title=f'Grupo {grupo}',
            marker_colors=colors,
            textinfo='label+percent+value',
            textfont=dict(size=12, family='Arial Black'),
            insidetextorientation='radial',
            pull=pull_values
        )
    )

    fig.update_layout(
         title={
         'text': f"Distribución de Liderazgo",
         'font': {'size': 18, 'color': 'skyblue', 'family': 'Arial, sans-serif'},
         'x': 0.5,  # Centrar el título
         'xanchor': 'center'
            },
         showlegend=False,
         height=height,
         paper_bgcolor='black',
         plot_bgcolor='black', 
    )

    st.plotly_chart(fig, use_container_width=True)

def grafica_bar(df, grupo):
    df = df[df['Grupo'] == grupo].sort_values('Puntaje_Liderazgo', ascending=True)

    # Normalizar los colores en función del rango de valores
    norm = (df['Puntaje_Liderazgo'] - df['Puntaje_Liderazgo'].min()) / (df['Puntaje_Liderazgo'].max() - df['Puntaje_Liderazgo'].min())
    colors = [px.colors.sequential.Viridis_r[int(i * (len(px.colors.sequential.Inferno_r) - 1))] for i in norm]

    fig = go.Figure()

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
            textfont=dict(size=12, family='Arial, sans-serif', color='white'),
            width=0.8,
        )
    )

    fig.update_layout(
        title={
            'text': f"Puntajes de Liderazgo - Grupo {grupo}",
            'font': {'size': 16, 'color': 'skyblue', 'family': 'Arial, sans-serif'},
            'x': 0.5,
            'xanchor': 'center'
        },
        showlegend=False,
        paper_bgcolor='black',
        plot_bgcolor='black',
        margin=dict(l=10, r=10, t=50, b=10),
        bargap=0.2,
        height=500,  # Altura fija inicial
    )

    fig.update_xaxes(showticklabels=False, showgrid=False, zeroline=False)
    fig.update_yaxes(
        showticklabels=True, 
        tickfont=dict(size=12, family='Arial, sans-serif', color='white'),
        showgrid=False,
        zeroline=False
    )

    # Ajuste responsivo
    st.markdown("""
        <style>
        .stPlotlyChart {
            width: 100% !important;
            max-width: 800px;
            margin: auto;
                
        }
        @media (max-width: 600px) {
            .stPlotlyChart {
                height: 400px !important;
            }
        }
        </style>
        """, unsafe_allow_html=True)

    # Usar el contenedor de Streamlit
    container = st.container()
    with container:
        st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False, 'responsive': True})