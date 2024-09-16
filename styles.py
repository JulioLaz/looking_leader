import streamlit as st

def style_gen():
   st.markdown("""<style>
   #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(9) > div > div{
        display:flex !important;
        justify-content: center;
    }               
   </style> """, unsafe_allow_html=True)

def text_input():
    st.markdown('''
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(3),
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(5) {
        display: flex;
        justify-content: center;
    }
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(3) > div,
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(5) > div {
        width: 20rem !important;
    }
    /* Estilos para el input de texto */
    .stTextInput > div > div > input {
        width: 20rem;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
    }
                
    .stRadio > div > div > div {
            display:flex !important;
            justify-content: center !important}
                
    .stButton > button {
        width: 20rem;
        padding: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
    }
                
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(7) > div{
               display: flex;
                justify-content: center;}

    .stButton > button:hover {background-color: #45a049}
                
    /*  centrar link de forms  */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(10) > div > div,                
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(5) > div > div{
            display:flex !important;
            justify-content: center !important}
                
    /*  hidden navbar initial */
#root > div:nth-child(1) > div.withScreencast > div > div > header > div.st-emotion-cache-15ecox0.ezrtsby0{
                display: none !important}    
                }                
#root > div:nth-child(1) > div.withScreencast > div > div > header > div.st-emotion-cache-15ecox0.ezrtsby0{
            display: none !important;
            background:none !important;
                } 
#root > div:nth-child(1) > div.withScreencast > div > div > header{
            display: none !important;
            background:none !important;
                } 
                              
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5{
padding-top: 0px !important
} 

    /* pg inicial   */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5{
    padding:0 !important;}
                                            
    /* input of the name */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(3) > div{
    width: min-content;}
                                
    /*inputs */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(5) > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(7) > div,
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(9) > div > div,                 
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(3){
    display: flex;
    justify-content: center;}
                             
    /*padding general */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5{
    width: 100%;
    padding: 1.5rem 1rem;
    min-width: auto;
    max-width: initial;}                                
    </style>''', unsafe_allow_html=True)  
   
def graficas():
    st.markdown('''<style>
    /* bordes de graf scatter pie & bar */            
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2),
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(1) > div > div > div > div > div > div > div > div > svg:nth-child(1){
            border: 1px solid #00ff00;
            border-radius: 5px;
            padding: 0 0 10px 0;
            text-align: center !important;
            font-size:10px !important;
            background-color:black;
    }            
    /* bordes de graf embudo */            
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(5) > div > div > div > div > svg:nth-child(5){
            border: 1px solid #00ff00;
            border-radius: 5px;
            padding: 5px;
    }            
    #tabs-bui3-tabpanel-0 > div > div > div > div > div > div > div > div > svg:nth-child(1){
            padding:0 20px;
                }

    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(8),
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div > div > div:nth-child(1) > div{
                display: flex;
                justify-content: center;
                }
    /*  btn inicio */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(6) > div{
    display: flex;
    justify-content:center;
    margin: 1rem;
                }
                /* hidden navbar streamlit */
    #root > div:nth-child(1) > div.withScreencast > div > div > header{
    display: none !important}                
             /* pg de graf */
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5{
    padding: 0 !important
                }         
    /*   btn   */
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-z5fcl4.ea3mdgi5 > div > div > div > div:nth-child(6) > div{
    display: flex;
    justify-content:center;
    margin-top:1rem;}                                       
    <style>''', unsafe_allow_html=True)
    
def radio():
        st.markdown("""
    <style>
    .stColumns {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: flex-end;
    }
    .stColumn {
        width: 48%;  /* Ajusta este valor según sea necesario */
    }
                /* centrar txt del error  */ 
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(8) > div > div > div > div > div > div > p{
    text-align: center !important;
                }
    </style>
    """, unsafe_allow_html=True)