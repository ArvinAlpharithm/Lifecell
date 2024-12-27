import streamlit as st
from streamlit.components.v1 import html

# Set page config for full width
st.set_page_config(
    page_title="Alpharithm HR",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# HTML content with responsive design
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Widget</title>
    <style>
        html, body {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100vh;
            background-color: #f0f0f0;
            overflow: hidden;
        }
        .container {
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        elevenlabs-convai {
            height: auto;
            width: auto;
            position: relative;
        }
        
        /* Desktop styles */
        @media screen and (min-width: 768px) {
            elevenlabs-convai {
                transform: scale(5);
            }
            .overlay {
                height: 120px;
            }
        }
        
        /* Tablet styles */
        @media screen and (min-width: 481px) and (max-width: 767px) {
            elevenlabs-convai {
                transform: scale(2);
            }
            .overlay {
                height: 250px;
            }
        }
        
        /* Mobile styles */
        @media screen and (max-width: 480px) {
            elevenlabs-convai {
                transform: scale(1);
            }
            .overlay {
                height: 320px;
            }
        }
        
        /* Common overlay styles */
        .overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            opacity: 1;
            background-color: #f0f0f0;
            z-index: 9999;
        }
    </style>
</head>
<body>
    <div class="container">
        <elevenlabs-convai agent-id="rMFc7PccmkPq7m0qAsxS"></elevenlabs-convai>
        <div class="overlay"></div>
    </div>
    <script src="https://elevenlabs.io/convai-widget/index.js" async type="text/javascript"></script>
</body>
</html>
"""

# Hide all Streamlit elements and remove padding/margins
hide_streamlit_style = """
<style>
    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
    #root > div:nth-child(1) > div > div > div > div {padding-top: 0rem;}
    .block-container {padding: 0rem 0rem !important;}
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    iframe {
        width: 100vw !important;
        height: 100vh !important;
        max-width: 100% !important;
    }
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Render the HTML content
html(html_content, height=1000, width=None)
