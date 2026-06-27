Fitness Plan Generator

A Python-based command-line application that generates personalized fitness recommendations based on user input such as age, weight, height, and fitness goals.

The program calculates daily calorie needs and protein intake and suggests a basic workout structure depending on training frequency.

Purpose

This project was built to strengthen my understanding of:

Python functions and modular programming
Input validation and error handling
Mathematical calculations in programming
Conditional logic for decision-making systems
Basic algorithm design for personalized outputs
Features
Collects user data (age, weight, height, name, goal)
Validates numeric input to prevent incorrect entries
Calculates Basal Metabolic Rate (BMR)
Estimates daily calorie requirements based on fitness goal:
Fat loss
Maintenance
Muscle gain
Estimates protein intake based on body weight
Generates a basic workout split (1–6 days per week)
Calculation Method

The program uses the Mifflin-St Jeor Equation to estimate BMR:

BMR is calculated using weight, height, and age
Daily calorie needs are adjusted based on the selected goal
Protein intake is estimated using standard fitness guidelines
How to Run

Run the script using Python:

python FITWPY-Gym Trainer.py

Follow the prompts in the terminal to generate a personalized fitness plan.

Concepts Used
Variables and user input/output
Functions with parameters and return values
Conditional statements (if/else logic)
Loops (while)
Exception handling (try/except)
Basic mathematical modeling
Notes
This is a beginner-level project focused on applying Python fundamentals to a real-world use case
The program is rule-based and does not use machine learning
