import streamlit as st
import pandas as pd
import plotly.express as px

# Load the CSV file
df = pd.read_csv("phytochemicals.csv")

# Strip whitespace from column names just in case
df.columns = df.columns.str.strip()

# Title
st.title("Phytochemical Search App")

# Show all columns for debug (optional, remove later)
st.write("📋 Columns loaded:", df.columns.tolist())

# Search box
search_term = st.text_input("🔍 Search by chemical name:")

# If the user enters a search term
if search_term:
    # Filter the dataframe using the correct column name
    result = df[df['Chemical name'].str.contains(search_term, case=False, na=False)]

    # Show the result
    st.write(f"Showing results for: **{search_term}**")
    st.dataframe(result)

    # Optional: plot QEDw scores if multiple matches
    if len(result) > 1:
        fig = px.histogram(result, x="QEDw", title="QEDw Score Distribution")
        st.plotly_chart(fig)
else:
    st.info("Enter a chemical name to search.")

# Optional: Show entire data table
with st.expander("📄 Show full data"):
    st.dataframe(df)

