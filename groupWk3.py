# Import datetime so that it can be
# used to compute a person's age.
"""
Asks the user to enter four values:
gender
birthdate in this format: YYYY-MM-DD
weight in U.S. pounds
height in U.S. inches
Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg).
Converts inches to centimeters (1 in = 2.54 cm).
Calculates age, BMI, and BMR.
Prints age, weight in kg, height in cm, BMI, and BMR.
"""

from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('What is your gender?(M or F?): ').upper()[0]
    birthdate = input('What is your birthdate? (YYYY-MM-DD): ')
    pounds = int(input("Enter your weight in U.S. pounds: "))
    inches = int(input("Enter your height in U.S. inches: "))
    
    # Call the compute_age, kg_from_lb, cm_from_in,
    age = compute_age(birthdate)
    kg = kg_from_lb(pounds)
    cm = cm_from_in(inches)
    
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    bmi = body_mass_index(kg, cm)
    bmr = basal_metabolic_rate(gender, kg, cm, age)
    # Print the results for the user to see.


    #Age (years): 19
    #Weight (kg): 56.70
    #Height (cm): 137.2
    #Body mass index: 30.1
    #Basal metabolic rate (kcal/day): 1315
    print(f"Age (years): {age}")
    print(f"Weight (kg): {kg}")
    print(f"Height (cm): {cm}")
    print(f"BMI : {bmi}")
    print(f"BMR (kcal/day): {bmr}")
    

def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(pounds):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    kilograms = pounds * 0.45359237
    return kilograms


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    Converts inches to centimeters (1 in = 2.54 cm).
    """
    cm = inches * 2.54
    return cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = weight / height ** 2 * 10000
    #bmi = 10,000 * weight / height ^ 2
    
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == 'F':
        #(women)  bmr = 447.593 + 9.247 weight + 3.098 height − 4.330 age
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        #(men)  bmr = 88.362 + 13.397 weight + 4.799 height − 5.677 age
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    
    return bmr


# Call the main function so that
# this program will start executing.
main()
