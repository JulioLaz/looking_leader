import streamlit as st

# HTML para el icono y el enlace
def forms():
   html = """
   <div style="text-align: center;">
      <a href="https://docs.google.com/forms/d/e/1FAIpQLSdW37CVsihwoAQKNtrEmAiczfjGPEV_rqHVZ4t5WruJXJ7lPQ/viewform?usp=sf_link" target="_blank" style="text-decoration: none;">
         <img src="https://img.icons8.com/ios-filled/50/ffffff/google-forms.png" alt="Google Forms Icon" style="vertical-align: middle;"/>
         <span style="font-size: 1.2rem; color: #fff; vertical-align: middle;">Si aún no llenaste el formulario o deseas modificar tus datos haz click en el link del forms!</span>
      </a>
   </div>
   """

   # Mostrar el HTML en Streamlit
   st.markdown(html, unsafe_allow_html=True)
