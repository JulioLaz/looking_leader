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
         'font': {'size': 18, 'color': '#00ffff', 'family': 'Arial, sans-serif'},
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
    norm = (df['Puntaje_Liderazgo'] - df['Puntaje_Liderazgo'].min()) / (df['Puntaje_Liderazgo'].max() - df['Puntaje_Liderazgo'].min())
    colors = [px.colors.sequential.Viridis_r[int(i * (len(px.colors.sequential.Inferno_r) - 1))] for i in norm]
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
         'font': {'size': 18, 'color': '#00ffff', 'family': 'Arial, sans-serif'},
         'x': 0.5,  # Centrar el título
         'xanchor': 'center'
            },
         showlegend=False,
         height=530,
         # height=height,
         paper_bgcolor='black',
         plot_bgcolor='black', 
    )

    st.plotly_chart(fig, use_container_width=True)

def graf_embudo(df):
   norm = (df['Puntaje_Liderazgo'] - df['Puntaje_Liderazgo'].min()) / (df['Puntaje_Liderazgo'].max() - df['Puntaje_Liderazgo'].min())
   colors = [px.colors.sequential.Viridis_r[int(i * (len(px.colors.sequential.Inferno_r) - 1))] for i in norm]

   df_sorted = df.sort_values('Puntaje_Liderazgo', ascending=False)

   fig = go.Figure(go.Funnel(
      y = df_sorted['Nombre'],
      x = df_sorted['Puntaje_Liderazgo'],
      textposition = "inside",
      textinfo = "label+value+percent total",
      # textinfo = "label+value+percent initial",
      textfont=dict(size=12, family='Arial Black'),

      # opacity = 0.65,
        marker = {"color": colors,
                  "line": {"width": [1]*len(df), "color": ["white"]*len(df)}},
      # connector = {"line": {"color": "royalblue", "dash": "solid", "width": 3}}
   ))

   fig.update_layout(
      title={
         'text': f"Orden de Liderazgo",
         'font': {'size': 20, 'color': '#00ffff', 'family': 'Arial, sans-serif'},
         'x': 0.5,  # Centrar el título
         'y':.96,
         'xanchor': 'center'
            },
      # title_font=dict(size=24, color='skyblue'),
      plot_bgcolor='black',  # Dark background
      paper_bgcolor='black',  # Dark background
      height=600,
      margin=dict(l=0, r=0, t=50, b=0),
      yaxis=dict(
         showgrid=False,
         showline=False,
         showticklabels=False,
         tickfont=dict(color='white'),
      ),
      xaxis=dict(
         showgrid=False,
         showline=False,
         showticklabels=False,
      ),
      funnelmode="stack"
   )

   # Display the chart in Streamlit
   st.plotly_chart(fig, use_container_width=True)