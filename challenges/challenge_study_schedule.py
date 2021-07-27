def study_schedule(permanence_periods, target_time):
    """Faça o código aqui."""
    students = 0
    if target_time is None:
        return None
    for period in permanence_periods:
        for time in period:
            if type(time) != int:
                return None
        if period[0] <= target_time <= period[1]:
            students += 1
    return students
