import pandas as pd
import requests
import streamlit as st

# https://docs.google.com/spreadsheets/d/1AoK3iyl88emnVbRJfrTjDhpIV47zmBCToGIW0tBuhHU/edit?usp=sharing
@st.cache_data
def load_data():
    gsheetid = '1AoK3iyl88emnVbRJfrTjDhpIV47zmBCToGIW0tBuhHU'
    sheetid = '700713393'
    # gsheetid = '1xoqR5jZa99UmIZ1nQxb7T_t29bsEO35F08yIinl-4Xo' # mes de julio
    # sheetid = '651754447' # mes de julio
    url = f'https://docs.google.com/spreadsheets/d/{gsheetid}/export?format=csv&gid={sheetid}'

    try:
        df = pd.read_csv(url)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Google Sheets: {e}")
        return pd.DataFrame()  # Return an empty DataFrame if there's an error
    return df

def calculate_code(value):
    if isinstance(value, str):
        if 'Ninguno' in value:
            return 0
        return sum(keyword in value for keyword in ['GitHub', 'editor']) * 5
    return 0

def replace_values(df, columns, replacement_dict):
    for column in columns:
        df[column] = df[column].replace(replacement_dict)
    return df

def feature():
    df=load_data().copy()
    df['Código'] = df['Código'].astype(str)
    df['Code'] = df['Código'].apply(calculate_code)

    exp_replacement_dict = {'nada': 0, 'poca': 3, 'media': 6, 'mucha': 10}
    cualidades_replacement_dict = {'poca': 3, 'media': 6, 'muy buena': 10}

    exp_columns = ['Experiencia  [En Data Science]', 'Experiencia  [En liderar grupos]']
    habilidades_columns = [
        'Habilidades blandas [¿Cuál es mi capacidad de manejo software para crear presentaciones?]',
        'Habilidades blandas [Mi capacidad de comunicación oral y/o escrita para contar historias (storytelling) con datos es...]',
        'Habilidades blandas [¿Cuál es mi capacidad presentar un proyecto?]'
    ]
    cualidades_columns = [
        'Cualidades [Empatía]', 'Cualidades [Colaboración]', 'Cualidades [Adaptabilidad]',
        'Cualidades [Flexibilidad]', 'Cualidades [Proactividad]'
    ]

    df = replace_values(df, exp_columns, exp_replacement_dict)
    df = replace_values(df, habilidades_columns, cualidades_replacement_dict)
    df = replace_values(df, cualidades_columns, cualidades_replacement_dict)

    df.drop(['Código', 'Puntuación'], axis=1, inplace=True)
    
    ob_columns = ['Python', 'Extracción', 'Limpieza', 'Análisis Exploratorio', 'Visualización']
    df[ob_columns] = df[ob_columns].astype('float16')

    df['Promedio_Tecnicas'] = df[['Experiencia  [En Data Science]', 'Python', 'Extracción', 'Limpieza',
                                  'Análisis Exploratorio', 'Visualización', 'Code']].mean(axis=1)
    df['Promedio_Blandas'] = df[habilidades_columns + cualidades_columns].mean(axis=1)
    df['Puntaje_Liderazgo'] = (df['Experiencia  [En liderar grupos]'] * 0.2 +
                               df['Promedio_Tecnicas'] * 0.6 +
                               df['Promedio_Blandas'] * 0.2)
    df['Nombre'] = df['Nombre'].str.strip()
    # df['Nombre'] = df['Nombre'].str.lower()
    df.sort_values('Grupo', ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    return df


columnas=['Nombre','Promedio_Tecnicas','Promedio_Blandas','Experiencia  [En Data Science]','Experiencia  [En liderar grupos]','Puntaje_Liderazgo','Grupo']

if __name__ == "__main__":
    df = load_data()
    if not df.empty:
        df_processed = feature()
        print(df_processed.info())
        print(df_processed.describe())
        print(df_processed[columnas].head(2))
    else:
        print("No data to process.")
