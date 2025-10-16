import pandas as pd

# Load CSV file
df = pd.read_csv("C:/Users/soban/Documents/StudentScores.csv")

# Display dataset
print("Student Scores Data:")
print(df, "\n")

# Compute average score per student
df["Average"] = df[["English", "Maths", "Physics", "Chemistry", "Biology", "Geography", "Further Maths", "Computer Science", "Technical Drawing", "Fisheries", "Civic Education"]].mean(axis=1)

# Find highest and lowest scores per subject
highest_scores = df[["English", "Maths", "Physics", "Chemistry", "Biology", "Geography", "Further Maths", "Computer Science", "Technical Drawing", "Fisheries", "Civic Education"]].max()
lowest_scores = df[["English", "Maths", "Physics", "Chemistry", "Biology", "Geography", "Further Maths", "Computer Science", "Technical Drawing", "Fisheries", "Civic Education"]].min()

# Identify top-performing student
top_student = df.loc[df["Average"].idxmax()]

# Results
print("Average Scores per Student:")
print(df[["Name", "Average"]], "\n")

print("Highest Scores per Subject:")
print(highest_scores, "\n")

print("Lowest Scores per Subject:")
print(lowest_scores, "\n")

print("Top Performing Student:")
print(top_student)

