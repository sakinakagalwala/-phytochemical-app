import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV, skip the first descriptive row
df = pd.read_csv("phytochemicals.csv", skiprows=1)

# Clean up column names
df.columns = df.columns.str.strip()

# Rename columns for clarity (adjust as per your CSV structure)
df.columns = ['IMPPAT_ID', 'Chemical_Name', 'SMILES', 'InChI', 'QEDw']

# Page title
st.title("🌿 Phytochemical Search App")

# Search input
search_term = st.text_input("🔍 Search by chemical name:")

# Filtered search results
if search_term:
    result = df[df['Chemical_Name'].str.contains(search_term, case=False, na=False)]
    st.subheader(f"🔎 Results for: *{search_term}*")
    st.dataframe(result)

    if len(result) > 1:
        fig = px.histogram(result, x="QEDw", title="QEDw Score Distribution")
        st.plotly_chart(fig)
else:
    st.info("Enter a chemical name to search.")

# Compound dropdown selector
st.subheader("🧬 Select a compound to view details")
compound_list = df['Chemical_Name'].dropna().unique()
selected = st.selectbox("Choose a compound:", compound_list)

# Display details of selected compound
selected_row = df[df['Chemical_Name'] == selected].iloc[0]
st.markdown(f"**🆔 IMPPAT ID:** {selected_row['IMPPAT_ID']}")
st.markdown(f"**🧪 SMILES:** {selected_row['SMILES']}")
st.markdown(f"**🧬 InChI:** {selected_row['InChI']}")
st.markdown(f"**📊 QEDw Score:** {selected_row['QEDw']}")

# Show full dataset if needed
with st.expander("📄 Show full dataset"):
    st.dataframe(df)


