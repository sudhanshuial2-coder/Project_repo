
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


# -----------------------------------------
# RESULT STATISTICS ANALYZER
# Project No: 94
# -----------------------------------------


def load_results(filename="results.csv"):

    if not os.path.exists(filename):
        print("\nError: results.csv file not found!")
        print("Please create results.csv in the project folder.")
        return None

    try:
        df = pd.read_csv(filename)

        # Check required columns
        if not {"RollNo", "Marks"}.issubset(df.columns):
            print("Error: CSV must contain RollNo and Marks columns.")
            return None

        # Convert marks into numeric values
        df["Marks"] = pd.to_numeric(
            df["Marks"], errors="coerce"
        )

        valid_marks = []

        for index, row in df.iterrows():

            roll = row["RollNo"]
            marks = row["Marks"]

            if pd.isna(marks):
                print(
                    f"Warning: Row {index + 2} skipped - "
                    "missing or invalid marks."
                )

            elif marks < 0 or marks > 100:
                print(
                    f"Warning: Row {index + 2} skipped - "
                    "marks must be between 0 and 100."
                )

            else:
                valid_marks.append(marks)

        return np.array(valid_marks, dtype=float)

    except Exception as e:
        print("Error reading CSV file:", e)
        return None


# -----------------------------------------
# DISPLAY STATISTICS
# -----------------------------------------

def show_statistics(marks):

    if len(marks) == 0:
        print("\nNo valid marks found. Nothing to analyse.")
        return

    print("\n========== RESULT STATISTICS ==========")

    print("Students:", len(marks))

    print("Mean:", f"{np.mean(marks):.2f}")

    print("Median:", f"{np.median(marks):.2f}")

    # Calculate mode using Pandas
    mode_values = pd.Series(marks).mode()

    if len(mode_values) > 0:
        if len(mode_values) == len(marks):
            print("Mode: No unique mode (all values occur once)")
        else:
            print("Mode:", ", ".join(
                str(int(x)) if x.is_integer() else str(x)
                for x in mode_values
            ))

    print("Highest:", f"{np.max(marks):.0f}")

    print("Lowest:", f"{np.min(marks):.0f}")

    print(
        "Standard Deviation:",
        f"{np.std(marks):.2f}"
    )

    pass_count = np.sum(marks >= 40)
    fail_count = np.sum(marks < 40)

    percentage = (pass_count / len(marks)) * 100

    print("Pass:", pass_count)
    print("Fail:", fail_count)
    print("Pass Percentage:", f"{percentage:.2f}%")

    print("=======================================")


# -----------------------------------------
# PASS PERCENTAGE AND DISTRIBUTION
# -----------------------------------------

def show_distribution(marks):

    if len(marks) == 0:
        print("\nNo valid marks found. Nothing to analyse.")
        return

    pass_count = np.sum(marks >= 40)
    fail_count = np.sum(marks < 40)

    pass_percentage = (pass_count / len(marks)) * 100

    # Define marks bands
    bands = ["0-39", "40-59", "60-79", "80-100"]

    counts = [
        np.sum((marks >= 0) & (marks <= 39)),
        np.sum((marks >= 40) & (marks <= 59)),
        np.sum((marks >= 60) & (marks <= 79)),
        np.sum((marks >= 80) & (marks <= 100))
    ]

    print("\n======= PASS PERCENTAGE AND DISTRIBUTION =======")

    print("Passed:", pass_count)
    print("Failed:", fail_count)

    print("Pass Percentage:", f"{pass_percentage:.2f}%")

    print("\nMarks Distribution:")

    for band, count in zip(bands, counts):
        print(f"{band}: {count}")

    print("================================================")

    # Display bar chart
    plt.figure(figsize=(9, 5))

    bars = plt.bar(
        bands,
        counts,
        edgecolor="black"
    )

    plt.title("Student Marks Distribution")
    plt.xlabel("Marks Range")
    plt.ylabel("Number of Students")

    plt.bar_label(bars)

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    plt.tight_layout()
    plt.show()


# -----------------------------------------
# MAIN MENU
# -----------------------------------------

def main():

    print("\n===================================")
    print("     RESULT STATISTICS ANALYZER")
    print("===================================")

    marks = load_results()

    if marks is None:
        return

    while True:

        print("\n------------ MAIN MENU ------------")
        print("1. Show Statistics")
        print("2. Pass Percentage and Distribution")
        print("3. Exit")
        print("-----------------------------------")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":

            show_statistics(marks)

        elif choice == "2":

            show_distribution(marks)

        elif choice == "3":

            print("\nThank you for using Result Statistics Analyzer!")
            break

        else:

            print("\nInvalid choice! Please enter 1, 2 or 3.")


# -----------------------------------------
# PROGRAM EXECUTION
# -----------------------------------------

if __name__ == "__main__":
    main()
