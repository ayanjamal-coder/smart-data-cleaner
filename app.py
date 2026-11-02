import streamlit as st
import pandas as pd

# 1. Page Configuration (Title and Icon)
st.set_page_config(page_title="DataViz Studio", page_icon="📊", layout="wide")

st.title("📊 DataViz Studio - Instant Data Cleaner & Dashboard")
st.write("Upload your CSV file to clean data and explore insights automatically!")

# 2. File Uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the dataset using pandas
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    # Tab layout for clean organization
    tab1, tab2, tab3 = st.tabs(["📋 Data Preview", "🧹 Data Cleaning", "📈 Visualizations"])

    # --- TAB 1: DATA PREVIEW ---
    with tab1:
        st.subheader("Raw Data Preview")
        st.dataframe(df, use_container_width=True)

        st.subheader("Quick Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Rows", len(df))
        col2.metric("Total Columns", len(df.columns))
        col3.metric("Duplicate Rows", df.duplicated().sum())

    # --- TAB 2: DATA CLEANING ---
    with tab2:
        st.subheader("Data Cleaning Options")

        # Handle Missing Values
        missing_count = df.isnull().sum().sum()
        st.write(f"**Total Missing Values:** {missing_count}")

        if st.button("Remove Duplicate Rows"):
            df = df.drop_duplicates()
            st.success("Duplicates removed!")

        if st.button("Drop Rows with Missing Values"):
            df = df.dropna()
            st.success("Missing values dropped!")

        st.subheader("Updated Data")
        st.dataframe(df, use_container_width=True)

    # --- TAB 3: VISUALIZATIONS ---
    with tab3:
        st.subheader("Interactive Charts")

        # Select numeric columns only
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

        if numeric_cols:
            selected_col = st.selectbox("Select a column to visualize:", numeric_cols)

            col_a, col_b = st.columns(2)

            with col_a:
                st.write("### Bar Chart")
                st.bar_chart(df[selected_col])

            with col_b:
                st.write("### Line Chart")
                st.line_chart(df[selected_col])
        else:
            st.warning("No numeric columns found in this file to build charts!")

else:
    st.info("Please upload a CSV file from the top to get started.")