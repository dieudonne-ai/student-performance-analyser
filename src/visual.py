"""
a small bonnus project to practice data analysis and visualization skills. We will analyze student performance data and create visualizations to gain insights into the factors that affect student scores. The dataset contains information about students' study hours, scores, and class. We will use the matplotlib library to create various plots to visualize the data.
"""


import matplotlib.pyplot as plt
import pandas as pd

def read_data(file_path):
    df = pd.read_csv(file_path)
    return df

def plot_score_distribution(df):
    plt.figure(figsize=(10, 6))
    plt.hist(df["score"], bins=20, color="skyblue", edgecolor="black")
    plt.title("Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Frequency")
    plt.grid(axis="y", alpha=0.75)
    plt.show()

def plot_study_hours_vs_score(df):
    plt.figure(figsize=(10, 6))
    plt.scatter(df["study_hours"], df["score"], color="orange", edgecolor="black")
    plt.title("Study Hours vs Score")
    plt.xlabel("Study Hours")
    plt.ylabel("Score")
    plt.grid()
    plt.show()

def plot_average_score_by_class(df):
    avg_scores = df.groupby("class")["score"].mean()
    plt.figure(figsize=(10, 6))
    avg_scores.plot(kind="bar", color="lightgreen", edgecolor="black")
    plt.title("Average Score by Class")
    plt.xlabel("Class")
    plt.ylabel("Average Score")
    plt.grid(axis="y", alpha=0.75)
    plt.show()

def main():
    df = read_data("../data/students.csv")
    plot_score_distribution(df)
    plot_study_hours_vs_score(df)
    plot_average_score_by_class(df)

if __name__ == "__main__":
    main()