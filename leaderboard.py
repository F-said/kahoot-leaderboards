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
STUDENT_PATH = r'data/scores.csv'

st.title("Kahoot Leaderboard (Cohort A & Cohort B)")
st.text("🥇 1st place; 🥈 2nd place; 🥉 3rd place; 🎖️ 4th–10th")

# load data
student_df = pd.read_csv(STUDENT_PATH)

# convert to ints
num_cols = student_df.select_dtypes(include="number").columns
student_df[num_cols] = (
    student_df[num_cols]
    .apply(pd.to_numeric, errors="coerce")
    .round(0)
    .astype("Int64")
)

# sort and assign ranking
student_df = student_df.sort_values(by="Total Score (points)", ascending=False).reset_index(drop=True)
student_df['Rank'] = student_df.index
student_df['Player'] = student_df.apply(lambda row: f"{add_medal(row['Rank'])} {row['Player']}", axis=1)
student_df.drop(columns=['Rank'], inplace=True)

# display
st.table(student_df)
