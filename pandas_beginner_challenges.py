"""
Link Challenge: https://docs.google.com/document/d/1kd4iXiXSdD_alCAKPncdf-oP9Zb-KAYgW9l5J265_u0/edit?tab=t.8xn3v27c3tfw
hello
"""

import pandas as pd

student_data = {
    "name": ["Alex", "Ben", "Chloe", "Daniel", "Emma",
             "Finn", "Grace", "Henry", "Iris", "Jack"],

    "class": ["8A", "8A", "8B", "8B", "8A",
              "8C", "8C", "8B", "8A", "8C"],

    "math": [88, 72, 95, 64, 91, 78, 85, 69, 97, 81],

    "english": [76, 85, 89, 70, 94, 82, 79, 74, 91, 87],

    "science": [90, 68, 92, 75, 88, 80, 84, 71, 96, 83],

    "study_hours": [8, 5, 12, 4, 10, 7, 9, 3, 14, 6],

    "sleep_hours": [7.5, 8, 6.5, 8.5, 7, 7.5, 8, 9, 6, 8],

    "club": ["Robotics", "Football", "Science", "Football",
             "Debate", "Robotics", "Debate", "Football",
             "Science", "Robotics"]
}

students = pd.DataFrame(student_data) #task 1
students.to_csv('students.csv', index=False) #task 2
df = pd.read_csv('students.csv') #task 3

task_4 = df.loc[:, 'math']
task_5 = df.loc[:, ['name', 'math', 'english']]
task_6 = df.club
task_7 = df.iloc[0, :]
task_8 = df.iloc[:4, :]
task_9 = df.iloc[:5, :3]
task_10 = df.iloc[-3:, :]
task_11 = df.loc[df["class"] == "8A"]
task_12 = df.loc[df['math'] >= 85]
task_13 = df.loc[(df['study_hours'] >= 8) & (df['math'] >= 85),
                 ["name", "math", "study_hours"]]
task_14 = df.loc[(df['club'] == 'Science') | (df['english'] >= 90)]
df['total_score'] = df[['math', 'english', 'science']].sum(axis=1) #task 15
df['average_score'] = df[['math', 'english', 'science']].mean(axis=1) #task 16
df['passed'] = True #task 17
df.loc[df['average_score'] < 75, 'passed'] = False #task 18
task_19 = df['math'].mean()
task_20 = df['english'].max()
task_21 = df['science'].min()
task_22 = df['study_hours'].median()
task_23 = df.describe()
task_24 = df['club'].value_counts()
task_25 = df['class'].unique()
task_26 = df['club'].nunique()
#---- Task 27 ----
constraints = ((df['average_score'] >= 85) &
            (df['study_hours'] >= 10) &
            (df['sleep_hours'] < 7))

high_performers = df.loc[constraints,
                        ['name', 'average_score', 'study_hours', 'sleep_hours', 'club']
                        ].sort_values(by='average_score', ascending=False)

print(high_performers)
print(df)
