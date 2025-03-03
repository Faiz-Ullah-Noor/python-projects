import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

file_uploader = st.file_uploader("Choose a CSV file", type = "csv")

if file_uploader is not None:
    df = pd.read_csv(file_uploader)
    st.subheader("Data preview")
    st.write(df.head())

    st.subheader("Data summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_columns = st.selectbox("Select column to filter by",columns)
    unique_values = df[selected_columns].unique()
    selected_values = st.selectbox("Select value",unique_values)

    filtered_df = df[df[selected_columns] == selected_values]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select X_axis column",columns)
    y_column = st.selectbox("Select Y_axis column",columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])
else:
    st.write("Waiting on file uploading...")