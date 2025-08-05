import streamlit as st
import pandas as pd
from utils import detect_loops, visualize_graph
from logger import setup_logger

logger = setup_logger()

st.set_page_config(page_title="Approval Loop Detector", layout="wide")

st.title("🔁 Approval Loop Detection App")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("File uploaded successfully!")
        st.dataframe(df.head())

        st.subheader("Detected Approval Loops")

        loops = detect_loops(df)

        if loops:
            for idx, loop in enumerate(loops, start=1):
                st.write(f"Loop {idx}: {' ➝ '.join(loop)}")
        else:
            st.write("✅ No loops found.")

        st.subheader("Approval Flow Network")
        fig = visualize_graph(df)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Error: {e}")
        logger.exception("Error in Streamlit app")
