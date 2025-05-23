import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV (skip the first row if it’s a description)
df = pd.read_csv("phytochemicals.csv", skiprows=1)

# Clean and rename columns
df.columns = df.columns.str.strip()
df.columns = ['IMPPAT_ID', 'Chemical_Name', 'SMILES', 'InChI', 'QEDw']

# App title
st.title("🌿 Phytochemical Search & Bioactivity App")

# Sidebar filters
st.sidebar.header("🔎 Filter Options")
search_term = st.sidebar.text_input("Search by chemical name:")

# QEDw filter
min_qed, max_qed = st.sidebar.slider("Filter by QEDw Score:", 0.0, 1.0, (0.3, 0.9))

# Apply filters
filtered_df = df[df['QEDw'].between(min_qed, max_qed)]
if search_term:
    filtered_df = filtered_df[filtered_df['Chemical_Name'].str.contains(search_term, case=False, na=False)]

# Results display
st.subheader("🧬 Filtered Phytochemicals")
st.write(f"Found {len(filtered_df)} compound(s).")

# Download button
st.download_button("📥 Download CSV", filtered_df.to_csv(index=False), "filtered_phytochemicals.csv")

# Show results in a table
st.dataframe(filtered_df)

# Show QEDw histogram
if not filtered_df.empty:
    fig = px.histogram(filtered_df, x="QEDw", nbins=20, title="📊 QEDw Score Distribution")
    st.plotly_chart(fig)

# Compound detail viewer
st.subheader("🔬 Compound Detail Viewer")
compound_list = filtered_df['Chemical_Name'].dropna().unique()
if len(compound_list) > 0:
    selected = st.selectbox("Select a compound to view details:", compound_list)
    selected_row = filtered_df[filtered_df['Chemical_Name'] == selected].iloc[0]

    st.markdown(f"**🆔 IMPPAT ID:** `{selected_row['IMPPAT_ID']}`")
    st.markdown("**🧪 SMILES:**")
    st.code(selected_row['SMILES'], language='text')

    st.markdown("**🧬 InChI:**")
    st.code(selected_row['InChI'], language='text')

    st.markdown(f"**📊 QEDw Score:** `{selected_row['QEDw']}`")

    # PubChem link
    pubchem_url = f"https://pubchem.ncbi.nlm.nih.gov/#query={selected_row['Chemical_Name']}"
    st.markdown(f"[🔗 View on PubChem]({pubchem_url})", unsafe_allow_html=True)

# Full data toggle
with st.expander("📄 Show full original dataset"):
    st.dataframe(df)
