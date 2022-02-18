def get_grade(*scores):
    # Code here
    average = sum([*scores])/len([*scores])
    if 90 <= average <= 100: return 'A'
    elif 80 <= average < 90: return 'B'
    elif 70 <= average < 80: return 'C'
    elif 60 <= average < 70: return 'D'
    return 'F'
