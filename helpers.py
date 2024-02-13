def get_pH_color(pH_value):
    """
    This function takes a pH value from 0 to 14 and returns the corresponding pH color.
    The color scheme is based on a general understanding of pH indicator colors.
    """
    if not (0 <= pH_value <= 14):
        return "Invalid pH value. Please enter a value between 0 to 14."

    if pH_value < 3:
        return "Red"  # Strong acid
    elif pH_value < 6:
        return "Orange"  # Weak acid
    elif pH_value < 7:
        return "Yellow"  # Acidic
    elif pH_value == 7:
        return "Green"  # Neutral
    elif pH_value < 9:
        return "Blue"  # Basic
    else:
        return "Purple"  # Strong base
