def BMICalc(feet, inches, weight):
    weight_kg = float(weight * 0.45)
    height = float(((feet * 12) + inches) * 0.025)

    if height <= 0:
        raise ValueError("Height values cannot be zero or negative")

    bodyMassIndex = round(weight_kg / (height ** 2), 1)
    return bodyMassIndex



def Categorization(bodyMassIndex):
    if bodyMassIndex < 18.5:
        return "Underweight"
    elif 18.5 <= bodyMassIndex <= 24.9:
        return "Normal Weight"
    elif 25 <= bodyMassIndex <= 29.9:
        return "Overweight"
    elif bodyMassIndex >= 30:
        return "Obese"


if __name__ == "__main__":
    try:
        feet = float(input("Enter your height in feet: "))
        inches = float(input("Enter the rest of your height in inches: "))
        weight = float(input("Please enter your weight in pounds: "))

        bmi = BMICalc(feet, inches, weight)
        category = Categorization(bmi)

        print(f"Your BMI is: {bmi} and your category is: {category}")

    except ValueError as e:
        print(f"Error: {e}")
