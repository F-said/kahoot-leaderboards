import streamlit as st
import pandas as pd

# Replace with your actual GCS URLs or paths if authenticated
GCS_PATH_1 = 'gs://dsteam_data_store/172/Canvas/csv/students_course_172_2025-06-11.csv'
GCS_PATH_2 = 'gs://dsteam_data_store/176/Canvas/csv/students_course_176_2025-06-12.csv'

@st.cache_data
def load_student_names(path1, path2):
    df1 = pd.read_csv(path1)
    df2 = pd.read_csv(path2)

    names1 = df1['name'].dropna().unique()
    names2 = df2['name'].dropna().unique()

    all_names = pd.Series(list(set(names1) | set(names2))).sort_values().reset_index(drop=True)
    return pd.DataFrame({'name': all_names, 'score': 0})


# Load Data
st.title("Leaderboard")
try:
    student_df = load_student_names(GCS_PATH_1, GCS_PATH_2)
    st.success("CSV files loaded successfully.")
except Exception as e:
    st.error(f"Error loading files: {e}")
    st.stop()

# Display
st.dataframe(student_df)
