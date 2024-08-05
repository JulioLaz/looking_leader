# Proyecto de Evaluación de Liderazgo en Data Science

Este proyecto utiliza Streamlit y Plotly para visualizar y analizar datos de evaluación de candidatos para posiciones de liderazgo en Data Science.

# App
https://looking-leader.streamlit.app/

# Formulario para datos:
https://docs.google.com/spreadsheets/d/1xoqR5jZa99UmIZ1nQxb7T_t29bsEO35F08yIinl-4Xo/edit?usp=sharing

## Características

- Visualización de datos mediante gráficos interactivos
- Análisis de habilidades técnicas y blandas
- Evaluación de experiencia en Data Science y liderazgo de grupos
- Cálculo y visualización de puntajes de liderazgo

## Gráficos Implementados

### 1. Gráfico de Barras Horizontal
![image](https://github.com/user-attachments/assets/28f52fd5-7349-4527-b822-c9e441bdae54)


Este gráfico muestra los puntajes de liderazgo de los candidatos en un formato de barras horizontales. Características:
- Barras coloreadas según el puntaje de liderazgo
- Etiquetas de texto dentro de las barras
- Diseño responsivo para dispositivos móviles

### 2. Gráfico de Pastel
![image](https://github.com/user-attachments/assets/51948861-1117-429e-b6fd-1a79c7c5db04)

Muestra la distribución de los puntajes de liderazgo en un gráfico de pastel. Características:
- Colores normalizados según el puntaje
- Resalta el valor más alto
- Muestra etiquetas, porcentajes y valores

### 3. Gráfico de Dispersión
![image](https://github.com/user-attachments/assets/f5483093-0a42-4a57-9b28-5ad1103df53d)

Este gráfico de dispersión proporciona una visión completa de los candidatos. Características:
- Eje X: Habilidades Técnicas
- Eje Y: Habilidades Blandas
- Tamaño de los puntos: Experiencia total
- Color de los puntos: Puntaje de Liderazgo
- Cuadrantes coloreados para categorización rápida

## Cómo usar

1. Asegúrate de tener instalado Streamlit y Plotly.
2. Ejecuta la aplicación con `streamlit run nombre_del_archivo.py`.
3. Selecciona un grupo para visualizar los datos correspondientes.
4. Interactúa con los gráficos para obtener más información sobre los candidatos.

## Requisitos

- Python 3.7+
- Streamlit
- Plotly
- Pandas (para manejo de datos)

## Instalación

```bash
pip install streamlit plotly pandas
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios mayores antes de hacer un pull request.

## Licencia

[MIT](https://choosealicense.com/licenses/mit/)
