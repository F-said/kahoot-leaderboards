import streamlit as st
import pandas as pd


def add_medal(rank):
    """ChatGPT generated code to color rows
    """
    if rank == 0:
        return "🥇"
    elif rank == 1:
        return "🥈"
    elif rank == 2:
        return "🥉"
    elif 3 <= rank <= 9:
        return "🎖️"
    else:
        return ""


# path to student file
STUDENT_PATH = r'data\students.csv'

st.title("Kahoot Leaderboard (Cohort A & Cohort B)")
st.text("🥇 1st place = gold")
st.text("🥈 2nd place = silver")
st.text("🥉 3rd place = bronze")
st.text("🎖️ 4th–10th = runner-ups")

# load data
student_df = pd.read_csv(STUDENT_PATH)

# sort and assign ranking
student_df = student_df.sort_values(by="score").reset_index(drop=True)
student_df['rank'] = student_df.index
student_df['name'] = student_df.apply(lambda row: f"{add_medal(row['rank'])} {row['name']}", axis=1)
student_df.drop(columns=['rank'], inplace=True)

# display
st.dataframe(student_df)
