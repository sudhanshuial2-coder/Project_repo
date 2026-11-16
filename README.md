# Project_repo

# Result Statistics Analyzer (Project No: 94)

A Python-based command-line tool designed to read student marks from a CSV file, validate entries, compute comprehensive statistical metrics using **Pandas** and **NumPy**, and generate visual distribution charts using **Matplotlib**.

---

## 🚀 Features

* **Automated CSV Processing**: Reads student data (`RollNo`, `Marks`) securely using Pandas.
* **Robust Error Handling**: Automatically catches missing files, empty dataframes, non-numeric entries, and out-of-range marks (`< 0` or `> 100`) with descriptive warnings.
* **Statistical Analysis**: Computes Mean, Median, Mode, Highest mark, Lowest mark, and Standard Deviation.
* **Pass/Fail Metrics**: Evaluates passing status (passing threshold $\ge 40$) and computes overall pass percentages.
* **Graphical Visualization**: Displays a clean bar chart mapping student performance across distinct score bands (`0-39`, `40-59`, `60-79`, `80-100`).

---

## 🛠️ Prerequisites & Dependencies

Make sure you have Python 3 installed along with the required third-party libraries:

```bash
pip install pandas numpy matplotlib
```

---

## 📂 Project Structure

```text
📁 Result-Statistics-Analyzer/
│
├── results.csv          # Input data file containing student roll numbers and marks
├── analyzer.py          # Main Python script containing all analysis logic
└── README.md            # Project documentation
```

---

## 📊 Sample `results.csv` Format

Your input file (`results.csv`) should follow this structure:

```csv
RollNo,Marks
1,45
2,56
3,67
4,72
5,72
6,80
7,85
8,90
9,38
10,95
```

---

## 🏃 How to Run the Project

1. Clone the repository or download the source code.
2. Ensure your `results.csv` file is placed in the same directory as the script.
3. Run the script from your terminal/console:

```bash
python analyzer.py
```

4. Follow the interactive **Main Menu** prompts to:
   * View full statistics (Mean, Median, Mode, Standard Deviation, etc.).
   * Check pass percentages and band distribution charts.

---

## 🧪 Test Cases Handled

* **Test Case 1 (Normal Input)**: Computes accurate statistics for a complete set of valid student marks.
* **Test Case 2 (Boundary/Minimum Input)**: Gracefully handles edge cases like single-row inputs.
* **Test Case 3 (Invalid Input)**: Identifies out-of-range marks or missing data rows and skips them safely with a warning message.
* **Test Case 4 (Different Valid Scenario)**: Calculates band-wise distribution counts and triggers the Matplotlib bar chart visualization.

---

## 💡 Technologies Used

* **Python 3**
* **Pandas** (Data manipulation and mode calculations)
* **NumPy** (Mathematical and statistical computations)
* **Matplotlib** (Data visualization and bar plotting)
