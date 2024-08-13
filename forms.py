import streamlit as st

    # <a href="https://docs.google.com/forms/d/e/1FAIpQLSdW37CVsihwoAQKNtrEmAiczfjGPEV_rqHVZ4t5WruJXJ7lPQ/viewform?usp=sf_link" target="_blank" style="
def forms():
    html = """
    <div style="
    text-align: center;
    margin-top: 10px;
    border: 1px solid rgb(0, 255, 0);
    border-radius: 5px;
    padding: 10px 0;
    width: 20rem;
    background-color: #143417;">
    <a href="https://forms.gle/9dhuSWxhNLRTCfhJ6" target="_blank" style="
        display: block;
        text-decoration: none;
        color: #fff;
        padding: 10px 0;">
        <div style="display: flex">
            <img style="padding:4px 0; width: 3rem" src="https://img.icons8.com/ios-filled/50/ffffff/google-forms.png" alt="Google Forms Icon" />
            <span style="width: 15rem; padding-right:2px; font-size: 1rem; vertical-align: middle;">
                Si aún no llenaste el formulario o deseas modificar tus datos, haz click aquí
            </span>
        </div>
    </a>
</div>
    """
    st.markdown(html, unsafe_allow_html=True)
    # <div style="
    #     text-align: center;
    #     margin-top: 10px;
    #     border: 1px solid rgb(0, 255, 0);
    #     border-radius: 5px;
    #     padding: 10px 0;
    #     width: 20rem;
    #     background-color: #143417>
    #     <a href="https://docs.google.com/forms/d/e/1FAIpQLSdW37CVsihwoAQKNtrEmAiczfjGPEV_rqHVZ4t5WruJXJ7lPQ/viewform?usp=sf_link" target="_blank" style="text-decoration: none;">
    #         <div style='display: flex'>
    #             <img style='padding:4px 0; width: 3rem' src="https://img.icons8.com/ios-filled/50/ffffff/google-forms.png" alt="Google Forms Icon" style="vertical-align: middle;"/>
    #             <span style="width: 15rem; padding-right:2px; font-size: 1rem; color: #fff; vertical-align: middle;">Si aún no llenaste el formulario o deseas modificar tus datos haz click en este link!</span>
    #         </div>
    #     </a>
    # </div>