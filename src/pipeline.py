"""
first project: student performance analyser
"""

import pandas as pd

# Load Data

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


# Clean Data

def clean_data(df):

    
    df["score"] = pd.to_numeric(df["score"], errors="coerce")
    df["study_hours"] = pd.to_numeric(df["study_hours"], errors="coerce")

    # remove missing values
    df = df.dropna()

    # keep only valid score range
    df = df[(df["score"] >= 0) & (df["score"] <= 20)]

    return df


# Add Grade Classification

def add_grade(df):

    def get_grade(score):
        if score >= 16:
            return "A"
        elif score >= 12:
            return "B"
        elif score >= 8:
            return "C"
        else:
            return "D"

    df["grade"] = df["score"].apply(get_grade)

    return df


# Analyze Data

def analyze_data(df):

    print("\nAverage score per class:")
    print(df.groupby("class")["score"].mean())

    print("\nAverage study hours:")
    print(df["study_hours"].mean())

    print("\nTop student:")
    print(df.loc[df["score"].idxmax()])

    summary = df.groupby("class").agg({
        "score": ["mean", "max", "min"],
        "study_hours": "mean"
    })

    print("\nSummary report:")
    print(summary)

    return summary


# Save Results

def save_results(summary):
    summary.to_csv("../result/report.csv")


# Main Pipeline

def main():

    df = load_data("../data/students.csv")

    df = clean_data(df)

    df = add_grade(df)

    summary = analyze_data(df)

    save_results(summary)


if __name__ == "__main__":
    main()
