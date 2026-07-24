# Lab 1: Grade Evaluator & Archiver

This project has two small programs:

1. **grade-evaluator.py** - reads a student's grades from a CSV file and tells you if they passed or failed.
2. **organizer.sh** - archives that grades file and starts a fresh, empty one, so you are ready for the next batch.

## What you need

- Python 3 installed
- A terminal that can run bash scripts (WSL, Git Bash, or any Linux/Mac terminal)

## How the grades file should look

The program expects a file called grades.csv in the same folder, with these columns:

assignment,group,score,weight
Quiz,Formative,85,20
Midterm,Summative,70,20

- assignment - the name of the assignment
- group - either Formative or Summative
- score - a number between 0 and 100
- weight - how much that assignment counts, as a percentage

One rule to keep in mind: all your Formative assignments must add up to exactly 60, and all your Summative assignments must add up to exactly 40. If they do not, the program will tell you and stop.

## Running the grade evaluator

1. Make sure grades.csv is sitting in the same folder as grade-evaluator.py.
2. Open a terminal in that folder and run:

python grade-evaluator.py

3. It will print a report showing the student's score, GPA, and whether they passed or failed. If they failed because of formative assignments, it will also tell you which assignment(s) they can resubmit.

If something goes wrong - the file is missing, the weights do not add up right, or a score is invalid - the program will explain what happened instead of just crashing.

## Running the organizer script

This script is meant to be run after you are done with a batch of grades. It moves your current grades.csv into an archive folder (renaming it with the date and time), and leaves you a brand new empty grades.csv to start fresh.

1. Open a terminal in the project folder.
2. Run:

bash organizer.sh

3. Check the archive folder - you will see your old grades file saved there with a timestamp in the name, like grades_20260724-115714.csv.
4. Check organizer.log - every time you run the script, it adds a line recording what it archived and when.

If there is no grades.csv to archive, the script will just tell you there is nothing to do, instead of causing an error.

## A typical way to use both together

python grade-evaluator.py
bash organizer.sh

First check the grades, then archive them and start fresh for the next batch.
