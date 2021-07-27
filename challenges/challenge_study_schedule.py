def check_values(values):
    for value in values:
        if type(value) != int:
            return False
    return True


def study_schedule(permanence_periods, target_time):
    """Faça o código aqui."""
    students = 0
    if target_time is None or permanence_periods is None:
        return None
    for period in permanence_periods:
        if not check_values(period):
            return None
        if period[0] <= target_time <= period[1]:
            students += 1
    return students
