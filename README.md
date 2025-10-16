# Data-Handling-with-Python
Student Score Analysis
■ Student Scores Data Analysis 
This project is a simple Python data analysis script that processes a dataset of students’ scores 
across multiple subjects using the pandas library. It computes each student’s average score, finds 
the highest and lowest scores per subject and identifies the overall top-performing student. 

■ Project Overview 
The script: 
1. Loads a CSV file containing student names and their scores. 
2. Displays the dataset for quick viewing. 
3. Calculates the average score per student. 
4. Determines the highest and lowest scores in each subject. 
5. Identifies the top-performing student based on the highest average score.
   
■ Requirements 
Ensure you have Python and pandas installed using the command: 
pip install pandas

■ How to Use 
1. Clone this repository or download the script. 
2. Place your dataset (e.g., StudentScores.csv) in a known directory. 
3. Update the CSV file path in the script. 
4. Run the script using: python student_scores.py (N.B: you can equally create yours from 
scratch).

■ Example Output 
Displays the student scores data, average scores, highest and lowest per subject and the top
performing student.

■ Data Format (CSV Example) 
h 
Maths 
Physics 
Chemistry 
Biology 
Geography 
Further Maths 
Computer Science 
Technical Drawing 
Fisherie
 80 
78 
85 
70 
82 
79 
90 
77 
88 
92 
85 
89 
90 
95 
91 
93 
89 

87 
■ Key Functions 
Function 
Purpose 
pd.read_csv() 
Loads the dataset 
df.mean(axis=1) 
Computes row-wise average 
df.max() / df.min() 
Finds subject highs and lows 
df.loc[df['Average'].idxmax()] 
Finds the top student
 
■■■ Author 
Sobanjo Oluwatosin 
■ AI/Ml Enthusiast 
■ https://github.com/TSobees  
■ License 
No license 
