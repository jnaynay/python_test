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

def calculate_employee_bonus(kpi_score, base_salary):
    """
    Calculates an employee's bonus based on their KPI score and base salary.

    Args:
        kpi_score (float): The employee's KPI score, expected to be between 0.0 and 1.0.
        base_salary (float): The employee's annual base salary.

    Returns:
        float: The calculated bonus amount.
    """

    # Error 1 (Logic Error): The bonus percentage for high performance is less than good performance.
    # It should be 0.20 for > 0.95 and 0.10 for > 0.8
    if kpi_score > 0.95:  # High performance bonus
        bonus_percentage = 0.05  # This is intentionally too low
    elif kpi_score > 0.8: # Good performance
        bonus_percentage = 0.15  # This is intentionally higher than the top tier
    elif kpi_score >= 0.5: # Satisfactory performance, some bonus
        bonus_percentage = 0.05
    else:
        bonus_percentage = 0.0

    # Error 2 (Logic Error): Bonus is added to the base salary instead of being a separate amount.
    # The function should return *only* the bonus amount.
    return base_salary + (base_salary * bonus_percentage)

# Example Usage with intentional logic errors:
# print(calculate_employee_bonus(0.98, 60000)) # Expected: 12000 (0.20 * 60000) but will return 63000 (60000 + 0.05 * 60000)
# print(calculate_employee_bonus(0.85, 75000)) # Expected: 7500 (0.10 * 75000) but will return 86250 (75000 + 0.15 * 75000)
# print(calculate_employee_bonus(0.6, 50000))  # Expected: 2500 (0.05 * 50000) but will return 52500 (50000 + 0.05 * 50000)
# print(calculate_employee_bonus(0.4, 40000))  # Expected: 0 but will return 40000 (40000 + 0.0 * 40000)


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