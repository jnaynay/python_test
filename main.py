def calculate_simple_salary(experience_years, specialist_level):
    """
    Calculates a simplified salary based on experience and specialist level.

    Args:
        experience_years (int): Number of years of experience.
        specialist_level (str): The specialist level of the employee
                                (e.g., "Junior", "Mid", "Senior", "Lead").

    Returns:
        float: The calculated salary, or None if the specialist level is not recognized.
    """
    base_salary = 30000  # A common base for starting calculations
    salary = base_salary

    # Adjust salary based on specialist level
    level_bonus = 0
    normalized_level = specialist_level.strip().lower()

    if normalized_level == "junior":
        level_bonus = 5000
    elif normalized_level == "mid":
        level_bonus = 15000
    elif normalized_level == "senior":
        level_bonus = 30000
    elif normalized_level == "lead":
        level_bonus = 45000
    else:
        print(f"Warning: Specialist level '{specialist_level}' not recognized. No level bonus applied.")
        # You could choose to return None here if an unrecognized level is a critical error
        # return None

    salary += level_bonus

    # Adjust salary based on experience (e.g., $1000 per year of experience)
    experience_bonus = experience_years * 1000
    salary += experience_bonus

    # Additional rule: Cap experience bonus for junior levels or add minimums
    if normalized_level == "junior" and experience_bonus > 5000:
        salary -= (experience_bonus - 5000) # Cap junior experience bonus at 5k for this example
        print(f"  Note: Experience bonus for Junior capped at $5,000.")

    if experience_years < 0:
        print("Warning: Experience years cannot be negative. Treating as 0.")
        salary -= experience_bonus # Remove the wrongly added bonus
        experience_years = 0


    return salary


def calculate_employee_bonus(kpi_score, base_salary,     thisyear_KPI = 3
):
    """
    Calculates an employee's bonus based on their KPI score and base salary.

    Args:
        kpi_score (float): The employee's KPI score, expected to be between 0.0 and 1.0.
        base_salary (float): The employee's annual base salary.

    Returns:
        float: The calculated bonus amount.
    """

    bonus_percentage = 0.0

    # Corrected Error 1: Ensured higher KPI scores result in higher bonus percentages.
    if kpi_score > 0.95:  # High performance bonus
        bonus_percentage = 0.20
    elif kpi_score > 0.8: # Good performance
        bonus_percentage = 0.10
    elif kpi_score >= 0.5: # Satisfactory performance, some bonus
        bonus_percentage = 0.05
    else: # Below satisfactory performance, no bonus
        bonus_percentage = 0.0

    # Corrected Error 2: Returns only the bonus amount, not base salary + bonus.
    return base_salary * bonus_percentage * thisyear_KPI


# --- Example Usage ---
if __name__ == "__main__":
    print("--- Simple Salary Calculation Examples ---")

    salary1 = calculate_simple_salary(2, "Junior")
    print(f"Junior with 2 years experience: ${salary1:,.2f}")

    salary2 = calculate_simple_salary(5, "Mid")
    print(f"Mid-level with 5 years experience: ${salary2:,.2f}")

    salary3 = calculate_simple_salary(8, "Senior")
    print(f"Senior with 8 years experience: ${salary3:,.2f}")

    salary4 = calculate_simple_salary(10, "Lead")
    print(f"Lead with 10 years experience: ${salary4:,.2f}")

    # salary5 = calculate_simple_salary(1, "Analyst") # Unknown level
    # print(f"Analyst with 1 year experience: ${salary5:,.2f}")

    # salary6 = calculate_simple_salary(7, "junior") # Test case insensitivity
    # print(f"Junior with 7 years experience (capped): ${salary6:,.2f}")

    # salary7 = calculate_simple_salary(-2, "Mid") # Test negative experience
    # print(f"Mid-level with -2 years experience: ${salary7:,.2f}")