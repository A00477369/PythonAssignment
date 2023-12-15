import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def load_and_validate_csv(file):
    try:
        df = pd.read_csv(file)
        if 'Name' not in df.columns or 'Age' not in df.columns:
            st.error("Invalid CSV file. Please ensure the file has 'Name' and 'Age' columns.")
            return None
        return df
    except Exception as e:
        st.error(f"Error loading the CSV file: {e}")
        return None

def plot_histogram(dataframe):
    plt.figure(figsize=(8, 6))
    plt.hist(dataframe['Age'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Histogram of Ages')
    st.pyplot()

# Streamlit app
def main():
    st.title("Question 3")

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        st.success("File uploaded successfully!")

        df = load_and_validate_csv(uploaded_file)

        if df is not None:
        

            plot_histogram(df)

if __name__ == "__main__":
    main()
