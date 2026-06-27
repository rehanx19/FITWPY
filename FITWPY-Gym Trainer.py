print("                                                              FITWCHAT")
def ask_number(question):
    while True:
        try:
            number = float(input(question))
            if number > 0:
                return number
            print("Please enter a number above 0.")
        except ValueError:
            print("Please enter a valid number.")


def ask_choice(question, choices):
    print(question)
    for i in range(len(choices)):
        print(str(i + 1) + ". " + choices[i])

    while True:
        answer = input("Choose a number or type your answer: ").lower().strip()
        if answer.isdigit():
            answer = int(answer)
            if 1 <= answer <= len(choices):
                return choices[answer - 1]
        else:
            for choice in choices:
                if answer == choice:
                    return choice
        print("Please choose a valid number.")


def calculate_bmr(sex, weight, height, age):
    if sex == "male":
        return (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        return (10 * weight) + (6.25 * height) - (5 * age) - 161


def get_activity_multiplier(days):
    if days <= 2:
        return 1.35
    elif days <= 4:
        return 1.50
    else:
        return 1.65


def get_calorie_goal(maintenance, goal):
    if goal == "lean bulk":
        return round(maintenance + 250), "bulk"
    elif goal == "muscle and strength":
        return round(maintenance + 200), "bulk"
    elif goal == "fat loss / cut":
        return round(maintenance - 400), "cut"
    elif goal == "athletic and toned":
        return round(maintenance - 100), "recomp"
    else:
        return round(maintenance), "maintain"


def get_protein_goal(weight, goal_type):
    if goal_type == "cut":
        return round(weight * 2.2)
    elif goal_type == "bulk":
        return round(weight * 1.8)
    else:
        return round(weight * 2.0)


def get_workout_plan(days, goal, physique):
    if days == 1:
        split = [
            "Day 1: Full body - squat or leg press, bench press, row, shoulder press, curls, triceps, abs"
        ]
    elif days == 2:
        split = [
            "Day 1: Upper body - chest, back, shoulders, arms",
            "Day 2: Lower body - quads, hamstrings, glutes, calves, abs"
        ]
    elif days == 3:
        split = [
            "Day 1: Push - chest, shoulders, triceps",
            "Day 2: Pull - back, biceps, rear delts",
            "Day 3: Legs - quads, hamstrings, glutes, calves, abs"
        ]
    elif days == 4:
        split = [
            "Day 1: Upper body strength",
            "Day 2: Lower body strength",
            "Day 3: Upper body muscle",
            "Day 4: Lower body muscle + abs"
        ]
    elif days == 5:
        split = [
            "Day 1: Push",
            "Day 2: Pull",
            "Day 3: Legs",
            "Day 4: Upper body",
            "Day 5: Lower body + arms"
        ]
    else:
        split = [
            "Day 1: Push",
            "Day 2: Pull",
            "Day 3: Legs",
            "Day 4: Push",
            "Day 5: Pull",
            "Day 6: Legs",
            "Day 7: Rest"
        ]

    if goal == "fat loss / cut":
        cardio = "Do 20-30 minutes of incline walking or cycling 3 times per week."
    elif physique == "skinny fat":
        cardio = "Do 15-20 minutes of light cardio 2 times per week. Focus more on lifting."
    else:
        cardio = "Do 10-15 minutes of light cardio 2 times per week for health."

    return split, cardio


def print_plan(name, sex, age, height, weight, physique, days, goal, calories, protein, goal_type, workout_split, cardio):
    print("\n" + "=" * 45)
    print("YOUR FITNESS PLAN")
    print("=" * 45)

    print("\nProfile:")
    print("Name:", name)
    print("Sex:", sex)
    print("Age:", int(age))
    print("Height:", int(height), "cm")
    print("Weight:", int(weight), "kg")
    print("Current physique:", physique)
    print("Goal:", goal)
    print("Training days:", days, "days per week")

    print("\nNutrition:")
    print("Calories per day:", calories, "calories")
    print("Goal type:", goal_type)
    print("Protein per day:", protein, "grams")
    print("Simple eating rule: hit your calories and protein every day.")
    print("Drink water, eat mostly normal whole foods, and do not skip protein.")

    print("\nWorkout:")
    for day in workout_split:
        print("-", day)

    print("\nExercise rules:")
    print("- Do 3 sets per exercise.")
    print("- Do 8-12 reps for most exercises.")
    print("- Rest 1-2 minutes between sets.")
    print("- When 12 reps gets easy, increase the weight next time.")
    print("-", cardio)

    print("\nExtra instructions:")
    if physique == "skinny":
        print("- Eat your full calories. Do not be scared of gaining a little weight.")
        print("- Focus on getting stronger every week.")
    elif physique == "skinny fat":
        print("- Do not crash diet. Lift hard and keep protein high.")
        print("- Your main goal is to build muscle while slowly losing fat.")
    elif physique == "overweight":
        print("- Stay consistent with the calorie target.")
        print("- Walk 7,000-10,000 steps daily if possible.")
    else:
        print("- Keep training hard and track your progress weekly.")

    print("\nCheck progress:")
    print("- Weigh yourself 3 times per week and use the average.")
    print("- If weight is not changing after 2 weeks, adjust calories by 150-200.")
    print("- Take progress pictures every 2 weeks.")
    print("=" * 45)


name = input("What is your name? ")
sex = ask_choice("What is your sex?", ["male", "female"])
age = ask_number("How old are you? ")
height = ask_number("What is your height in cm? ")
weight = ask_number("What is your weight in kg? ")

physique = ask_choice(
    "What does your current physique look like?",
    ["skinny", "skinny fat", "average", "overweight", "already muscular"]
)

days = int(ask_number("How many days per week do you want to work out? Pick 1-6: "))
if days < 1:
    days = 1
elif days > 6:
    days = 6

goal = ask_choice(
    "What type of body do you want to build?",
    ["lean bulk", "fat loss / cut", "athletic and toned", "muscle and strength", "maintain"]
)

bmr = calculate_bmr(sex, weight, height, age)
maintenance = bmr * get_activity_multiplier(days)
calories, goal_type = get_calorie_goal(maintenance, goal)
protein = get_protein_goal(weight, goal_type)
workout_split, cardio = get_workout_plan(days, goal, physique)

print_plan(name, sex, age, height, weight, physique, days, goal, calories, protein, goal_type, workout_split, cardio)
