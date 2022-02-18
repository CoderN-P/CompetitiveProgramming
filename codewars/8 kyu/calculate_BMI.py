def bmi(weight, height):
    if weight/height**2 <= 18.5:
        return "Underweight"
    elif weight/height**2 <= 25:
        return "Normal"
    elif weight/height**2 <= 30:
        return "Overweight"
    return "Obese"