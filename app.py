import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("phytochemicals.csv")

st.title("Phytochemical Explorer")

search_term = st.text_input("Search by Chemical Name:")

# Filter and display
if search_term:
    result = df[df['Chemical Name'].str.contains(search_term, case=False, na=False)]
    st.dataframe(result)
else:
    st.info("Type a chemical name to begin.")

# Optional: Visualize QEDw score
if 'QEDw Score' in df.columns:
    st.subheader("QEDw Score Distribution")
    fig = px.histogram(df, x='QEDw Score', nbins=20)
    st.plotly_chart(fig)
