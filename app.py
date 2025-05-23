import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV and skip first row
df = pd.read_csv("phytochemicals.csv", skiprows=1)
df.columns = df.columns.str.strip()

# Title
st.title("Phytochemical Search App")

# Debug: Show columns
st.write("📋 Columns loaded:", df.columns.tolist())

# Search box
search_term = st.text_input("🔍 Search by chemical name:")

# Filter results
if search_term:
    result = df[df['Chemical name'].str.contains(search_term, case=False, na=False)]
    st.write(f"Results for: **{search_term}**")
    st.dataframe(result)

    # Optional: QEDw chart
    if len(result) > 1:
        fig = px.histogram(result, x="QEDw", title="QEDw Score Distribution")
        st.plotly_chart(fig)
else:
    st.info("Enter a chemical name to search.")

# Optional: full dataset
with st.expander("📄 Show full data"):
    st.dataframe(df)


