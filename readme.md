# 🐼 Pandas Beginner Project

## Student Performance Analyzer

### 📌 Project Overview

Your school has collected data about students' academic performance and
study habits.

Your task is to use **Pandas** to create, read, select, filter, modify,
and analyze the dataset.

### Dataset Columns

  Column          Description
  --------------- -------------------------------
  `name`          Student name
  `class`         Student's class
  `math`          Math score
  `english`       English score
  `science`       Science score
  `study_hours`   Study hours per week
  `sleep_hours`   Average sleep hours per night
  `club`          School club

------------------------------------------------------------------------

## Part 1 --- Creating a DataFrame

### Task 1 --- Create the DataFrame

Convert the provided `student_data` dictionary into a Pandas DataFrame
called `students`.

Display the completed DataFrame.

------------------------------------------------------------------------

## Part 2 --- Writing and Reading Files

### Task 2 --- Write a CSV File

Save the `students` DataFrame into a CSV file called:

`students.csv`

Do **not** save the DataFrame index in the CSV file.

### Task 3 --- Read a CSV File

Read `students.csv` and store the resulting DataFrame in a variable
called `df`.

Display the first **5 rows** of the DataFrame.

------------------------------------------------------------------------

## Part 3 --- Basic Selection

### Task 4 --- Select One Column

Select only the `math` column.

The result should be a **Series**.

### Task 5 --- Select Multiple Columns

Select the following columns:

-   `name`
-   `math`
-   `english`

The result should be a **DataFrame**.

### Task 6 --- Dot Notation

Select the `club` column using **dot notation** instead of square
brackets.

------------------------------------------------------------------------

## Part 4 --- Indexing with `iloc`

### Task 7 --- Select the First Student

Using `.iloc`, select the **first student** in the DataFrame.

### Task 8 --- Select the First Four Students

Using `.iloc`, select the **first 4 students**.

### Task 9 --- Select Specific Rows and Columns

Using only `.iloc`, select the **first 5 students** and the following
columns:

-   `name`
-   `class`
-   `math`

### Task 10 --- Last Three Students

Using `.iloc`, select the **last 3 students**.

Your solution should work without knowing how many rows are in the
DataFrame.

------------------------------------------------------------------------

## Part 5 --- Filtering with `loc`

### Task 11 --- Filter by Class

Select all students who are in class `8A`.

### Task 12 --- Filter by Score

Select all students whose Math score is **at least 85**.

### Task 13 --- Multiple Conditions

Select students who meet **both** of the following conditions:

-   Study at least **8 hours per week**
-   Have a Math score of at least **85**

Return only these columns:

-   `name`
-   `math`
-   `study_hours`

### Task 14 --- OR Condition

Select students who meet **at least one** of the following conditions:

-   Belong to the `Science` club
-   Have an English score of at least **90**

------------------------------------------------------------------------

## Part 6 --- Assigning and Creating Columns

### Task 15 --- Total Score

Create a new column called `total_score`.

Calculate each student's total score using their:

-   Math score
-   English score
-   Science score

### Task 16 --- Average Score

Create a new column called `average_score`.

Calculate each student's average score across:

-   Math
-   English
-   Science

### Task 17 --- Create a Passed Column

Create a new column called `passed`.

Initially, set the value to `True` for **every student**.

### Task 18 --- Modify Values with `loc`

Change `passed` to `False` for students whose:

`average_score < 75`

Use `.loc` to modify the appropriate values.

------------------------------------------------------------------------

## Part 7 --- Summary Functions

### Task 19 --- Mean

Find the **average Math score** of all students.

### Task 20 --- Maximum

Find the **highest English score**.

### Task 21 --- Minimum

Find the **lowest Science score**.

### Task 22 --- Median

Find the **median number of study hours per week**.

### Task 23 --- Statistical Summary

Use one Pandas command to generate a **statistical summary of all
numerical columns** in the DataFrame.

------------------------------------------------------------------------

## Part 8 --- Exploring the Dataset

### Task 24 --- Count Club Members

Find how many students belong to each club.

### Task 25 --- Unique Classes

Find all **unique class names** in the dataset.

### Task 26 --- Number of Unique Clubs

Find the **number of unique clubs** represented in the dataset.

------------------------------------------------------------------------

## Part 9 --- Final Challenge

### Task 27 --- High Performers

Your teacher wants to identify:

> **Which high-performing students may be studying a lot while sleeping
> relatively little?**

A student meets the criteria if:

-   `average_score >= 85`
-   `study_hours >= 10`
-   `sleep_hours < 7`

Create a DataFrame called `high_performers`.

Keep only the following columns:

-   `name`
-   `average_score`
-   `study_hours`
-   `sleep_hours`
-   `club`

Finally, sort the students from **highest to lowest `average_score`**.

------------------------------------------------------------------------

# ⭐ Bonus Challenges

## Bonus Challenge 1 --- Highest-Performing Student

Find the student with the **highest average score**.

Display:

-   Student's name
-   Average score

------------------------------------------------------------------------

## Bonus Challenge 2 --- Largest Class

Find the **class with the most students**.

Display:

-   Class name
-   Number of students

------------------------------------------------------------------------

## Bonus Challenge 3 --- Class 8A Math Performance

Calculate the **average Math score** of students in class `8A`.

------------------------------------------------------------------------

## Bonus Challenge 4 --- Above-Average Math Students

Calculate the **overall average Math score**.

Then find all students whose Math score is **higher than the overall
average**.

Display:

-   Student's name
-   Math score

------------------------------------------------------------------------

## Bonus Challenge 5 --- Club Performance

Calculate the **average `average_score` of students in each club**.

Your result should have a structure similar to:

  Club         Average Score
  ---------- ---------------
  Robotics               ...
  Football               ...
  Science                ...
  Debate                 ...

------------------------------------------------------------------------

# ✅ Project Completion Checklist

By the end of this project, you should be able to work with:

-   [ ] Creating DataFrames
-   [ ] Reading CSV files
-   [ ] Writing CSV files
-   [ ] Selecting columns
-   [ ] `.loc`
-   [ ] `.iloc`
-   [ ] Boolean filtering
-   [ ] Multiple conditions with `&` and `|`
-   [ ] Creating new columns
-   [ ] Assigning and modifying values
-   [ ] `.sum()`
-   [ ] `.mean()`
-   [ ] `.median()`
-   [ ] `.min()`
-   [ ] `.max()`
-   [ ] `.describe()`
-   [ ] `.value_counts()`
-   [ ] `.unique()`
-   [ ] `.nunique()`
-   [ ] `.sort_values()`
-   [ ] Basic data analysis

------------------------------------------------------------------------

## 🎯 Goal

Complete all **27 tasks** and the **5 bonus challenges** without copying
solutions.

When you encounter an error, use the traceback to identify whether the
problem comes from a **column name, row/column selection, condition, or
method**.
