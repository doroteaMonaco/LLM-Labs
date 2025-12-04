
def compute_average(grades):
    """
    Computes the average of grades, excluding the best and worst grades.

    Args:
        grades (list): A list of six grades, where each grade is between 18 and 33.

    Returns:
        float: The computed average.
    """
    if len(grades) != 6:
        raise ValueError("The list must contain exactly six grades.")
    for grade in grades:
        if grade < 18 or grade > 33:
            raise ValueError("Grades must be between 18 and 33.")

    sorted_grades = sorted(grades)
    sorted_without_extremes = sorted_grades[1:-1]
    return sum(sorted_without_extremes) / len(sorted_without_extremes)